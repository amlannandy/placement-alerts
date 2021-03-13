# Placement Alerts

This is a web application made using Flask and PostgreSQL. It consists of a web scraper which scrapes data of the College website's placement notice every 24 hours, and if it finds a new notice up, it sends it as an email to all its subscribers.

You can subscribe to the service <a href="https://placement-alerts.herokuapp.com/">here</a>

## Technology Stack

1. Flask - Core framework used to build the App
2. PostgreSQL - Serves as the database
3. BeautifulSoup - Used to scrape data off the college website
4. Sendinblue API - To send emails to the subscribers

## Local Development Setup

Follow these steps to get the project running on your local machine.

**1. Fork and clone the repository.**

**2. Open terminal in the project directory.**

**3. Create a virtual environment using the following command**

```
virtualenv venv
```

**4. Activate the newly created virtual environment by using the following command**

For Linux/Mac
```
source venv/bin/activate
```

For Windows (Using Git Bash)
```
source venv/Scripts/activate
```

**5. Create a .env file and add the following values to it**

```
DATABASE_URL=<postgresql-database-uri>
MAIL_PORT=587
MAIL_SERVER=smtp-relay.sendinblue.com
MAIL_USERNAME=<your-sendinblue-email>
MAIL_PASSWORD=<your-sendinblue-account-api-password>
MAIL_DEFAULT_SENDER=<you-email-address>
ADMIN_PASSWORD=<password-of-your-choice>
```

Note - Instead of PostgreSQL, you can also use Flask's inbuilt SQLite database. In that case, set Database URI to

```
DATABASE_URL=sqlite:///db.sqlite3
```

**6. Create the tables by running this command**

```
python create_database.py
```

**7. Run the Application**

```
flask run
```

## Screenshots

<img src="https://user-images.githubusercontent.com/45410599/111032686-79682900-8433-11eb-8460-aee1ba710039.png" >

<div style="flex-direction: row margin-top: 10px;">
  <img src="https://user-images.githubusercontent.com/45410599/111032200-0f4e8480-8431-11eb-9e93-b3e50eb255a3.png" width="250px" style="margin-right: 10px;" alt="">
  <img src="https://user-images.githubusercontent.com/45410599/111032205-107fb180-8431-11eb-92aa-e7d88ced1ba2.png" width="250px" style="margin-right: 10px;" alt="">
</div>

