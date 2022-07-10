Backend code for the running of Autentida app.

# API Reference

## Login: `http://localhost:8000/auth/jwt/login`

Logs a user in with their email and password. Returns refresh and access tokens along with the user role and 

### Sample Payload

```
{
    "email":"test@test.com",
    "password":"test1234!"
}
```

### Sample Response

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NzUwODQwMywianRpIjoiN2EzNTdlYjllYTZhNDljNmFjOGRiNzUwZDU2MjMzNzIiLCJ1c2VyX2lkIjoyfQ.J_NhSYnh9Nd0vwK4xf3mUmh5FyY8jcwtPzG1MORcHh8",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NDIyMzAzLCJqdGkiOiI3MGQ3NWE5NDI0ZTM0NDkzODQ4ODVlNjBhMGJlNDhiOSIsInVzZXJfaWQiOjJ9.yeFlMs2hb1hGME7guYnxream_Ds1Gzp11_ZmMFiKEWQ",
    "role": "EU",
    "id": 2
}
```


## Signup:  `http://localhost:8000/auth/register`

Signs a new user up using their credentials. Specify role as either 'IN' (for an institution), or 'EU' (for an end user).

### Sample Payload

```
{
    "email":"test@test.com",
    "display_name": "OCBC Bank",
    "password":"test1234!",
    "role":"IN"
}
```

### Sample Response

```
{
    "id": 3,
    "email": "test@test.com",
    "display_name": "OCBC Bank",
    "role": "IN",
    "created_at": "2022-07-09T08:59:22.259095Z"
}
```

# API Endpoints for End Users

## List all Verification Codes as an End User:  `http://localhost:8000/verifier`

Lists all the codes sent from institutions to a particular user. 

Each entry consists of the verification code sent by the institution, a timestamp which represents the time when the SMS/Email notification was supposedly sent, and the display name of the institution which the code originated from.

### Sample Payload

Nothing. User identity is determined based on the JSON Web Token which is sent to the backend.

### Sample Response

```
[
    {
        "id": 2,
        "verification_code": "660",
        "time_sent": "2022-07-09T15:15:15Z",
        "create_at": "2022-07-09T09:17:50.379490Z",
        "update_at": "2022-07-09T09:17:50.379497Z",
        "user_to": 2,
        "user_from": "OCBC Bank"
    },
    {
        "id": 3,
        "verification_code": "12454",
        "time_sent": "2022-07-09T15:15:15Z",
        "create_at": "2022-07-09T09:22:48.213024Z",
        "update_at": "2022-07-09T09:22:48.213034Z",
        "user_to": 2,
        "user_from": "OCBC Bank"
    }
]
```


## List all institutions: `http://localhost:8000/register/listallinstitutions`

Lists all the institutions that exist in the system, which the user can choose to register themselves with.

### Sample Payload

Nothing.

### Sample Response

```
[
    {
        "id": 1,
        "email": "institution1@test.com",
        "display_name": "Institution 1",
        "role": "IN"
    },
    {
        "id": 2,
        "email": "institution1@test.com",
        "display_name": "Institution 2",
        "role": "IN"
    }
]
```


## List my institutions: `http://localhost:8000/register/listmyinstitutions`

Lists all the institutions which the given user is currently registered with.

### Sample Payload

Nothing. User identity is determined by JSON Web Token.

### Sample Response

```
[
    {
        "id": 1,
        "email": "institution1@test.com",
        "display_name": "Institution 1",
        "role": "IN"
    }
]
```


## Add an institution: `http://localhost:8000/register/addinstitution`

Add an institution to the list of institutions that the end user wishes to receive codes from.

### Sample Payload

```
{
    "institution_id":1
}
```

## Response Codes

`HTTP_200`: Institution Added Successfully.

`HTTP_400`: Institution ID is specified in the wrong format or is absent.

`HTTP_404`: Institution with that ID is not found.


## Remove an institution: `http://localhost:8000/register/deleteinstitution`

Remove an institution to the list of institutions that the end user wishes to receive codes from.

### Sample Payload

```
{
    "institution_id":1
}
```

## Response Codes

`HTTP_200`: Institution Removed Successfully.

`HTTP_400`: Institution ID is specified in the wrong format or is absent.

`HTTP_404`: Institution with that ID is not found.


# API Endpoints for Institutions

## Send a code:  `http://localhost:8000/verifier/send`

Send a verification code to an end user.

User Identity is determined by JSON Web Token. Verification Code is generated on the side of the Institution, and the Time Sent will be based on the time that the institution sends their SMS/Email. User_to will be the user_id of the end user which the institution wants to send the verification code to.

### Sample Payload

```
{
    "verification_code":"28",
    "time_sent":"2022-07-09T15:15:15",
    "user_to":1
}
```

### Response Codes

`HTTP_400`: Bad request - request did not match correct format
`HTTP_200`: Code sent successfully.


## List end users: `http://localhost:8000/register/listendusers`

Lists all the end users that are registered with this institution.

### Payload

None. Institution Identity is based on their JSON Web Token.

### Sample Response

```
[
    {
        "id": 2,
        "email": "user1@test.com",
        "display_name": "User 1",
        "role": "EU"
    }
]
```

