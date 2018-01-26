Complete source code for [Django Rest Framework Tutorial](https://wsvincent.com/django-rest-framework-tutorial/) which implements basic CRUD functionality in a blog API.

## Local Setup

```
$ git clone  https://github.com/wsvincent/django-rest-framework-tutorial.git
$ cd django-rest-framework-tutorial
$ pipenv install
$ pipenv shell
(api) $ ./manage.py runserver
```

Navigate to the list view at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) and detail view at [http://127.0.0.1:8000/api/1](http://127.0.0.1:8000/api/1).

![Blog list view](screenshots/blog-list.png)

![Blog detail view](screenshots/blog-crud.png)
