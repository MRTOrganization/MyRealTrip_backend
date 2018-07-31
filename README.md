# My Real Trip

## Requirements

- Python (3.6)
- Django (2.x)

### Secrets

#### `.secrets/base.json`

```json
{
  "SECRET_KEY": "<Django secret key>"
}
```

#### `.secrets/dev.json`

- PostgreSQL을 사용, DATABASES섹션의 설정 필요

```json
{
  "DATABASE": {
    "default": {
      "ENGINE" : "django.db.backend.postgresql",
      "HOST" : "<host>",
      "PORT" : 5432,
      "USER" : "<user>",
      "PASSWORD": "<password>",
      "NAME": "<db name>"
    }
  }
}
```

## Installation

```
pipenv install
```

## Running
```
# Move to project directory
$ pipenv install
$ pipenv shell
$ cd app
$ export DJANGO_SETTINGS_MODULE=config.settings.local
$ ./manage.py runserver
```