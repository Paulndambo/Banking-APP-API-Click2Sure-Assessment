# How to run the Project

# Note
The Project Has The Two Parts:
    1. The API which you will run normally as a django project
    2. The Test Suite which is a small NodeJs application which contains the API testing Automation Scripts

#Remember the endpoints are protected so obtain authentication/authorization tokens
#Token generation instructions are also stated in this document

# clone the project from github
git clone https://github.com/Paulndambo/Banking-APP-API-Click2Sure-Assessment.git
cd into Banking-APP-API-Click2Sure-Assessment

# Install Dependencies
pip install -r requirements.txt

# Create SuperUser
#Run the command below on your terminal/cmd
python manage.py createsuperuser

#Run the server by running this command on terminal
python manage.py runserver


# Go to API Documentation
#Open this ip on your browser http://127.0.0.1:8000

The API Documentation will allow you:
    1. Try the APIs on the browser
    2. Provide you will curl commands to test the API on your terminal

# Generate User Tokens
On the API documentation you will see Auth which is where you will find the auth urls
