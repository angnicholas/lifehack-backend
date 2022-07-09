# AUTH ENDPOINTS

## Login: `http://localhost:8000/auth/jwt/create`

Logs a user in.

### Payload

`
{
    "email":"test@test.com",
    "password":"test1234!"
}
`

### Response

`
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NzQ0MDY2MiwianRpIjoiOWUwZjAwOWY4Y2QxNDEyZDk0MmQxNWI0Yzg1ODFlN2EiLCJ1c2VyX2lkIjo2fQ.JeCzttgiSQdB84Z_Fhw8-p2lCrgtXIQzLjF0NnazVKA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3MzU0NTYyLCJqdGkiOiI0NjNlNjNlMDIyNGM0MzM0OWNkNzI4MDdlMDc1ZDE0MSIsInVzZXJfaWQiOjZ9.rEoohBTZuvXwObYiz3paX0u4Io90aKaQGxIwz7ICzuA"
}
`


## Signup:  `http://localhost:8000/auth/register`

Sign up

### Payload

Role is either IN (INSTITUTION) or EU (END USER).

`
{
    "email":"test@test.com",
    "display_name": "OCBC Bank",
    "password":"test1234!",
    "role":"IN"
}
`

### Response

`
{
    "id": 3,
    "email": "test@test.com",
    "display_name": "OCBC Bank",
    "role": "IN",
    "created_at": "2022-07-09T08:59:22.259095Z"
}
`



# END USER ENDPOINTS

## List all Codes:  `http://localhost:8000/verifier`

Lists all the codes sent from institutions.

### Payload

Nothing

### Response

`
[
    {
        "id": 2,
        "verification_code": "420",
        "time_sent": "2022-07-09T15:15:15Z",
        "create_at": "2022-07-09T09:17:50.379490Z",
        "update_at": "2022-07-09T09:17:50.379497Z",
        "user_to": 2,
        "user_from": 1
    },
    {
        "id": 3,
        "verification_code": "420",
        "time_sent": "2022-07-09T15:15:15Z",
        "create_at": "2022-07-09T09:22:48.213024Z",
        "update_at": "2022-07-09T09:22:48.213034Z",
        "user_to": 2,
        "user_from": 1
    }
]
`


## List all institutions: `http://localhost:8000/register/listinstitutions`

Lists all the institutions that this end user registered themselves with.

### Payload

Nothing

### Response

[
    {
        "id": 1,
        "email": "institution1@test.com",
        "display_name": "Institution 1",
        "role": "IN"
    }
]



## Add an institution: `http://localhost:8000/register/addinstitution`

Add an institution to the list of institutions that the end user wishes to receive codes from.

### Payload

`
{
    "institution_id":1
}
`

## Response

"Institution Added successfully."

or 400, I think, double check the code 



# INSTITUTION ENDPOINTS

## Send a code:  `http://localhost:8000/verifier/send`

Send a verification code to an end user.

### Payload

`
{
    "verification_code":"420",
    "time_sent":"2022-07-09T15:15:15",
    "user_to":1
}
`

### Response

400 or 200 I think, check the code to double-check


## List end users: `http://localhost:8000/register/listendusers`

Lists all the end users that are registered with this institution.

### Response

`
[
    {
        "id": 2,
        "email": "user1@test.com",
        "display_name": "User 1",
        "role": "EU"
    }
]
`

