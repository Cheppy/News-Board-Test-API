[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# News Board Djangro REST API

## About
Simple news board API is created with django rest framework. Project is deployed on [Heroku](http://news-blog-django-yefrem.herokuapp.com/).

   * Here you can find acces to [Articles](http://news-blog-django-yefrem.herokuapp.com/api/articles).
   
   * Here you can find acces to [Comments](http://news-blog-django-yefrem.herokuapp.com/api/comments).
   
 Detailed  API usages and documantion are available as postman collection  : [News board Collection](https://www.getpostman.com/collections/70aa9c511b554c325246).
## Get started
 It is possible to run this application in docker. To do so be sure you have `docker-compose` installed.
 To get the application running. Mac and Windows users can [install Docker Desktop](https://docs.docker.com/docker-for-mac/install/) that includes Compose along with other Docker apps ( [Link for Windows](https://docs.docker.com/docker-for-windows/install/))
 <br>With `docker compose` already installed run following command from the project root directory:<br/>
                             
  ```
  docker-compose up
  ```

 It is also possible to start project by running it like a simple Django application. For this, first, you need to install all required modules to  your virtualenv:
 ```
 pip install -r requirements.txt
 ```
 And run the django server:
 ```
 python manage.py runserver
 ```
 ## Featuers
  It is possible to schedule some commands as a cronjob, or even execute them manualy. Commands can be found in `Django_News_board/news_board/management/commands`
  
 ## Licenses
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


  
  
