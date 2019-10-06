# Dell Hackathon

## Setup

_Note:_ install `pipenv` from `pypi.org`.

```bash
# Install all the dependencies
$ pipenv install
```

## Usage

Few commands have been created to ease the development process.

```bash
# To run the development server
$ pipenv run start

# To create a new app
$ pipenv run create-app <app_name>

# To make migrations
$ pipenv run make-migrations [app_name]

# To migrate
$ pipenv run migrate
```
