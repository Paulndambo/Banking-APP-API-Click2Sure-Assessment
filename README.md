# How to run the Project

# Note
The Project Has The Two Parts:
#1.The API which you will run normally as a django project
#2. The Test Suite which is a small NodeJs application which contains the API testing Automation Scripts

#Remember the endpoints are protected so obtain authentication/authorization tokens
#Token generation instructions are also stated in this document

# Usage Disclaimer
#Incase you face authorization difficulties while trying to test the endpoints on the Docs, Just use your postman or any other application you have been using to test APIs 
#You can choose to run the project inside a virtual environment or not

#Incase you want to run the project inside a virtual environment
# Create Virtual Environment - Optional
#Windows, run the commands below
#python -m venv click2sureassessmentenv
#click2sureassessmentenv/Scripts/activate

#Linux
#python3 -m venv click2sureassessmentenv
#source click2sureassessmentenv/bin/activate

# clone the project from github
#git clone https://github.com/Paulndambo/Banking-APP-API-Click2Sure-Assessment.git
#cd into Banking-APP-API-Click2Sure-Assessment

# Install Dependencies
#pip install -r requirements.txt

# Create SuperUser
#Run the command below on your terminal/cmd
#python manage.py createsuperuser

#Run the server by running this command on terminal
#python manage.py runserver


# Go to API Documentation
#Open this ip on your browser http://127.0.0.1:8000

#The API Documentation will allow you:
#1. Try the APIs on the browser
#2. Provide you will curl commands to test the API on your terminal

# Generate User Tokens
#On the API documentation you will see Auth which is where you will find the auth urls
#To Create A User Account use this endpoint
#http://127.0.0.1:8000/api/auth/register/

#To Generate Auth Token
#http://127.0.0.1:8000/api/auth/token/

#To Get All Users
#http://127.0.0.1:8000/api/auth/users/

# Running The Test Suite
#The testsuite is a simple NodeJs project inside this project which will run an automated API testing for you
#Make sure you keep the project server running as you run the APIs test scripts

#Steps
#Open the project folder in another terminal window
#while inside the project folder change directory to testsuite
#cd testsuite
#Then run this command => npm install or you can also run => yarn install
#The above command will install the required node modules and if successful you are good to go
#To run the scripts type the command below on your terminal
#npm run test

# Download CSV Reports
#User the superuser account you created to login to the admin dashboard
#While on the Admin Dashbord you will see Accounts and Bank Transactions
#You Can Download a CSV for each from there 
#Admin url => http://127.0.0.1:8000/admin