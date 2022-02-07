# Project

* This repository contains the companion project for creating RESTful API through flask module and mysql with Python. 

## Prerequisite
* firstly, you should create your tables on database through certain sql statemnets:
```
  use mydb;
CREATE TABLE customer
(
  id int2 NOT NULL,
  name varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  phone varchar(16) DEFAULT NULL,
  address text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE customer
  ADD PRIMARY KEY (id);
  
ALTER TABLE customer
 MODIFY id int2 NOT NULL AUTO_INCREMENT;
```
## Installation

* you can download  all the required modules or libraries to run the application from this command line:
  
```
pip install -r REST_API_MYSQL/requirements.txt

```

## Running locally

* To run the application ,Navigate to the directory.

```
python main.py
```


















