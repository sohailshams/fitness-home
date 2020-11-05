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
3. As a user, I want to be able to search the items in the store.
4. As a user, I want to be able to see the detailed information about the products and services.
5. As a user, I want to be able to create an account.
6. As a user, I want to be able to add items in the shopping cart and adjust the shopping cart.
7. As a user, I want to be able to save delivery information to my profile.
8. As a user, I want to be able to make secure payments.
9. As a user, I want to be able to make purchases anonymously.
10. As a user, I want to be able to see the order history.
11. As a user, I want to be able to update the profile information.
12. As a user, I want to receive a confirmation email after the checkout.
13. As a user, I want to get in touch with the store owner.
14. As a user, I want to be able to add a review.
15. As a user, I want to be able edit or delete my review.


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
- **Merchandise Size** - At the moment the merchandise products have only one-size available. The option to purchase 
different sizes of the merchandise products will also be added in the future.

## Technologies Used

- **HTML5** - HTML5 is used to create the the structure of the website.
- **CSS3** - CSS3 is used for custome styling the HTML5 elements. 
- **JavaScript/JQuery** - is used to make the website interactive. 
- **[Bootstrap Framework](https://getbootstrap.com/)** - Front-end framework is used to make website responsive.
- **[Python](https://www.python.org/)** - Python is used as the back-end programming language.
- **[Django](https://www.djangoproject.com/)** - Python Web framework that encourages rapid development is used to create this project.
- **[Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)** - Django crispy forms are used to control the rendering behavior of Django forms.
- **[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)** - Jinja templating language is used with Django in the HTML5 code.
- **[Balsamiq](https://balsamiq.com/)** - Balsamiq is used to create wireframes for this project.
- **[Google Fonts](https://fonts.google.com/)** - Google fonts *Do Hyeon* and *Ubunto* are used in this project.
- **[Git](https://git-scm.com/)** - Used as a distributed version control system.
- **[Gitpod](https://www.gitpod.io/)** - Used as a online IDE.
- **[Github](https://github.com/)** - Used as a remote repository. 
- **[Heroku](https://www.heroku.com/#)** - It is used as hosting platform to deploy this project.
- **[Stripe](https://stripe.com/en-dk)** - Used to add secure payment feature in this project.
- **[HTML Formatter](https://webformatter.com/html)** - Used to format and beautify my code.
- **[Animate On Scroll](https://michalsnik.github.io/aos/)** - Used to make website visually appealing.

## Testing

Google developers tool has been used form the  beginning to see the the result after adding a feature or after making
any changes, how do they looks like on different screen sizes. Further I used **print statement** to debug the issues.
I created my own account and tested all the functions to make sure they work properly. In addition, I aslo asked my family and
friends to test the project and give their feedback.

### User Stories

User stories from the UX section were tested to see if they all work as intended. 

#### As a store owner

- *As a store owner, I want a simple responsive user friendly website.*
1. A simple minimalist design is created. 
2. Go to the **Home** Page and browse through the website to experience the design.
3. Right click and go to **inspect** and choose mobile, tablet or desktop screen size to test the page responsiveness.
- *As a store owner, I want to add new products/services in the store.*
1. Go to the **Home** Page.
2. Log In as a **super user** and click on **My Account**, a dropdown will open.
3. Go to **Merchandise Admin**, **Exercise Admin** or **Nutrition Admin**.
4. Fill out the relevant form and click on **Add**
5. Item will be added in the store.
- *As a store owner, I want to update existing products/services in the store.*
1. Go to the **Home** Page and log in as a **super user**.
2. Go to **Merchandise, **Exercise** or **Nutrition**.
3. Under each product/service **Edit** button will show up.
4. Click on **Edit** button, make changes and click on **Update** button to make updates.
- *As a store owner, I want to delete a product/service from the store.*
1. Go to the **Home** Page and log in as a **super user**.
2. Go to **Merchandise, **Exercise** or **Nutrition**.
3. Under each product/service **Delete** button will show up.
4. Click on **Delete** button, a modal will appear to confirm the deletion.
5. Click on **Yes**, item will be deleted.

#### As a site user

- *As a user, I expect the website is easy to navigate from one page to another page.*
1. Go to the **Home** Page.
2. Navbar stays at the top all the time and contains the main navigation links like **Merchandise**, **Exercise** and **Nutrition**
as well as a search bar **My Account** button and **Shopping Cart**.
3. **Home** button is also added in different placed in the website. Thus user can easily navigate through the website.
- *As a user, I expect the website to be responsive so I can use it form any device for example mobile, tablet or laptop.*
1. Go to the **Home** right click and go to **inspect**.
2. Choose mobile, tablet or desktop screen size you want to test the page responsiveness.
- * As a user, I want to be able to search the items in the store.*
1. Go to the **Search input box** in the navbar.
2. Add any search key word and click on search icon.
- *As a user, I want to be able to see the detailed information about the products and services.*
1. Go to the **Home** Page.
2. For **Merchandise** item's detail, go to **Merchandise** and click on **Detials** button.
3. A new window will open which contains the item detail.
4. For **Exercise Plns** detail, click on **Exercise**.
5. A new window will open which contains the **Exercise Plns** and their detail.
4. For **Nutrition Plns** detail, click on **Nutrition**.
5. A new window will open which contains the **Nutrition Plns** and their detail.
- *As a user, I want to be able to create an account.*
1. Go to the **Home** Page and click on **My Account**.
2. From the dropdown select **Register**.
3. Fill in the form and click on **Sign Up**.
4. Verification email will be sent to provided email address.
5. Verify your email addess, your account is created.
- *As a user, I want to be able to add items in the shopping cart and adjust the shopping cart.*
1. Go to the **Home** Page.
2. To add **Merchandise** items , go to **Merchandise** and click on **Detials** button.
3. A new window will open which contains the item detail and **Add to Cart** button.
4. Click on **Add to Cart** button to add item in the **Shopping Cart**.
5. To add **Exercise Plns**, click on **Exercise**.
6. A new window will open which contains the **Exercise Plns**.
7. Click on **Add to Cart** button to add the **Exercise Plan** in the **Shopping Cart**.
8. To add **Nutrition Plns**, click on **Nutrition**.
9. A new window will open which contains the **Nutrition Plns**.
10. Click on **Add to Cart** button to add the **Nutrition Plan** in the **Shopping Cart**.
11. To adjust the **Shopping Cart**, click on the **Shopping Cart**.
12. A new window will open which contain the **Shopping Cart** items.
13. To update the quantity of the merchandise item change the quantity in the input box.
14. Clik the **Update** button to adjust the **Shopping Cart**.
15. To delete any item from the **Shopping Cart** click on **Delete** button.
- *As a user, I want to be able to save delivery information to my profile.*
1. Go to the **Home** page and log in.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form and check **Save this delivery information to my profile** box.
- *As a user, I want to be able to make secure payments.*
1. Go to the **Home** page and log in.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form.
5. Add credit card number, expiry date, cvc, zip and click on **Complete Order** button.
- *As a user, I want to be able to make purchases anonymously.*
1. Go to the **Home** page.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form.
5. Add credit card number, expiry date, cvc, zip and click on **Complete Order** button.
- *As a user, I want to be able to see the order history.*
1. Go to the **Home** page and log in.
2. Click on **My Account** and select **My Profile** from the dropdown.
3. If user has already purchased something then in **User Info** section **My Orders** button will appear.
4. Click on **My Orders** button to view the order history.
- *As a user, I want to be able to update the profile information.*
1. Go to the **Home** page and log in.
2. Click on **My Account** and select **My Profile** from the dropdown.
3. A new window will open, which contains the delivery information.
4. Change any information and click on **Update** button.
- *As a user, I want to receive a confirmation email after the checkout.*
1. Go to the **Home** page and log in.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form.
5. Add credit card information and clik on **Complete Order** button.
6. An order confirmation email has sent to the user.
- *As a user, I want to get in touch with the store owner.*
1. Click on contact icon in the footer.
2. A new window will open which contains **Contact Us** form.
3. Fill in the form and clik on **Send** button.
- *As a user, I want to be able to add a review.*
1. Go to the **Home** page and log in.
2. Click on **My Account** and select **My Profile** from the dropdown.
3. If user has already purchased something then in **User Info** section **Add Review** button will appear.
4. Click on **Add Review** button, a new window will open which contains **Add Review** form.
5. Fill in the form and click **Add** button.
- *14. As a user, I want to be able edit or delete my review.*
1. Go to the **Home** page and click on **Customer Reviews**.
2. A new window will open which contains all the reviews.
3. **Edit** and **Delete** buttons will appear under your added review.
4. Click on **Edit** button, a new window will open to edit the review.
5. Make the changes and click on **Update** button.
6. To delete the review, click on **Delete** button, a modal will appear to confirm the deletion.
7. Click on **Yes** to delete the  review.

### Responsiveness on different browsers & Mobiles

The website is tested on following browsers and mobiles, it looks fine and work properly on them.
- Google Chrome
- Microsoft Edge
- Firefox
- Opera 
- iPhone 6
- Huawei P30 lite

### Code Validation

The code has been validated by using;

- [W3C Markup Validation Service for HTML](https://validator.w3.org/)
- [W3C Markup Validation Service for CSS](https://jigsaw.w3.org/css-validator/)
- [Pep8 Online for Pyhton](http://pep8online.com/)
- [JSHint](https://jshint.com/)

### Interesting Bugs / Issue

1. **Modal was not working properly** - I added a modal to make sure that super user really wants to delete the produsts / services, 
it's not just accessdently **Delete** button is pressed. But I encountered a problem that when I was deleting an item, an other item
was deleted from the store even though I was using {{ item.id }} as an id and data-target. Some how the it was not working with 
numbers so with the help of tutor support, a solution was found. Used {{ item.sku }} as an id and data-target and it solved 
the issue.
2. **Modal stopped working** - To delete products / services from store super user has to confirm the deletion, as by clicking 
on **Delete** button a modal pops up but I realized that this modal stopped working. I found out later that it happened after 
I **added animate on scroll**. To over come this issue I excluded the **Delete** button from **AOS** div and everything start working fine. 
3. **Image was not showing up** - If a product / service does not have an image associated with it, then a no image shall 
show up but it was not happening. I made sure that media_url is added in the settings.py and urls.py but I was not getting the desired output. 
Later I found out that I forgot to add noimage.png in the media folder that is why there was no image to show if an item 
did not have an image. So I added noimage.png in the media folder and it solved the problem. 
4. **Local variable 'intent' referenced before assignment** - When I completed checkout/views.py and created an order I start
getting this error. The initial thought was that it is happening because the **form is not valid** and it is triggering the else block.
But I tested this with print statement and I could see the **intent** was created in the terminal. The issue was
actually I was not returning anything if the **form was valid**. I was missing the redirect to **checkout_success** which I had not
created till this point. So I created checkout success page and redirected to **checkout_success** and got rid of this error. Credit to
**Chris Zielinski** who helped me to identify this issue.  
5. **Total was not counted** - I encountered with this issue of total not being counted when I add, delete or save line item.
The reason found that was causing this problem was I did not include **default_app_config = 'checkout.apps.CheckoutConfig'** in **checkout/__init__.py**.

## Credits

### Media

- All pictures are taken from [Google](https://www.google.com/)

### Acknowledgements

1. Code Institute's **Boutique Ado Project** was great source of inspiration. I followed it to design and develop my **Fitness Home** website.
2. Code for **bottom to top** button is taken from [w3schools.com](https://www.w3schools.com/)
3. Code Institute's tutor support has been a great help during the whole project, a very special thanks to tutor support team.
4. **[Bootstrap Framework](https://getbootstrap.com/)** is used in this project.
5. A very special thanks to **Chris Zielinski** for his support and help to accomplish this project.
6. I would like to thank my mentor **Owonikoko Oluwaseun** for his valuable feedback during mentoring sessions. 
7. **[Stack overflow](https://stackoverflow.com/)** was great source of help.
8. I would like thank my lovely wife Ayesha, my sons Ibrahim and Ismail for their support and motivation.
9. Used favicon Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> 
from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
10. [Django Docs](https://docs.djangoproject.com/en/3.1/)

## Disclaimer
This project is for educational purposes only..