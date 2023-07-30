# Hair Salon Booking System
![Responsive](docs/images/hairsalon-responsive.png)

## Purpose
The Booking System is a web application designed to streamline the process of scheduling and managing appointments for a beauty salon. <br> The application allows customers to view available time slots for different services provided by stylists and book appointments online.

The Booking System is intended to be used by Carlen & CO:s customers. <br> Stylists can be managed through Django's admin interface, <br> while customers can register and log in to book their preferred time slots for various beauty services.

With this application, both salon owners and customers can enjoy a hassle-free appointment scheduling experience, <br> enhancing the overall efficiency and convenience of the booking process.

## Features

### Existing Features

1. **Home Page And Navigation:** <br> An landing page providing an overview of the hair salon. <br> Non-logged-in users will be presented with a message. The navigation bar will follow the user to other pages.


2. **About Page:** <br> A dedicated page containing detailed information about the salon, its history, team, and philosophy.


3. **User Authentication:** <br> The application offers user registration and login functionalities using Django's built-in authentication system. When signed in the user will have access to the booking system.


4. **Booking Appointments:** <br> Customers can book appointments for specific time slots by selecting the desired slot from a dropdown list. However, they are prevented from booking more than one slot on a specific day.


5. **Edit and Delete Appointments:** <br> Customers can edit and delete their booked appointments as needed, subject to permission checks to ensure only the original customer can modify the booking.


6. **Confirmation Messages:** <br> The application provides confirmation messages and error messages to guide users through the booking process and notify them of successful or failed actions.


7. **Responsive Design:** The frontend templates are designed using Bootstrap, making the application mobile-friendly and accessible across different devices.
 
8. **Custom Error Pages:** <br> Custom error views are implemented to display user-friendly messages for 404 Not Found and 500 Server Error pages.


### Future Features

1. **Separate Schedules For Each Hairdresser**

2. **Manager View**

3. **Employee View**

## Data Model
<img src="docs/images/ERD.png" alt="mobile mockup, 404 error page" width="700"/>



 **The relationships between the models are as follows:** 

1. **User:**<br> This is the built-in Django User model, representing the users of the application. It contains fields like username, email, and password.

2. **Slot:**<br> This model represents the available time slots for appointments. It is related to the User model using a foreign key, as each slot belongs to a specific stylist (user). The model includes fields for date, start time, end time, and a boolean field to indicate whether the slot is reserved or not.

3. **Booked:**<br> This model represents the booked appointments. It includes foreign keys to the Slot and User models, as each booking is associated with a specific slot and user (customer). The model also includes a comment field for additional notes about the booking.

## User Stories And Testing

In this project, due to time constraints and project priorities,<br>
I made a deliberate decision to focus on manual testing rather than implementing automated tests


### Closed User Stories

#### 1. [Welcome/About Page](https://github.com/Stojj2/Portfolio-Project-4/issues/10)
   - As a **user** I can **get basic information about the salon without login in** so that **I am aware of open times and location**
<br><br>
     - **`Test 1 - Viewing the about page` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and press the "about" button from the menu.
       2. The about view should be displayed on the screen.
        <br><img src="docs/features/about.png" alt="mobile mockup, about page" width="250"/>

#### 2. [Account Registration](https://github.com/Stojj2/Portfolio-Project-4/issues/9)
  - As a **customer** I can **create a user account** so that **I can book and view my appointments**
<br><br>
     - **`Test 1 - Register an account` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and press the "Register" button from the menu.
       2. The signup form should be displayed on the screen.
        <br><img src="docs/features/register_page.png" alt="mobile mockup, register page" width="250"/>
       3. Fill in the form and press "Sign Up"
       4. The home page should be displayed on the screen with a message that says successfully signed in
        <br><img src="docs/features/sign_in-successfull.png" alt="mobile mockup, successful message" width="250"/>

#### 3. [Create Booking](https://github.com/Stojj2/Portfolio-Project-4/issues/1)
  - As a **customer** I can **view the list of available times offered by the salon** so that **I can book the one that suits my needs.**
<br><br>
     - **`Test 1 - Create booking` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and press the "Booking" button from the menu.
       <br><img src="docs/features/signed_in-menu.png" alt="mobile mockup, navbar/booking on phone" width="250"/>
       2. Press the "New" button from the dropdown list
       <br><img src="docs/features/menu_booking.png" alt="mobile mockup, navbar on phone" width="250"/>
       2. The "booking" page should be diplayed on the screen
       <br><img src="docs/features/booking.png" alt="mobile mockup, booking page" width="250"/>
       3. After filling in the form and clicking "submit," you will be redirected to the appointments page where your booked slot will be visible.
      <br><img src="docs/features/appointments.png" alt="mobile mockup, appointments with booking" width="250"/>
      <br><br><br><br>
     - **`Test 2 - Multiple booking protection` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and press the "Booking" button from the menu.
       <br><img src="docs/features/signed_in-menu.png" alt="mobile mockup, navbar/booking on phone" width="250"/>
       2. Press the "New" button from the dropdown list
       <br><img src="docs/features/menu_booking.png" alt="mobile mockup, navbar on phone" width="250"/>
       2. The "booking" page should be diplayed on the screen
       <br><img src="docs/features/booking-dubblebooking.png" alt="mobile mockup, booking page" width="250"/>
       3. Upon submitting the form with a slot that has the same date as the first one, an error message will be displayed indicating that you already have a booking on that day.
       <br><img src="docs/features/booking-dubbelbooking_error.png" alt="mobile mockup, booking page with error message" width="250"/>

#### 4. [Read Bookings](https://github.com/Stojj2/Portfolio-Project-4/issues/3)
  - As a **customer** I can **see my booked appointments** so that **I have a record of the details.**
     - **`Test 1 - Read booking` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and press the "Booking" button from the menu.
       <br><img src="docs/features/signed_in-menu.png" alt="mobile mockup, navbar/booking on phone" width="250"/>
       2. Press the "My Appointments" button from the dropdown list
       <br><img src="docs/features/menu_booking.png" alt="mobile mockup, navbar on phone" width="250"/>
       2. The "appointments" page should be diplayed on the screen, you should see the appointments that you have booked
       <br><img src="docs/features/appointments.png" alt="mobile mockup, appointments page" width="250"/>

#### 5. [Update Bookings](https://github.com/Stojj2/Portfolio-Project-4/issues/4)
  - As a **customer** I can **update my appointment** so that **I can change it at my convenience.**
     - **`Test 1 - Update appointment` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and click the "Booking" button from the menu.
       <br><img src="docs/features/menu_booking.png" alt="mobile mockup, navbar on phone" width="250"/>
       2. Click the "My Appointments" button from the dropdown list
       <br><img src="docs/features/appointments.png" alt="mobile mockup, appointments with booking" width="250"/>
       3. Click the "Edit" button on the data card you wish to modify, update the comment as needed, and then click the "Update" button to save the changes.
       <br><img src="docs/features/edit-appointments.png" alt="mobile mockup, edit-appointments page" width="250"/>
       4. The appointment should have been updated with the new comment
       <br><img src="docs/features/appointment-edited.png" alt="mobile mockup, edit-appointments page" width="250"/>
       <br><br><br><br>

     - **`Test 2 - Protection for updating another users appointment` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and click the "Booking" button from the menu.
       <br><img src="docs/features/menu_booking.png" alt="mobile mockup, navbar on phone" width="250"/>
       2. Click the "My Appointments" button from the dropdown list
       <br><img src="docs/features/appointments.png" alt="mobile mockup, appointments with booking" width="250"/>
       3. Click the "Edit" button on the data card you wish to modify
       <br><img src="docs/features/edit-appointments.png" alt="mobile mockup, edit-appointments page" width="250"/>
       4. Update the booking number in the last part of the URL to try to edit an appointment made by a different user.
       <br>
       User-1 (Loggedin)
       https://hairsalon4-ac0e725d37cb.herokuapp.com/edit/"user 1 booking nr"
       <br>
       to
       <br>
       User-2 (Not-Loggedin)
       Use a booking number that is in another users appointments list
       https://hairsalon4-ac0e725d37cb.herokuapp.com/edit/"another users booking nr"
       <br><img src="docs/features/error-500.png" alt="mobile mockup, error 500" width="250"/>
       

#### 6. [Delete Bookings](https://github.com/Stojj2/Portfolio-Project-4/issues/5)
  - As a **customer** I can **delete my booked appointment** so that **the information will reach the hairdresser**

       - **`Test 1 - Delete appointment` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and click the "Booking" button from the menu.
       <br><img src="docs/features/menu_booking.png" alt="mobile mockup, navbar on phone" width="250"/>
       2. Click the "My Appointments" button from the dropdown list
       <br><img src="docs/features/appointments.png" alt="mobile mockup, appointments with booking" width="250"/>
       3. Click the "Delete" button on the data card you wish to delete. Your booking should disappear from the appointments view
       <br><img src="docs/features/appointments_no-bookings.png" alt="mobile mockup, appointments" width="250"/>
       <br><br><br><br>

     - **`Test 2 - Protection for deleting another users appointment` <span style="color:green">✓</span>**
       1. Visit https://hairsalon4-ac0e725d37cb.herokuapp.com/ and click the "Booking" button from the menu.
       <br><img src="docs/features/menu_booking.png" alt="mobile mockup, navbar on phone" width="250"/>
       2. Click the "My Appointments" button from the dropdown list
       <br><img src="docs/features/appointments.png" alt="mobile mockup, appointments with booking" width="250"/>
       
       4. change the URL as described bellow to try to delete an appointment made by a different user.
       <br>
       User-1 (Loggedin)
       https://hairsalon4-ac0e725d37cb.herokuapp.com/appointments
       <br>
       to
       <br>
       User-2 (Not-Loggedin)
       Use a booking number that is in another users appointments list
       https://hairsalon4-ac0e725d37cb.herokuapp.com/delete/"another users booking nr"
       <br><img src="docs/features/error-500.png" alt="mobile mockup, error 500" width="250"/>

### Open User Stories

#### 8. [Separate Schedules For Each Hairdresser](https://github.com/Stojj2/Portfolio-Project-4/issues/2)
  - As a **customer** I can **see the availability of each hairdresser** so that **I can book an appointment with a specific stylist.**

#### 9. [Manager View](https://github.com/Stojj2/Portfolio-Project-4/issues/8)
  - As a **manager** I can **edit all employee schedules** so that **I have full control of all the staff and which customers they have on their schedule**

#### 10. [Employee View](https://github.com/Stojj2/Portfolio-Project-4/issues/7)
  - As a **hairdresser** I can **view and update my customer bookings** so that **I can keep track of my schedule accurately.**

<br><br>

## Validator testing

### HTML
1. https://validator.w3.org/nu/?doc=https%3A%2F%2Fhairsalon4-ac0e725d37cb.herokuapp.com%2F
<br>

2. https://validator.w3.org/nu/?doc=https%3A%2F%2Fhairsalon4-ac0e725d37cb.herokuapp.com%2Fabout

**Bugs**
1. W3 error from having a body element in all templates. should only be in base.html file
   - element replaced with a div element. 

### Python

**admin.py**
<br><img src="docs/testing/admin.py.png" alt="PEP8" width="1000"/>

**forms.py**
<br><img src="docs/testing/forms.py.png" alt="PEP8" width="1000"/>

**models.py**
<br><img src="docs/testing/models.py.png" alt="PEP8" width="1000"/>

**views.py**
<br><img src="docs/testing/views.py.png" alt="PEP8" width="1000"/>

**Bugs**
1. Long line errors
   - shortening f-strings


### CSS
**style.css**
<br><img src="docs/testing/style.css.png" alt="CSS picture" width="1000"/>

**Bugs**
**0**

### Lighthouse
**Desktop**
<br><img src="docs/testing/signout-desktop.png" alt="Lighthouse" width="400"/>
<img src="docs/testing/signin-desktop.png" alt="Lighthouse" width="400"/>
<img src="docs/testing/home-desktop.png" alt="Lighthouse" width="400"/>
<img src="docs/testing/about-desktop.png" alt="Lighthouse" width="400"/>
<img src="docs/testing/register-desktop.png" alt="Lighthouse" width="400"/>
<img src="docs/testing/scheduler-desktop.png" alt="Lighthouse" width="400"/>
<img src="docs/testing/appointments_edit-desktop.png" alt="Lighthouse" width="400"/>
<img src="docs/testing/appointments-desktop.png" alt="Lighthouse" width="400"/>


## Technology 
  - **GitPod**
    - GitPod where used for writing all code 
  - **GitHub**
    - For storing the code GitHub where used
  - **Django**
    - For a fullstack framework
  - **Bootstrap**
    - For design and styling
 - **ElephantSQL**
    - For running a PostgreSQL database
 - **Cloudinary**
    - For storing media assets in the cloud.      
  - **Heruko**
    - Heruko was use to deploy the app
  - **Mobile FIRST**
    - Mobile First Chrome extension where used for screenshots
    
## Deployment
### Heroku
This project was deployed to Heroku.
  - Steps for deployment:
    - Fork or clone this repository
    - Create a new heruko app
    - Go to settings and set up the "Config Vars" 
    - Link the Heruko app to the repository 
    - Click **Deploy**
    
 ### GitPod
 The entire coding process was carried out using the cloud-based IDE GitPod.
  - The app was coded using GitPod. The steps to deploy is as following:
  - In the GitHub repository, press the green GitPod button for transfer the project to GitPod enviroment
    - NOTE!
      - [GitPod webbrowser plugin](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki) To access this button, it is necessary to install this plugin on your browser.

## Credits

**Tomas Jansson** -  For pictures and media from the hair salong CARLEN & CO <br>
http://www.scubasite.nu/

**Rohit Sharma** - For mentoring me thru this project

**Django** - For the development of this full-stack web application, providing a user-friendly interface and robust features. It's a powerful tool that simplified and accelerated the entire process <br>
https://www.djangoproject.com

**Bootstrap** - for quick design and style developing <br>
https://getbootstrap.com

**Code Institute** - For providing invaluable walk-through projects that significantly aided in resolving numerous issues. <br>
https://codeinstitute.net/
