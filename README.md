# Welcome to Alien Bloc's (unofficial) verison of TopLogger ! 
This is a personal project where I created a site where customers at Alien Bloc (the local climbing gym that I work at) could hypothetically track the routes that they climb. 

## Functionality
**Staff User funtionality:**

* Create new routes at a particular location on the map 
* Delete old routes

**Customer functionality:**

* Track climbs that they send
* See which climbs they have sent
  
**Shared functionality**
  
* Can filter routes by hold colour and V grade range 
* Can see route locations on the map when they select the routes from the route list

## Project structuring

This project is being created using Javascript with Vue, Python with Django, and a MySQL database. I used DigitalOcean for depolyment, along with apache. Certbot was used for SSL vertifcation. The DJango back end is serving my vue files, instead of having the front and back end running seperately. 

## Running locally
If you want to run this locally, 
1. `git clone` my repo
2. Install MySQL
3. `sudo mysql` to open to mysql shell
4. `CREATE USER 'username'@localhost IDENTIFIED WITH authentication_plugin BY 'password';` to create an admin user, replace username, and password with a username and password of your choosing.
6. `CREATE DATABASE climbingdatabasename;` Make an empty schema in your MySQL
7. `GRANT PRIVILEGE ON *.* TO 'username'@localhost;` Gives you user acess to all databases and tables.
8. Go into the `settings.py` file on the DJango folder (alien_top_logger\Django_Alien_Top_Logger\Django_Alien_Top_Logger), go to the DATABASES variable, and update the database to have your MySQL schema details (username, password).
9.  From there, you need to open up teminal, naviagte to alien_top_logger\Django_Alien_Top_Logger, which teh file manage.py is located. Then, you can run the following :
10. `python manage.py migrate`, to run the db migrations
11. `python manage.py shell`
12. Copy and run contents of makegroups.py (located in alien_top_logger\Django_Alien_Top_Logger\climbing_app)
13. Ctrl z to exit shell
14. `python manage.py runserver` to run the server
15. Go to localhost:8000

## ToDo
**ToDo: Functionality:**
  * Customer users being able to see what routes other customer users have climbed would be good. If I do this, I feel like I should give customers the oppurtunity to not allow their route data to be visible to other users if they want to opt out of this.
  * Staff users should be able to see what staff user has added which route.
  * Staff users should be able to say that they have climbed a particular route to test it as a staff member.
  * Staff users to be able to  change the date and time of route creation.
  * I haven't implemented locking for staff users so they can't both edit the same route at once, maybe something to think about later, especially if I wind up with staff being able to change the location and date and time of creation of a route.
  * I think having a beginning and end grade range slider instead of a dropdown would be good as well, ie, being able to select all routes with blue holds between V0 and V5. It would mean changing the way grades are stored in the database though, which might be a bit annoying.
  * The map for the first and second room shouldn't be next to each other, I think they should be a slideshow of images you can click between with would leave space next to the slideshow to have the filter section so the user could easy see both things when in full screen. Ah, the troubles of developing with inspect element open the whole time :( 

**ToDo: Code:**
* I realised part of the way through that vue props should have kebab case, and should probably go back and correct it so it looks more standard
* I probably should swicth to using env variable for the database password, but if someone has gotten into the mysql database, then at that point I imagine they have gotten into my ubuntu instance, likely as root user. In which case it won't matter what the db password is.
* I need to add tests, this was the opposite of test driven development...

## Next Time
If I could start again, I would first figure out deployment, then make the login page functional, create figma designs, figure out what database tables I will need to create and what columns they should have, then create api end points to get data from the back end, and finally make the front end functionaly. Instead, I started with figma designs, and the frontend...

Link to figma design:
https://www.figma.com/design/vHwCqeF9en6vpSCyVGyRsy/Alien_Top_Logger?node-id=0-1&p=f&t=poWZ5xZ3xkm750QU-0
 
