# Recruiterbox

> A Portal to appreciate your colleges by giving them kudos.

## Pre-Requisites

This project uses [Python3](https://www.python.org/), [node.js](https://nodejs.org/en/), [pipenv](https://pipenv.readthedocs.io/en/latest/) and [npm](https://www.npmjs.com/) thus you need to have them install in your system.

**Clone this repository**

## Development Server
- Change your directory to `server`
  ```sh
  $ cd server
  ```

- To activate the virtual environment
  ```sh
  $ pipenv shell
  ```

- To install packages
  ```sh
  $ pipenv install --dev --pre
  ```

- Now make migrations and migrate the db.
  ```
  $ ./manage.py makemigrations
  $ ./manage.py migrate
  ```

- Create superuser
  ```
  $ ./manage.py createsuperuser
  ```

- Collect static files
  ```
  $ ./manage.py collectstatic
  ```

- Start the development server  
  ```
  $ ./manage.py runserver
  ```

- To run tests
  ```
  $ pytest -v
  ```

- To run linting
  ```
  $ flake8 .
  ```

- To load fake data
  ```
  $ ./manage.py load_fake_data -orgs 2 --users 5 --kudos 100
  ```

## Development client

- Change your directory to `client`
  ```sh
  $ cd client
  ```

- To install dependencies
  ```
  $ npm install
  ```

- To compiles and hot-reloads for development
  ```
  $ npm run serve
  ```

- To compiles and minifies for production
  ```
  $ npm run build
  ```

- To run tests
  ```
  $ npm run test:unit # For unit tests
  $ npm run test:e2e  # For e2e tests
  ```

- To run linting
  ```
  $ npm run lint
  ```

## Built With

- [Python3](https://www.python.org/) - Programming language
- [node.js](https://nodejs.org/en/) - Programming language
- [pipenv](https://pipenv.readthedocs.io/en/latest/) - Python Dev Workflow for Humans
- [npm](https://www.npmjs.com/) - package manager for the JS programming language
- [django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [Django REST framework](https://www.django-rest-framework.org/) - a powerful and flexible toolkit for building Web APIs
- [vue.js](https://vuejs.org/) - The Progressive JavaScript Framework

## Authors

- **Ratan Kulshreshtha**- <ratan.shreshtha@gmail.com>

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- Stack Overflow
- etc
