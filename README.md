# Django-DiscordOauth2
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com)

### A web application for Discord Oauth2 with **Django** web framework 
###### And **Jquery**, **Bootstrap** css and JavaScript framework 😐

# About
This project was just to practice in the **Django** framework and challenge me in this framework.

allows you to see your profile and the servers you are in after your authentication in Discord, but according to Discord rules and the services it provides to us. So do not worry about stealing your identity and the servers you are on.

# What is Discord?
[**Discord**](https://discord.com/company) is a voice, video and text communication service used by over a hundred million people to hang out and talk with their friends and communities.

# What is OAuth2?
[**OAuth2**](https://discord.com/developers/docs/topics/oauth2#oauth2) enables application developers to build applications that utilize authentication and data from the Discord API. Within Discord, there are multiple types of OAuth2 authentication. We support the authorization code grant, the implicit grant, client credentials, and some modified special-for-Discord flows for Bots and Webhooks.

# Requirements
  ### Python
  **Python 3.6** or greater
  ### Packages
    asgiref==3.4.1
    pytz==2021.1
    sqlparse==0.4.1
    Django==3.2.6
    python-decouple==3.4
 
 # How to usage
 1. Clone this repo.
 2. Open command prompt inside the folder where you cloned repo and enter this command `pip install -r requirements.txt`.
 3. Create Discord account and login with the browser.
 4. Go to [Discord Developer portal](https://discord.com/developers/applications) and create your own application, click OAuth2 and copy your client ID and client secret.
 5. Then paste them into the .env file.
      
        client_id = Your client id
        client_secret = Your client secret
6. In the same section of Oauth2, click on Add redirect and enter this address for callback.
    `http://127.0.0.1:8000/auth`
    ## tip
    If you want to run this project on a server or host, put your domain instead of 127.0.0.1:8000 and go to the settings.py file in the DiscordOauth2 folder and set DEBUG to       False and put your domain in the ALLOWED_HOSTS list, e.g => `www.mydomain.com` or `mydomain.com`, then change redirect_uri to `http://yourdomain/auth`
    And for static files, serving is the responsibility of the server or host([For more information](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment)).
    
7. Then with the help of OAuth2 URL Generator In Oauth2, by selecting the url you added in Redirects in the SELECT REDIRECT URL section and checking `identify` and `guilds`, the    url generator will give you a url, copy it and paste it in .env file
        
        auth_url_discord = The url you copied
        
8. Enter this command on command prompt `python manage.py runserver`
9. If you encounter an error during Authentication, raise it [here](https://github.com/TShoKT/Django-DiscordOauth2/issues).
    
    But some errors are related to the database, e.g => no such table django_section, so you can delete db.sqlite3 file and run this command on command prompt `python manage.py migrate` 😁

