# API Test

### 1. Overview
- The purpose of this project is to build simple REST API service connected with a PostgreSQL database named `L` in which an user could perform `GET` & `POST` requests to retrieve or insert new data into `L`.
- The REST API service, which is developed upon Django REST, PostgreSQL & PgAdmin, is containerised by using `docker` and `docker-compose`.


### 2. How to run
- Download this folder to your local machine.
- Then run the following
```
docker-compose build && docker-compose up -d
```

### 3. What to expect
#### 3.1. Data Models
- There are three models as follows
![alt text](https://github.com/dukele35/inspectorio-test/blob/main/images/data-model.jpg)
- `factory`:
    - `factory_id` (primary key): a unique identifier chosen randomly between from 10,000 to 99,999.
    - `factory_name`: a character describing a factory's name.
- `org`:
    - `org_id` (primary key): a unique identifier chosen randomly between from 1,000 to 9,999.
    - `org_name`: a character describing an organisation's name.
- `item`:
    - `id` (primary key): a unique identifier starting from 1.
    - `factory_id` (foreign key): a unique identifier chosen randomly between from 10,000 to 99,999.
    - `org_id` (foreign key): a unique identifier chosen randomly between from 1,000 to 9,999.
    - `country`: a two-digit character describing a country with 5 available choices including "VN" (Vietnam), "MY" (Malaysia), "PH" (Philippines), "SG (Singapore), "TH" (Thailand).
    - `fail_rate`: a float between 0 and 1.
    - `defect_rate`: a float between 0 and 1.
#### 3.2. REST API
- http://localhost/ shows the default Django REST's API Root page which includes http://localhost/item/, http://localhost/org/ & http://localhost/factory/
- http://localhost/api/ reveals the Swagger API doc instructing us how to perform `GET`, `POST`, `PUT`, `PATCH` & `DELETE` requests on different data models, i.e. `item`, `org` & `factory`.
- All endpoints are publicly available since there is no authentication method applied. Thus, using `curl` could be simply performed.
- It is recommended that one should create new entries, i.e. `POST` request, for both `org` and `factory` first before creating new entries or retrieving data from `item`. It is because `item` is depedent on and having many-to-one relationships with `org` and `factory`.
#### 3.3. PgAdmin & PostgreSQL
- After creating new entries in `org`, `factory` & `item`, you could access the PostgreSQL database `L` with PgAdmin via http://localhost:5050/. Please refer to the credentials given seperately from this repo to access PgAdmin. Also, to connect the database after logging in, please refer to the given credentials.
#### 3.4. CICD pipeline
- [Github Actions](https://github.com/dukele35/inspectorio-test/actions) notifies and safeguards this project from vulnerabilities associated with poor coding practices with `flake8`, security issues with `bandit`, unit testing as well as coverage report.
- This is an [example](https://github.com/dukele35/inspectorio-test/actions/runs/2942717582) of the CICD pipeline featuring code testing & building docker images. From here, one could check the following:
    - `flake8 checking & report` and `bandit checking & report` ([link](https://github.com/dukele35/inspectorio-test/runs/8057037825?check_suite_focus=true)). Please click into those sections to have more information.
    - `unit tests` and `coverage report` ([link](https://github.com/dukele35/inspectorio-test/runs/8057039403?check_suite_focus=true)). Please click into those sections to have more information.
#### 3.5. Pre-commit hooks
- Pre-commit helps to check and possibly reformat this repo's code in terms of code styles, security issues, etc. before pushing onto Github. This repo uses `black` hook, `flake8` hook and default `pre-commit` hooks in this [file](https://github.com/dukele35/inspectorio-test/blob/main/.pre-commit-config.yaml).
- Instructions of how to use pre-commit hooks could be found [here](https://pre-commit.com/).

### 4. How to stop
- Run the following
```
docker-compose down
```
