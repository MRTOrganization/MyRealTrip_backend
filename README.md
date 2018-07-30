# My Real Trip

## Requirements

- Python (3.6)
- Django (2.x)

### Secrests

#### `.secrets/base.json`

```json
{
  "SECRET_KEY": "<Django secret key>"
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