# Inspectorio Project

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
