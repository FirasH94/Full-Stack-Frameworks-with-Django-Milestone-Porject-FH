Link to deployed website [Fitness Paradise](https://firas-fitness-paradise-django.herokuapp.com/)  
     
# Fitness Paradise

Fitness Paradise is an online supplements shop where users are able to browse different fitness related products to help them achieve/boost their fitness goals.

To achieve this, the user would need to sign up and create a new account. Once they have created and verified their account, they are able to browse the products on the website and make the necessary purchases. The user would need to insert their delviery details, contact details and banking information in order to complete the purchase.

Furthermore, the user will be able to write a review on the product that they have used for others to view and help in making decisions when purchasing.

The website also contains a blog page where the users can find some useful nutritional information or general stories about the fitness industry.


### Developer goals:

-	To help the customer boost their journey in reaching their fitness goal.
-	To help the user increase their fitness knowledge.
-   To enable the customer in sharing their opinion regarding a product for other customers to see.
-   To allow the user to register and create an account.

### User goals and interests:


- 	To purchase supplements that support them in their fitness goals.
-	Being able to view different types of products and read product reviews that are written by other users.
-	To register an account and have the ability to write a review about a specific product.
-	To read blogs about different fitness related topics.

### Users who would be interested in this web app (Target clients)


- 	Someone looking to build muscle.
-	Someone looking to become lean.
- 	Somneone looking to buy and consume different type of Vitamins.
-   Someone looking to boost their energy during a workout session.
-   Someone looking to review a product and provide an advise.
-   Someone looking to buy products and consume as meal replacements.


## UX

**This application was developed for the following stories:**


-	As a user type, I want to purchase suplements that help me become lean.
-	As a user type, I want to purchase suplements that help me bulk in muscle mass.
-	As a user type, I want to purchase suplements that act as a meal replacement when I do not have time to cook food.
-	As a user type, I want to be able to sign up and create an account.
-   As a user type, I want to have the ability to view product reviews and leave a product review myself.
-   As a user type, I want to view the product details about a specific product.
-   As a user type, I want to add products to the shopping cart.
-   As a user type, I want to view the shopping cart with all the products I am about to purchase.
-   As a user type, I want to have the ability to change my address and billing details.
-   As a user type, I want to to have the ability to search specific products by typing a specific name in a search bar.
-   As a user type, I want to view products using different types of categories.
-   As a user type, I want to have the ability to view different blogs about fitness written by the admin.
-   As a user type, I want to receive a confirmation email confirming that my order has been placed and a purchase has been made successfully.


This app was designed to be responsive on all available platforms such as desktops, tablets and mobile phones.



**Wireframes**


The user can view the initial wireframes design for this web app by downloading the following [PDF document](https://pdfhost.io/v/JwPqTlm1U_Project_Wireframespdf.pdf).

## Features



**Navigation around the site:**

The web app consists of multiple pages which will be explained in more detail below.


The navigation bar changes into a toggler when viewed on a smaller sized screen such as mobile phone. 
When the screen size shrinks, a burger menu button appears which then can be clickable to slide out from the left all the navigation links around the app.


**Home Page:**

This is the main page where the user will be landing when accessing the web app for the first time.

This page is a very basic page with a button that says "Shop now" which will take the user to the products page.


**All Products:**

This is the page where the user is able to view all the products that are available in the store.

The user can also view products based on: categories, price, rating, type of protein, performance, vitamins & health.

There is also a search bar for the user to use and search a specific product by using a keyword.

There is also the "sort" dropdown menu which the user can use to sort the products by different methods such as prices low to high or alphabetically.

The user will be able to see the name, price, category and rating of each product. The admin will also have the edit/delete buttons visible for them for each product to modify.

Each product can be clicked to access the product details page of that product.


**Product details:**

On this page the user will be able to see the name, price, category and rating of each product. The admin will also have the edit/delete buttons visible for them for each product to modify.

There is also a summary description of the product and what it is about to provide the user with more information about the product.

On this page the user will be able to pick what flavour they want to have the product in and the quantity of the product.

Under the product, there is a review form. This is available for people that have registered only. This allows the user to post a review on this product and giving them up to a 5 star rating.

The review will be displayed to the right hand side of the product form for all the users to read.

**Shopping cart:**

The user will be able to see the full list of products they have added to the cart.

The usaer will also be able to modify the cart by updating the quantity of the products or removing them completely from the shopping cart.

Each product will be displayed with the name, flavour and SKU code.

The user will be able to see the: price, subtotal price of each prodcut, the bag total, the delivery charge and the gran total.

**Checkout (Stripe pay):**

This page will require the user to fill in their personal details such as: Name, Email, Delivery address and Payment info.

If the user is signed up, the will be able to save all the information for future purposes use.

This page will also display the order summary of the products to the right hand side.

Once the user has inserted the correct details, they are able to click on "Complete order" and confirm the purchase with Stripe.


**Order confirmation (Thank you):**

The user will be redirected to the confirmation page which will display all their purchase details.

The user will also have a confirmation email sent directly to their email confirming their order.

**Register:**

All fields are required to fill.

Email validation will detect if the email already exists.

Password validation and confirm password match.

An alert message will advise the user if the username or email address already exists.

Once the user registers, they will need to verify their email through a confirmation link that is sent directly to their email inbox.

**Login:**

Login system with the user's username and password.

An alert message will advise the user if the username or password is incorrect.

When user logged in the top navigation burger menu in the right hand side changes from register and login to my profile, product management (for admins) and logout.

a forgotton password link should user forget password

**My profile:**

The user will be able to change their delivery information.

An order history view to the right hand side which the user can click on each individual previous orders to preview the order details.

**Product management (admin account):**

The admin will be able to fill in the product details information here and add a new product to the supplements page.

This is a quicker option to do rather than accessing the admin panel.

**Blog:**

Blogs will be written and posted by the admins only.

This page will dispaly all the published blogs.

Each blog card will contain the blog title, author, publishing date and a summary of the blog.

A read more button is visible for the user to click and access the full blog details page.

**Blog details:**

This page will display the full story of the published blog for the users to read.

**Admin dashboard:**

The admin can add/edit accounts.

The admin can add/edit blogs and publish them.

The admin can view preview order history of all users and remove them if needed.

The admin can access the Categories/comments and products which they are able to add/edit/remove.

Stocks and quantity of products can be reviewed and edited by the admin.

**Features to implement in the future:**

-	A coupon system for customers.
-	The functionality to have the shopping cart saved on a user's account so when they log out and back in, their cart does nto reset.
-	A change password functionality in "my profile"
-   To prevent a user from posting multiple reviews and limit them to 1 for each product.


## Technologies used 

-   Django Framework - Through gitpod used the Framework to create the whole project.
-	HTML/HTML5 – This was used to implement most of the content on the site.
-	CSS – This was used for the design/look and feel of the site.
-	Git – Used as a repository for version control.
-	Heroku - Used to host the files and the web app itself as well as version control.
-   AWS - Used to load and host the Static files including all images.
-	Gitpod – This is the platform used for developing the web app.
-	Bootstrap – This was used mainly for navigation purposes and to aid in making the web app responsive.
-	material.io - This was used to fetch the icons for the social media platforms in the footer.
-	JavaScript/jQuery – This was used to implement the bag quantity/remove item functionality and product sort selector.
-   Stripe - Payment integration system.
    Google Fonts - For the typeography of the site.


## Testing



W3C Markup Validation was used to validate HTML.

W3C CSS validation was used to validate CSS.

The majority of functionality has been tested at each stage of development and the bugs/issues have been resolved, before moving on to another step.

### Generic/Journey testing:

The following have been tested from a user’s perspective to ensure the web app works as expected:

-	Easy to navigate around the web app as the navigation bar/menu is easily visible on the web app.
-	Each page of the web app easily recognisable, easy to navigate around and easy to read/understand.
-   Submit the empty registration form and an alert message pops up asking to fill in the fields. This has been tested for all required fields.
-   Submit the registration form with username less than 4 characters and a message pops up, "Please lengthen this text to 6 characters or more (you are currently only using 2 characters)".
-   Submit an incorrect email and an alert message pops up for email validation.
-   Submit the form with an already existing username and email. An error message will appear mentioning that the credentials exist.
-   Submit the form with a short password. I receive the error messages of password being too short/too common. Also if I try to submit a numeric password only, I get error message too.
-   Complete the form with mismatch passwords and an alert message pops up informing me that the passwords do not match.
-   Submit the form with all inputs valid and verify that a success message appears.
-   Submit cart checkout while leaving some fields empty and an alert message pops up asking to fill in the fields. This has been tested for all required fields.
-   Submit the card with wrong payment information and an alert message pops up saying my card details are invalid.

### Manual Testing

-	Navigation links:
	Each navigation link has been tested to ensure that it is linked to the correct page. The navigation link has also been tested when viewed on a smaller screen sizes to ensure the functionality is consistent making sure the toggler is activated correctly.
-	Login/Logout/Register/Read more (blog post):
    The functionality of these buttons have been all tested to make sure they work correctly as expected.
-	Adjust bag/Keep shopping:
	The functionality of these buttons have been all tested to make sure they work correctly as expected. Adjust bag returns me to the cart and Keep shopping returns me to the products page.
-	Sort dropdown/flavours dropdown/quantity picker:
	The functionality for these have been tested manually and all work correctly as expected. The products are displayed correctly with the correct flavour and quantity in the cart.
-	Write a review functionality:
	The full functionality has been tested for this from the start to end. The review gets submitted with the correct name of user, subjectm review comment and publish date. Also, I am unable to post a review when I am not logged in as a user.
-	Edit/Delete admin buttons for the product:
	The functionality of these buttons has been tested and work as expected when logged in as a superuser. These links are not visible for normal users.
-	Update/Delete shopping cart product functionality:
	The update works correctly when I change the quantity and the remove button completely removes the product from the cart.
-	Numeric fields:
	Numeric fields have been tested to make sure the user is unable to insert any characters apart from numbers.
-   Search bar:
    The search bar was tested by inserting a keyword and it dispalyed the correct related products.
-   Account registeration email/Order confirmation email:
    Both of these have been tested and I received an email successfully asking me to confirm my email and an email confirming my order.

The web app content was checked and tested to make sure that there was no Grammarly error.


### Cross browser/device testing:

**iPad:**

-	Safari: The web app has been tested to make sure all sections are appearing correctly on iPad making sure the media queries are working as expected. This has been tested as landscape as well as portrait.

-	Chrome: The web app has also been tested on the chrome browser making sure it is displayed consistently a long with Safari on the iPad device.


**Desktop:**

-	Chrome: Testing was done to make sure all images/content was displayed clearly on the large desktop screen.

-	Firefox: Testing was also carried on Firefox to make sure everything is consistent with chrome.


**Android phone:**

-	Android internet: Tested mainly to make sure the web app is responsive correctly on small screen sizes. This was tested through landscape and portrait orientation.

-	Chrome: The web app was also tested on chrome mainly for orientation purposes.


### Issues found and resolved:

The main testing was done throughout carrying the project which means that almost all issues were fixed as the implementation carried forward.

The edit/done/remove icons were not being aligned correctly to the right hand side of each collapsible. This was fixed.

The web app title was coming out of the navigation menu when viewed on android due to size issues. This has been fixed.


### Left to resolve:

The modal which provides the user a confirmation message on the manage categories page is removing the wrong category. I will be looking into this further to find a work around and make sure the correct categoryy is removed.



## Deployment

This project was developed using Gitpod as well as MongoDB to create the database, this was then committed to git and heroku then pushed to GitHhub and Heroku as well through the terminal.

To deploy the project on Heroku, I took the following steps:

1.	Logged into Heroku.
2.	On Gitpod through terminal I created the requirements.txt file.
3.	I also created the Procfile through the terminal.
4.	I also used the terminal on Gitpod to commit and push the project to Heroku.
5.	Once the project has been pushed, I added all the necessary Config Vars to make sure the website is deployed and pulling through correctly.
6.	Once all the steps above have been done, the web app should be ready to view online when clicking on the "View app" button within Heroku.

Please note - On submission the The Development Branch and Master Branch of this project are identical.

The submission URL to the Final version of the website is: https://workout-tracker-python-project.herokuapp.com/



## Credits

**Content:**

-	All the content within the website Has been written by me from scratch.


**Media:**

-	All the icons used on the website have been taken from material.io.

**Code:**

-	The look and feel of the website was created from scratch by me however I have used https://materializecss.com/ to assist me in the design and implementation of the front-end design.

## Disclaimer

The content of this website was created for educational purposes only.