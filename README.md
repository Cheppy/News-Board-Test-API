[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
#
# News Board Djangro REST >API DEPRICATED<

## About
Simple news board API is created with django rest framework. Project is deployed on [Heroku](http://news-blog-django-yefrem.herokuapp.com/).
Examples of usage:

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
  * To manage or add new commands go to `/managment/commands` in the application folder.
  * It is possible to schedule some commands as a cronjob. to do so, add them in `cron.py` script that is located in application folder.
  
  To show current active jobs of this project use:

   ```
   python manage.py crontab show
   ```
   To add new command, add it to the CRONJOBS list in `settings.py` as shown in example below:
   ```
   CRONJOBS = [
    ('58 23 * * *', 'news_board.cron.clean_upvotes_job'),
     ('* 10 * * *', 'django.core.management.call_command', ['clearsessions']),
    ]
   ```
   To add all defined jobs from CRONJOBS to crontab run this command:
   ```
      python manage.py crontab add
   ```
   
   
 ## Licenses
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


  
