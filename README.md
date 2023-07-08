# NitWork

>  An API where user and company can register/login and get a Token that allow them to make comments

Additional description about the project and its features.


## Built With

- DJANGO
- DJANGO REST FRAMEWORK
- Django Rest Knox
- GITHUB ACTIONS
- VSCODE

## Getting Started
### Usage
To have this app on your pc, you need to:
* [download](https://github.com/pariyajebreili/NitWork/archive/refs/heads/main.zip) or clone this repo:
  - Clone with SSH:
  ```
    git@github.com:pariyajebreili/NitWork.git
  ```
  - Clone with HTTPS
  ```
    https://github.com/pariyajebreili/NitWork.git
  ```

* In the project directory, you can run:

Create virtual enviroment 

Run migrations:

``` bash
   py manage.py migrate
```
Run server:

``` bash
   py manage.py runserver
```

Endpoints:
``` bash
    http://127.0.0.1:8000/account/ signup/student/
    http://127.0.0.1:8000/account/ signup/company/
    http://127.0.0.1:8000/account/ login/
    http://127.0.0.1:8000/account/ logout/ [name='logout']
    http://127.0.0.1:8000/account/ logoutall/ [name='logoutall']
    http://127.0.0.1:8000/account/ comapny/dashbord/
    http://127.0.0.1:8000/account/ student/dashboard/
    http://127.0.0.1:8000/account/ student_update/
    http://127.0.0.1:8000/account/ company_update/
    http://127.0.0.1:8000/account/ companies/ [name='company-list']
    http://127.0.0.1:8000/account/ company_detail/<str:identifier>/ [name='company_detail']
    http://127.0.0.1:8000/comment/ send_comment/<int:id_company>/ [name='send_comment']
    http://127.0.0.1:8000/comment/ show_comment/<int:id_company>/ [name='show_comment']
```

## Acknowledgments 🚀

- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework Docs](https://www.django-rest-framework.org/)
- [Django-Rest-Knox](https://james1345.github.io/django-rest-knox/)


## 📝 License

This project is [MIT](lic.url) licensed.
