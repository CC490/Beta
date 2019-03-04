# 
### Project CLCDb:
#
   This is a Web Application for the Challenger Learning Center of Richland One,
which will provide a Visitor Information and Scheduling Database, coupled with a technically
and aesthetically approachable cloud-based user interface. This Application is intended
for utilization by the Staff of the CLC, with the core functionalities of adding,
reviewing, revising, and deleting Event reservations in a simple, streamlined environment.
Further central features of the CLCDb project will be maintenance of records regarding the 
volume of Events over a given time period, and relevant information regarding Visitor habits (such 
as attendance at reserved events and timeliness of payments). The primary focus of this project is
ensuring intuitive user interface with the database via Webpages intentionally designed to remain 
visually accommodating, even throughout extended periods of use.



## Necessary Packages:

[Python for Windows](https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe)

[CLCDb Master WebApp Package](https://github.com/SCCapstone/CLCDb.git) 

[Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/?v=a)


## ** NOTE: **
   
   - Depending on your individual machine's settings, you may need 
         to prefix your commands with the keyword 'python3' or 'py -3';
         additionally, this Application has been developed primarily for
         use on Windows machines. It is possible that the file path or
         the PATH environment variable on a Linux/mac machine may not be 
         formatted properly, especially for behavioural testing. If the
         behavioural test does not succeed, please copy the geckodriver.exe
         from the "./CLCDb/" folder into the environment path.
         

## Installing Project for Testing and Demonstration:


- Download Python from the link above, and add to PATH:

   - edit "Path" environment variable to include 
      "pathto/python/python37" 
      as well as 
      "pathto/python/python37/Scripts" 

- clone CLCDb repository to Windows machine
   - 'git clone https://github.com/SCCapstone/CLCDb.git'
      - (need github username and password)
- navigate into the "./CLCDb/" directory inside 
      a terminal opened with Adminstrator privileges
- execute the following shell commands:
   - git fetch
   - git checkout master
   - pip3 install pipenv
   - pipenv shell
   - pipenv sync
   - pipenv install --dev
   - git add .
   - git commit -m "saving environment state."
   - manage.py <command>
      - eg: manage.py runserver
   - exit
      

- It is possible it could help to run:

   - pipenv install virtualenvwrapper-win
      immediately before running 'pipenv install --dev',
      but in my testing it has not seemed necessary.

      *****also, it looks like this wrapper only works on windows,
      it is currently in the Pipfile but maybe shouldn't be.


### Once Environment is Installed:
-----------------------------------

## Run Project on LocalHost:
- navigate into the "./CLCDb/" directory inside 
      terminal with Adminstrator privileges.
- execute the following shell commands:
   - 'pipenv shell'
   - 'manage.py runserver'
- In Web Browser, navigate to LocalHost IP and Port:
      - http://127.0.0.1:8000
- Login information for testing (case sensitive):
      - username: admin490
      - password: Sup3rP@s$wOrd



## Alternatively, visit the deployed website (not currently available):
- Navigate to http://denv.zrmwfbvv9m.us-east-2.elasticbeanstalk.com/accounts/login/
- Login information for testing (case sensitive):
      - username: admin490
      - password: Sup3rP@s$wOrd



## Deployment:
We will be using AWS Elastic Beanstalk for deployment.



## Unit Testing:

- Navigate to "./CLCDb/" in two seperate Administrator terminals.
- execute the following commands:
   - 'pipenv shell'
   - 'manage.py runserver'
   - 'manage.py test <app_directory_name>'
   
      - example: 'manage.py test reservation'

   - unit tests will run and output 'OK' given success.

- Currently only "./CLCDb/reservation/" includes unit testing; other
      application directories will have unit tests developed as they
      themselves continue to be developed.


## Behavioural Testing:

- Install Mozilla Firefox on machine.

- Navigate to "./CLCDb/" in two seperate Administrator terminals.

- execute the following commands:
   
   - terminal_A & terminal_B:
      'pipenv shell'
   
   - terminal_A:
      'manage.py runserver'

   - terminal_B:
      'manage.py test tests'

- If test fails due to Firefox driver not in Path:
   - create/open file '.env'
   - type: "PATH"+=".\geckodriver.exe"
   - save and quit
   - repeat test commands

- *** It is necessary to activate the pipenv shell for behavioural testing, 
         as doing so adds the geckodriver.exe to PATH, allowing Selenium to 
         automate the tests within the Mozilla Firefox Browser.



## Style Guide:

[Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)



## Development Sources:

[Pipenv](https://pipenv.readthedocs.io/en/latest/) 

[Django](https://www.djangoproject.com/download/) 



## Authors
- Maya Stelzer
- Benjamin King
- William Bradham
- Chao Chen
