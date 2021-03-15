# Getting started

```shell script
git clone git@github.com:almn/django-pages-api.git
```

### Run tests

```shell script
docker-compose up autotets
```

should give something like
```shell script
...
Run autotests
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.209s

OK
Destroying test database for alias 'default'...
```

### Start services

```shell script
docker-compose up runserver
```

#### Request pages list

```shell script
curl --location --request GET 'http://127.0.0.1:8000/pages/'
```

or, for page 2

```shell script
curl --location --request GET 'http://127.0.0.1:8000/pages/?page=2'
```


Answer should looks like

```json
{
    "count": 13,
    "next": "http://127.0.0.1:8000/pages/?page=2",
    "previous": null,
    "results": [
        {
            "title": "Page 1",
            "url": "http://127.0.0.1:8000/pages/1/"
        },
        {
            "title": "Page 10",
            "url": "http://127.0.0.1:8000/pages/11/"
        },
        {
            "title": "Page 11",
            "url": "http://127.0.0.1:8000/pages/12/"
        },
        {
            "title": "Page 12",
            "url": "http://127.0.0.1:8000/pages/13/"
        },
        {
            "title": "Page 2",
            "url": "http://127.0.0.1:8000/pages/2/"
        },
        {
            "title": "Page 3",
            "url": "http://127.0.0.1:8000/pages/3/"
        },
        {
            "title": "Page 4",
            "url": "http://127.0.0.1:8000/pages/4/"
        },
        {
            "title": "Page 5",
            "url": "http://127.0.0.1:8000/pages/5/"
        },
        {
            "title": "Page 6",
            "url": "http://127.0.0.1:8000/pages/6/"
        },
        {
            "title": "Page 7",
            "url": "http://127.0.0.1:8000/pages/8/"
        }
    ]
}
```

#### Request page details:

```shell script
curl --location --request GET 'http://127.0.0.1:8000/pages/1/'
```

Response should looks like:

```json
{
    "title": "Page 1",
    "items": [
        {
            "title": "audio 2",
            "bitrate": 200,
            "counter": 2
        },
        {
            "title": "text 2",
            "content": "text 2 sample",
            "counter": 1
        },
        {
            "title": "audio 5",
            "bitrate": 500,
            "counter": 1
        }
    ]
}
```

Of course, all these request may be made by browser.


## Admin page

http://127.0.0.1:8000/admin/

Default admin credentials are

admin:admin