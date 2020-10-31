# Fitness Home

## Full Stack Frameworks with Django Milestone Project-4

## Description

Fitness Home is designed and developed to create online presence of a fitness center, so that the fitness community
can purchase exercise plans, nutrition plans and merchandise online. Users can create an account and save profile information.
Users can also make secure payments and see their order history.

# UX

### Target Audience

 The target audience of this web-application is the fitness community and health conscious people as well as the people 
 who want to bring change in their life style. 
 
 ### Target Audience Goals

 - Able to browse the website easily.
 - Get information about the product and services.
 - Make secure payment.
 - Able to purchase anonymously.
 - Able to create account, save profile information and track order history.

 ### Site Owner's Goals:

 Site owner's main goal is to create online presence, create brand awareness and attract more customers to 
 sell them online through a secure payment method.

 ### Project Suitability

This project is suitable to make purchases online;
- Users have the ability to search for merchandise in the the store.
- Users have the ability to create an account and save their profile information.
- Users have the ability to purchase merchandise, exercise plan or nutrition plans and make secure payments.
- Users can view their order history.

### User Stories

- **As a store owner:**
1. As a store owner, I want a simple responsive user friendly website.
2. As a store owner, I want to add new products/services in the store.
3. As a store owner, I want to update existing products/services in the store.
4. As a store owner, I want to delete a product/service from the store.  

- **As a site user:**
1. As a user, I expect the website is easy to navigate from one page to another page.
2. As a user, I expect the website to be responsive so I can use it form any device for example mobile, tablet or laptop.
3. As a user, I want to be able to see the detailed information about the products and services.
4. As a user, I want to be able to make purchases anonymously.
5. As a user, I want to be able to create an account.
6. As a user, I want to be able to adjust the shopping cart.
7. As a user, I want to be able to save my profile information.
8. As a user, I want to be able to make secure payments.
9. As a user, I want to be able to see the order history.
10. As a user, I want to be able to update the profile information.
11. As a user, I want to receive a confirmation email after the checkout.


## Design

 The website design is simple and responsive which allows the user to navigate easily through the website form mobile, tablet 
 or laptop and make purchases. The design inspiration is taken from the **Code Institute's Boutique Ado Project**.

#### Fonts

-  Google fonts **Do Hyeon** is used in navbar and in headings. 
-  Where as google fonts **Ubunto** is used in rest of the text.

#### Icons

- To make design appealing font awesome icons are widely used in the website.

#### Attribute

- The target_blank value is given to the social links in the footer so that they will open in a new tab / window on click.

#### Colors

The color scheme of the website is kept fairly simple to make it attractive and appealing for the users. 
- Dark blue color **#12375a** is used for headings, text and button background in the website.
- Light grey color **#f8f9fa** is used as a background color of navbar and footer to make navigation links and buttons prominenet. 
- White color **fafafa** is used as a background color of the rest of the page so that products and the information can be displayed clearly.
- Red color **#e84610** is used in the breadcrum on landing page, in the delete button and in hover effect.    

#### Animation

- Animate in scroll library is also used you give nice effect on merchandise, exercise plans and nutrition plans.

#### Hover Effect

- Background color changes to red color **#e84610** when hover over the buttons.
- Cursor also changes to hand pointer when hover over buttons.

## Wireframes

Wireframes for this project were created by using [Balsamiq](https://balsamiq.com/). It includes wireframes for dektop,
tablet and mobile screen size.

- [Link to Wireframes](https://balsamiq.cloud/sw0h08w/p7zuf10/r2278) 
- [Wireframes in PDF](media/wireframes.pdf)

## Database & Data Models

**Sqlite3** databse is used in the development which is pre-installed by **Django**

- [Fitness Home Data Models in PDF](media/data-models.pdf)

## Features
### Existing Features

- **Navbar** - Navbar is fixed at the top all the time so user can easily navigate through the website. Logo is fixed 
at the top left corner. Navbar also contains links to the merchandise, exercise plans and nutrition plans as well as search bar, 
my account and shopping cart. On screen size less than 992 px navbar design changes as it appears a burger button on the top 
left corner which contians the logo fitness home, merchandise, exercise plans and nutrition plans. Search bar input field will
disappear and rest will stay the same. By clicking on search bar the search bar input will appear at the bottom of the navbar.
- **Log In/Sign Up** - User can easily log in if already have an account to access the extra features otherwise user has the
option to create an accout. User will get an email to verify the account when an account is created on fitness home. User can 
can also recover an account if user has forgotten the password.
- **Admin** - For website management the store owner will have extra links in my account dropdown when owner is logged in as 
a super user.
- **Customer Reviews** - When a user land on the home page, user can read the customer reviews by clicking on **Customer Reviews** button.
- **Search** - User can search for merchandise in the database either way, without logging in or after logging in the website.
- **Logout/Sign Out** - Logout allows a user to end the session but user has to confirm it by clicking on **Sign Out** which 
will bring the user to the home page.
- **Add to Cart** - User can add the merchandise, exercise plan or nutrition plan to the shopping cart with **Add to Cart** button.
- **Shopping Cart Adjustment** - User can update the quantity of merchandise or delete merchandise, exercise plan or nutrition plan
from the shopping cart.
- **Checkout** - User can checkout and pay by filling out the order form.
- **Order Summary** - On checkout page user will be shown the order Summary and button to adjust the shopping cart.
- **Profile** - Logged in user can save the delivery information in his/her profile.
- **Profile Update** - Logged in user can aslo update his/her delivery information saved in profile.
- **Autofill** - If user has saved his/her delivery information then the order form will be prefilled on next purchase.
- **Order History & Order Details** Logged in user can see his/her order history and details of particular order
by going into the profile page.
- **Add/Update/Delete Review** - Logged in user can also add, update or delete a review if user has purchased something.
- **Deletion Confirmation**- If a user click on delete button, then a modal will pop up to confirm if user is sure to delete the review or not.
- **Add/Update/Delete Product/Plans** - Update and delete buttons will only show up to the Super User (Store Owner). Super User 
can add new items, update existing items and delete the items from the website.
- **Deletion Confirmation for super user**- If super user click on delete button, then a modal will pop up to confirm if super user is sure to delete the product/plan or not.
- **Contact** - If user need any information, user has the possibility to contact the store owner by filling contact us form.
- **Thank You** - If a user sends an enquiry, a thank you message will be shown to the user afterwards.

### Features Left to Implement

- **Search** - At the moment search is performed only on the merchandise-product because the exercise plans and nutrition plans
are less in number. Thus as exercise plans and nutrition plans will grow in future, the search functionality will also be added in these sections.
- **Size** - Right now merchandise on sale has only one size. Thus in future different size will be added and also the 
functionality for user to select different size will also be added in the website.
- **Social Media Log In** - Log In through social media functionality will also be added in the future.
- **Coaching Sessions** -  A system to book session with the coach/trainer will also be added in future.
