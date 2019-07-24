# sinopac_demo

POST user 
#### url: http://127.0.0.1:8000/users/
#### json format
input 
```
{
    "password": "passwd",
    "username": "admin",
    "email": "admin@mail.com",
    "phone": "0912345678",
    "gender": "f",
    "age": 18,
    "groups": [],
    "user_permissions": []
}
```

output
```
{
    "id": 1,
    "username": "admin",
    "email": "admin@mail.com",
    "phone": "0912345678",
    "age": 18,
    "last_login": null,
    "gender": "f"
}
```
