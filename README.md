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


