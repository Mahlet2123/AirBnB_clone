# 0x05. AirBnB clone - RESTful API
By: Guillaume, CTO at Holberton School
Weight: 2
 
Project to be done in teams of 2 people

## General
- What REST means
- What API means
- What CORS means
- What is an API
- What is a REST API
- What are other type of APIs
- Which is the HTTP method to retrieve resource(s)
- Which is the HTTP method to create a resource
- Which is the HTTP method to update resource
- Which is the HTTP method to delete resource

Install Flask

    $ pip3 install Flask

Tasks
0. Restart from scratch!
mandatory
Score: 100.0% (Checks completed: 100.0%)
No no no! We are already too far in the project to restart everything.

But once again, let’s work on a new codebase.

For this project you will fork this codebase:

Update the repository name to AirBnB_clone_v3
Update the README.md:
Add yourself as an author of the project
Add new information about your new contribution
Make it better!
If you’re the owner of this codebase, create a new repository called AirBnB_clone_v3 and copy over all files from AirBnB_clone_v2
Repo:

GitHub repository: AirBnB_clone_v3
   
1. Never fail!
mandatory
Score: 53.85% (Checks completed: 53.85%)


Since the beginning we’ve been using the unittest module, but do you know why unittests are so important? Because when you add a new feature, you refactor a piece of code, etc… you want to be sure you didn’t break anything.

At Holberton, we have a lot of tests, and they all pass! Just for the Intranet itself, there are:

5,213 assertions (as of 08/20/2018)
13,061 assertions (as of 01/25/2021)
The following requirements must be met for your project:

all current tests must pass (don’t delete them…)
add new tests as much as you can (tests are mandatory for some tasks)

    guillaume@ubuntu:~/AirBnB_v3$ python3 -m unittest discover tests 2>&1 | tail -1
    OK
    guillaume@ubuntu:~/AirBnB_v3$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
    OK
    guillaume@ubuntu:~/AirBnB_v3$ 


