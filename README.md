# APIs documentation:

Valid requests/responses:

1. endpoint: http://127.0.0.1:8000/users/login/
request:
{
    "username": "username",
    "password": "password"
}
response:
{
    "username": "abyl",
    "password": "abyl"
}

2. endpoint: http://127.0.0.1:8000/users/register/
# TODO: Dastan

3. endpoint: http://127.0.0.1:8000/users/logout/
request:
{
    "username": "username"
}
response:
{
    "status": "User is logged out.",
    "username": "abyl"
}

4. endpoint: http://127.0.0.1:8000/users/get_appointments/
request:
{
    "username": "abyl"
}
response:
[
    {
        "topic": "awdawd",
        "subject": "awdaw",
        "description": "awdawd",
        "date": "2022-03-25",
        "time": "21:45:53",
        "offline_mode": true,
        "meeting_link": "awdawd",
        "host_username": "abyl",
        "place_id_field": 1,
        "place": {
            "name": "NU",
            "info_link": "nu.edu.kz",
            "verified": true,
            "lat": 10.0,
            "lng": 10.0
        },
        "users": [
            "abyl",
            "miko"
        ],
        "host": {
            "username": "abyl"
        }
    }
]

5. endpoint: http://127.0.0.1:8000/users/get_appointments_number/
request:
{
    "username": "abyl"
}
response:
1

6. endpoint: http://127.0.0.1:8000/appointments/create/
request:
{
    "topic": "",
    "subject": "",
    "description": "",
    "date": null,
    "time": null,
    "offline_mode": false,
    "meeting_link": "",
    "host_username": "",
    "place_id_field": null
}
response:
{
    "topic": "topic",
    "subject": "subject",
    "description": "description",
    "date": "0001-01-01",
    "time": "01:01:00",
    "offline_mode": true,
    "meeting_link": "aaa",
    "host_username": "abyl",
    "place_id_field": 1
}

7. endpoint: http://127.0.0.1:8000/appointments/join/
request:
{
    "username": "",
    "appointment_id": null
}
response:
{
    "username": "abyl",
    "appointment_id": "1"
}

8. endpoint: http://127.0.0.1:8000/appointments/get_filtered/
request:
{
    "subject": "",
    "topic": ""
}
response:
[
    {
        "topic": "topic",
        "subject": "subject",
        "description": "description",
        "date": "0001-01-01",
        "time": "01:01:00",
        "offline_mode": true,
        "meeting_link": "aaa",
        "host_username": "abyl",
        "place_id_field": 1,
        "place": {
            "name": "NU",
            "info_link": "nu.edu.kz",
            "verified": true,
            "lat": 10.0,
            "lng": 10.0
        },
        "users": [],
        "host": {
            "username": "abyl"
        }
    }
]
