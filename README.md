# AvocaTo
Forum in form of FAQ for every kind of questions

### Purpose
The purpose of this project is to create the web application forum called Avoca.To

This web application provide the simple way of exchanging the knowledge and information between the people. Every person can ask any kind of question that is interested for him and every user of the application will be able to answer him. The questions could be rated by other users and also by the author of the question.
All of the site visitors will be able to see the question and the answers but only the authorized users will be able to create the question or answer them.

## Getting Started
This guide walks you through to start the AvocaTo application.

#### Installation

* Clone this repository or download the version package

* Go to project directory and install requirements for development
```
cd AvocaTo && pipenv install --dev && pipenv shell
```

* Create .env and fill with your environment variables configuration file from example config
```
cp config/.env.example config/.env
```
 
* Run the migration to set up the database
```
./manage.py migrate
```

#### Run the application

Run development server:

```
./manage.py runserver
```

## System dependencies

Python: *v3.8*

PostgreSQL: *v11*


### License
This project is licensed under the GNU General Public License
