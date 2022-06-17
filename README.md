## Prommies

### 13/06/2022

## Author

[Ninah Odoyo]

# Description
Prommies is a webpage where a user can upload their projects,get to see other peoples project and rate the projects according to their own liking.


## Live link


## User Story
The user should be able to:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

* 
## Setup and Installation

##### Clone the repository
```bash
https://github.com/odoyoninah/prommies.git
```
##### Install requirements 
``bash
cd Prommies pip install -r requirements.txt
```
### Install and activate virtual environment
```bash
python3 -m venv virtual - source virtual/bin/activate
```
 ##### Database  
  SetUp your database. Add user and password, host then make migrations. 
 ```bash 
python manage.py makemigrations prommiesapp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 