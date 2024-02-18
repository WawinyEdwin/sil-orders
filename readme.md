
### Installation Guide

- Clone this repository [here](https://github.com/WawinyEdwin/wezacare-challenge.git).
- The `main` branch is the most stable branch at any given time, ensure you're working from it.
- Create a virtual environment on the repo directory, `python3 -m venv venv`
- Run `pip install -r requirements.txt` to install dependencies.
- Once the packages are installed preferably on a virtual env
- Create a file `.env` file at the root directory, copy contents of the `.env.example` into the `.env` file and populate its contents appropriately.
- Run `python3 manage.py migrate` to migrate the database tables.

### Testing

- To run tests on this application.
- Run `python3 manage.py test`

### Coverage

- To run test coverage
- Run `coverage run manage.py test`
- Then `coverage report`

### Usage

- Run `python3 manage.py runserver 8001` to start the application.
- Connect to the API using Postman or web client on port 8001.

### API Authorization
Pass given authorization header for the requests
- Authorization `Token <server_issued_token_for_exchanged_oauth_access_token>`

### API Endpoints

| HTTP Verbs | Endpoints                                     | Action                                      |
|------------|-----------------------------------------------|---------------------------------------------|
| GET       | /api/customers/                               | fetch customers                   |
| POST       | /api/customers/                               | add customer details                    |
| GET       | /api/customers/:customerID/orders/                                  | fetch orders for a given customer            |
| POST       | /api/customers/:customerID/orders/                                  | add a customer order            |
| POST       | /api/register-by-access-token/social/google-oauth2/| Exchange oauth issued token for our server token                  |


---

### API Documentation

Find the API documentation
here [Postman Documentation](https://documenter.getpostman.com/view/17474568/2s93JqSR4c)

### Technologies Used

- [Python](https://nodejs.org/) is a programming language that lets you work more quickly and integrate your systems
  more effectively.
- [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and
  clean, pragmatic design.
- [Django Rest Framework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible
  toolkit for building Web APIs.
- [Google Oauth Plaground](https://developers.google.com/oauthplayground/) Useful for simulating user consent and acquire Google issued access tokens.
- [Africas Talking Python SDK](https://github.com/AfricasTalkingLtd/africastalking-python) Used to communicate to AfricasTalking APIs for messaging.