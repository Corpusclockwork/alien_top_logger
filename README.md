# Welcome to Alien Bloc's (unofficial) verison of TopLogger ! 
This is a personal project where I created a site that customers at Alien Bloc (the local climbing gym that I work at) could hypothetically track the routes that they climb. 

## Functionality
**Staff User funtionality:**

* Create new routes at a particular location on the map 
* Delete old routes

**Customer functionality:**

* Track routes that they send
* See which routes they have sent
  
**Shared functionality**
  
* Can filter routes by hold colour and V grade range 
* Can see route locations on the map when they select the routes from the route list

## Project structuring

This project was created using Javascript with Vue, Python with Django, and a MySQL database. I used DigitalOcean for deployment, along with apache2. Certbot was used for SSL verification. 

## Use
 Go to https://alienroutelogger.com/. I've created a set of users called 'CustomerUser1' all the way to 'CustomerUser5' and another set of users for staff;'StaffUser1' to 'StaffUser5'. The passwords for these users are the same as their usernames. To login, create a customer user, or login as one of my premade customer users. Or, alternatively, create a staff user (by clicking the little checkbox in the top right of the create user screen), or log in as one of my premade staff users.

## Running locally
If you want to run this locally, 
1. `git clone` my repo
2. Install MySQL
3. `sudo mysql` to open to mysql shell
4. `CREATE USER 'username'@localhost IDENTIFIED WITH authentication_plugin BY 'password';` to create an admin user, replace username, and password with a username and password of your choosing.
6. `CREATE DATABASE climbingdatabasename;` Make an empty schema in your MySQL
7. `GRANT PRIVILEGE ON *.* TO 'username'@localhost;` Gives you user access to all databases and tables.
8. Create an .env file in the alien_top_logger\Django_Alien_Top_Logger folder with the following variables. Remember to update the DATABASE_NAME, DATABASE_USER and DATABASE_PASSWORD to be for your user.
```
SECRET_KEY=secretkey
DEBUG=True

ALLOWED_HOSTS=127.0.0.1
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000, http://localhost:8000

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASE_NAME=climbingdatabasename
DATABASE_USER=username
DATABASE_PASSWORD=yourdatebasepassword
```
9.  From there, you need to open up terminal, navigate to alien_top_logger\Django_Alien_Top_Logger folder, which the manage.py file is in located. Then, you can run the following :
10. `python manage.py migrate`, to run the db migrations
11. `python manage.py shell`
12. Copy and run contents of makegroups.py (located in alien_top_logger\Django_Alien_Top_Logger\climbing_app)
13. Ctrl z to exit shell
14. `python manage.py runserver` to run the server
15. Go to http://127.0.0.1:8000

## ToDo
**ToDo: Functionality:**
 * Customer users being able to see what routes other users have climbed would be good. If I do this, I feel like I should give customers the opportunity to not allow their route data to be visible to other users if they want to opt out of this.
  * Staff users should be able to see what staff user has added which route.
  * Staff users should be able to say that they have climbed a particular route to test it as a staff member.
  * Staff users should be able to  change the date and time of route creation.
  * I haven't implemented locking for staff users so they can't both edit the same route at once, maybe something to think about later, especially if I wind up with staff being able to change the location and date and time of creation of a route.
  * I think having a beginning and end grade range slider instead of a dropdown would be good as well, ie, being able to select all routes with blue holds between V0 and V5. It would mean changing the way grades are stored in the database though, which might be a bit annoying.
  * The map for the first and second room shouldn't be next to each other, I think they should be a slideshow of images you can click between which would leave space next to the slideshow to have the filter section so the user could easily see both things when in full screen. 
