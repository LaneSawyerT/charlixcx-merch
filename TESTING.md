# Testing

## Contents 
   - [Automated Testing](#automated-testing)
      * [HTML validation](#w3c-markup-validator)
      * [CSS validation](#w3c-css-validator)
      * [JS validation](#jshint-javascript-validator)
      * [Pep8 validation](#pep8-validation)
      * [Lighthouse testing](#lighthouse-testing-in-devtools)
      * [Unit testing](#unit-testing)
   - [Testing User Stories](#testing-user-stories)
   - [Manual testing](#manual-testing)
   - [Bugs](#bugs)
      * [Found and Fixed](#found-and-fixed)
      * [Existing](#existing)


## Automated Testing

The W3C Markup Validator and W3C CSS Validator were used to validate all the main pages of the project to ensure there were no syntax errors in the project. All had the same or similar warnings about using too many '---' for comments in the code which I use to help my eyesite. Also, I added the type/Javascript to scripts thinking it would help organise the code a bit better and I didn't give h2 to the foot sections because of size issues I wanted to do.

-   ## [W3C Markup Validator](https://validator.w3.org/) 

    - index.html

       ![index.html validation](/media/html/indexhtml.png)

    - merchandise.html

       ![merchandise.html validation](/media/html/merchhtml.png)

    - merchandise_info.html

       ![merchandise_info.html validation](/merch/html/merchinfohtml.png)
  
    - add_merch.html

       ![add_merch.html validation](/media/html/addmerchhtml.png)

    - Edit_merch.html

       ![Edit_merch.html validation](/media/html/editmerchhtml.png)

    - Bag.html

       ![Bag.html validation](/media/html/baghtml.png)

    - Profile.html

       ![Profile.html validation](/media/html/profilehtml.png)

    - Checkout.html

       ![checkout.html validation](/media/html/checkouthtml.png)

    - news.html

       ![event.html validation](/media/html/news.png)
      
    - Checkout_success.html

       ![Checkout_success.html validation](/media/html/checkoutsuccesshtml.png)

    - Post detail.html
       ![Post detail.html validation]()


-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

   -  Thankfully passed the CSS without a problem.
    
       ![css validation](/media/readme/css.png)
   

-   ## [JSHint JavaScript Validator](https://jshint.com/) 
    

    - stripe_elements.js
       * Same as base.js plus stripe variable required by stripe so justified.

       ![stripe_elements.js validation](/media/readme/stripejs.png)

    - quantity_input_element.html 
       ![quantity.js validation](/media/readme/quantityjs.png)


-   ## [Pep8 validation](http://pep8online.com/) 
    
    ### Initial/final testing
       [this on stack overflow](https://stackoverflow.com/questions/53158284/python-giving-a-e501-line-too-long-error?noredirect=1&lq=1) and so implemented it and didn't seem to break the auth_password_validators

       ![settings.py validation](/docs/readme-assets/testing_images/settings.png)
       ![settings.py retest](/docs/readme-assets/testing_images/fixedsettings.png)


-   ## [Lighthouse testing in devtools](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 

    ### Home page
       + Mobile 

          ![Mobile lighthouse scores for home page](/docs/readme-assets/testing_images/home-lighthouse.png)

       + Desktop

          ![Desktop lighthouse scores for home page](/docs/readme-assets/testing_images/home-desktop.png)

    ### Shop page
       + Mobile 

          ![Mobile lighthouse scores for shop page](/docs/readme-assets/testing_images/shop-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for shop page](/docs/readme-assets/testing_images/shop-desktop.png)

    ### Add Product page
       + Mobile 

          ![Mobile lighthouse scores for add product page](/docs/readme-assets/testing_images/add-product-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for add product page](/docs/readme-assets/testing_images/add-product-desktop.png)

    ### Edit Product page
       + Mobile 

          ![Mobile lighthouse scores for edit product page](/docs/readme-assets/testing_images/edit-product-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for edit product page](/docs/readme-assets/testing_images/edit-product-desktop.png)

    ### Profile page
       + Mobile 

          ![Mobile lighthouse scores for profile page](/docs/readme-assets/testing_images/profile-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for profile page](/docs/readme-assets/testing_images/profile-desktop.png)

    ### Event page
       + Mobile 

          ![Mobile lighthouse scores for event page](/docs/readme-assets/testing_images/events-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for event page](/docs/readme-assets/testing_images/events-desktop.png)

    ### Add Event page
       + Mobile 

          ![Mobile lighthouse scores for add event page](/docs/readme-assets/testing_images/add-event-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for add event page](/docs/readme-assets/testing_images/add-event-desktop.png)

     ### Edit Event page
       + Mobile 

          ![Mobile lighthouse scores for edit event page](/docs/readme-assets/testing_images/edit-event-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for edit event page](/docs/readme-assets/testing_images/desktop-edit-event.png)

    ### Contact page
       + Mobile 

          ![Mobile lighthouse scores for contact page](/docs/readme-assets/testing_images/contact-report-mobile.png)

       + Desktop

          ![Desktop lighthouse scores for contact page](/docs/readme-assets/testing_images/contact-desktop.png)
        
    
-   ## Unit Testing 
    I knew at the start that I wanted to try and implement automated testing. I was worried I'd spend too long trying to get the testing right that I wouldn't get all the project requirements done, so I left it to the end, which I realise is not how you do it.
    Tried to get as much done in the time I had left, not as much as I would have liked but its something that I can improve and learn more about going forward.

      ![Coverage for project](/docs/readme-assets/testing_images/coverage-report.png)
  
    ### Home app

      ![Coverage for home app](/docs/readme-assets/testing_images/home-coverage.png)

    ### Contact app

      ![Coverage for contact app](/docs/readme-assets/testing_images/contact-coverage.png)

    ### Profile app

      ![Coverage for profile app](/docs/readme-assets/testing_images/profiles-coverage.png)

    ### Products app

      ![Coverage for products app](/docs/readme-assets/testing_images/products-coverage.png)

    ### Checkout app

      ![Coverage for checkout app](/docs/readme-assets/testing_images/checkout-coverage.png)

    ### Basket app

      ![Coverage for basket app](/docs/readme-assets/testing_images/basket-coverage.png)

    ### Events app

      ![Coverage for events app](/docs/readme-assets/testing_images/events-coverage.png)

## Testing User Stories 

   - #### Unregistered Visitor
        1.  As an unregistered visitor, I want to be able to add products to my bag.
            Below you can see a button on the selected merchandise for the customer to add to their bag.

             ![Image showing add to bag](/media/readme/userstories/add.png)

        2. As an unregistered visitor, I want to be able to view my bag.
           The bag is on the top right of the page. When there are items the number is in 
           brackets beside the bag. In addition when a product is added to the basket, success 
           message contains a link to view basket.

             ![Image showing bag in nav menu](/media/readme/bagtotal.png)
             ![Image showing Success message view bag link](/media/readme/userstories/addtobag.png)

        3. As an unregistered visitor, I want to be able to edit my bag.
           In view bag page there are Update and Delete buttons

             ![Image showing edit and delete links in bag](/media/readme/userstories/editbag.png)

        4. As an unregistered visitor, I want to be able to checkout and pay.
           In view bag page and in success message upon adding a product there is a checkout 
           button that takes user to checkout page.

             ![Image showing checkout button on bag page](/media/readme/userstories/checkoutpage.png)
             ![Image showing Success message checkout button](/media/readme/userstories/checkoutbag.png)

        5. As an unregistered visitor, I want to see an order confirmation.
           When an order is put through, the checkout success page renders.

             ![Image showing checkout success page](/media/readme/userstories/orderconfirm.png)

        6. As an unregistered visitor, I expect the site to look good on my mobile device.
           The site was designed with mobile first in mind

             ![Image showing mobile home page](/docs/readme-assets/testing_images/home.png)

        7. As an unregistered visitor, I want to easily Search the website for products
           
             ![Image showing  search box](/media/readme/userstories/searchbar.png)

        8. As an unregistered visitor, I want to be able to easily register.
            Register link is in main nav menu and in footer links for non registered users. In addition the 
            banner for non signed in users is a link to register page.

              ![Image unregistered footer](/media/readme/userstories/unregisteredfooter.png)

            ![Image unregistered my account nav](/media/readme/userstories/unregisteredhome.png)



   - #### First Time Visitor (in addition to above)
        1. As a first time visitor, I want to easily understand the main purpose of the site.
           The landing page has a photo of the cover of Charli XCX's new album and the footer has a brief description about her.
            
             ![Image home page](/media/readme/userstories/homepage.png)
             ![Image about footter](/media/readme/userstories/aboutfooter.png)

        2. As a first time visitor, I want to be able to intuitively use the site.
           I have kept the basket on the top right, the logo on the top left, the nav menu at the top 
           and other links in the footer where a user will expect to find them. This aids with single user
           learning and therefore intuitive use.

             ![Image showing nav bar](/media/readme/userstories/navbar.png)
             ![Image showing footer links](/media/readme/userstories/footerlinks.png)

        3. As a first time visitor, I expect to see an attractive, visually appealing site.
           Main landing page image colours are carried through the site for uniformity to give a sleek design.

             ![Image showing home page image](/media/readme/userstories/homepage.png) 
             ![Image showing profile page image](/media/readme/userstories/profilepage.png)
             ![Image showing news page image](/media/readme/userstories/newspage.png)

        4. As a first time visitor, I expect an accessible site.
           All links are aria labelled, all images have alternative text and the colour contrast ratio passes 
           lighthouse testing in the devtools.

        5. As a first time visitor, I expect the site to look good on my mobile device. This was designed with a mobile first point of view.

            ![Image mobile design](/docs/readme-assets/testing_images/mobile_nav.png)

   - #### Registered Returning Visitor Goals
        1. As a returning visitor, I want to be able to see previous order history. Users can make their way to their profile and see that their order history is there.

             ![Image showing orderhistory](/media/readme/userstories/orderhistory.png)

        2. As a returning visitor, I want to be able to purchase more merchandise with previous details saved.
           The user has their information saved to make their next purchases easier.

             ![Image showing details on profile](/media/readme/userstories/detailsprofile.png)
           
        3. As a returning visitor, I want to look at new updates or news from this artist. The User can make their way to the news site and see just that.

             ![Image showing news page](/media/readme/userstories/newspage.png)
           
        4. As a returning visitor, I want to be able to save my details or liked news posts.
           User can save their favorite news stories on the post details page and it will show up in their profile page.

             ![Image showing liked posts](/media/readme/userstories/likednews.png)

        5. As a returning visitor, I want to search for specific merchandise. Users have the functionality to search for the specific product they are looking for.
            
             ![Image showing searchbar](/media/readme/userstories/searchbar.png)
             
   - #### Registered Frequent Visitor Goals
        1. As a frequent visitor, I want to be able to easily look at my liked news posts. Users can look back at their profile page to see the liked news post.

             ![Image showing liked posts](/media/readme/userstories/likednews.png)

        2. As a frequent visitor, I want to be able to edit my profile information.
           In the profile page there is a a form. If user has completed their personal information, this will prefill the relevant fields.

             ![Image showing details on profile](/media/readme/userstories/detailsprofile.png)

        3. As a frequent visitor, I want to be able to see my order history.
           On profile page, there is a spot to see all the previously processed orders.

             ![Image showing orderhistory](/media/readme/userstories/orderhistory.png)
            
        4. As a frequent visitor, I want to be able to search for merchandise. Users have the functionality to search for the specific product they are looking for.

             ![Image showing searchbar](/media/readme/userstories/searchbar.png)


   - #### Superuser goals
        1. As superuser, I want to be able to add or edit merchandise.
           On the Add merchandise page the admin can upload the relevant details for their merchandise.

             ![Image showing add merchandise](/media/readme/userstories/adminmerchandise.png)

        2. As superuser, I want to be able to add updates about the artist.
           In superusers main menu is a link to the admin panel where they can add new genres.

             ![Image showing posts in admin panel](/media/readme/userstories/adminnews.png)
             ![Image showing add post in admin panel](/media/readme/userstories/adminlistpost.png)
             
        3. As superuser, I want to be able to make another user admin. Admins can chose in the adminal panel under User which one to pick and click the labels for superuser.

             ![Image showing admin superuser](/media/readme/userstories/superuser.png)
             
        4. As superuser, I want to be check availability of limited products. Users can go onto the merchandise page and click on edit and see the limited number of the limitted product on display and update accordingly. 

             ![Image showing delete user in admin panel](/media/readme/userstories/limitednum.png)

        5. As superuser, I want to be able to keep customers up to date on the artists via news posts. The superuser can create many different posts about the artist in the news post admin page.

        6. As superuser, I don’t want users to be able to order product if there is none left in stock.
           If product has a stock_quantity of 0, the add to basket buttons are inactivated and on the main merchandise page to say that it is soldout. 

            ![Image showing out of stock message with no add to basket button available](/media/readme/userstories/nobutton.png)
            ![Image showing out of stock message on merchandise page](/media/readme/userstories/soldout.png)
       
      
## Manual Testing

-  I generally test as I'm developing as well as at the end so some of the findings are from during development. The website was viewed with browsers: Google chrome, Safari, Microsoft Edge, Firefox and Opera. Viewed all pages on each and checked the following:

### Home Page/base.html 
  - Nav links from main menu works
  - Nav links change depending on users log in and superuser status.
  - Logo takes user to home page.
  - Shop vinyl spinning button takes user to shop page.
  - Basket icon takes user to view basket page
  - Banner takes user to event page if logged in.
  - Banner takes user to register page if not logged in.
  - Social links work and open in a new window.
  - Back to top link works
  - Other links in footer work and change according to user log in status.
  - Hover effects work on all links and buttons.

### Shop page
  - Vinyl search bar works for song, title or artist for logged in and non logged in users.
  - Genre header links allow user to see all products of that genre.
    * Hover effect wasn't working, .genre h3 a styling was overriding the hover effect of a:hover. 
  - Genre header links are underlined on small and medium screens to make it more obvious that they are clickable as hover effects aren't in play.
  - View all link allows user to view all products
  - Carousel arrows work for those genres with more than one product
  - Details buttons open product page.
  - All products should have an image, backup image shows if a broken image. 
    * Removed default image from one of the products and it broke the site. Fixed the default_images view to use 
    one of the other images if no default image, else product not displayed. As adding a default image is required 
    on the Add Vinyl page, this shouldn't happen. 

### Product Details page
  - Back to shop link works.
  - Add to basket button works, message shows with basket contents.
  - Success message checkout button, close buttons and view basket link works.
  - Basket in nav updates to show number of items in basket and current grand total.
  - When a product has only one left in stock, a hurry paragraph shows. 
  - When a product has no stock left, add to basket buttons aren't available and an Out of stock paragraph shows.
  - Product Admin functionality only shows for superusers.
  - Product admin edit button opens Edit Product Page.
  - Product admin delete button opens a delete confirmation, cancel button closes it and delete button, successfully deletes product from database and success message shows.

### View Basket Page
  - Edit item opens a collapsible to edit quantity. Quantity values available are will be stock quantity of that product so will differ between them.
  - Update basket and cancel button in the edit collapsible both work.
  - Upon basket update success message shows
  - Delete product button opens a delete confirmation, cancel button closes it and "Yes, I'm sure" button, successfully deletes product from basket and success message shows.
  - Success messages within basket page shouldn't show the basket contents as that would be pointless.
  - Continue shoppping link takes user back to shop page.
  - Checkout button takes user to checkout page
  - When editing basket, totals and delivery update accordingly.
  - Toast messages close button works.
  - Toast message vinyl icon is a different colour depending on what type of toast it is, green for success, red for error etc.

### Checkout Page
  - Checkout form prefills if user has saved information on their profile page
  - Back to basket link works
  - Checking save info, saves users information to profile.
  - Checking save info saves users address & delivery address if provided to Address Book.
  - Unchecking save info, does not save users info
  - Form can submit without delivery data filled in
  - Form will not submit without required fields completed
  - Form will not submit with white space as an entry
    * I put empty space in the first name field, I got an internal server error. Went back and filled in the name and then got a processing error. When I checked admin this was because the order had actually went through via the webhook. In development environment repeated to see what error I would get. It said "The view checkout.views.checkout didn't return an HttpResponse object. It returned None instead." I wrote a validators.py file and added it into my required models and migrated, this did not fix the issue. I put return redirect('checkout') in the else block if form not valid, that seemed to solve the issue and now shows an error message. So didn't end up migrating changes to the model to Postgres database. I was wondering why the order and payment still went through, but I realised as stripe requires a name and my surname field was filled in, this was sufficient information for stripe but not for my model. Now however the stripe payment goes through twice and two orders appear in database as two intents created so two pids created. As this is due to stripe accepting just the first or surname in the name field, so in stripe_element.js added a check for both names and if not show an error message. Tried to make it a toast but I couldn't get it to work, tried creating and inserting an element for it and putting in the toast html but after spending hours on it I gave up due to time restraints and just put a similar error div that is used to display stripe errors. I'm sure it was something stupid I was doing so will revisit at a later date.

### Checkout Success Page
  - The success messages show, one for saving info if that was selected and one for order.
    * Noticed that when I have multiple messages the white background and border don't meet when I close one and when there are no 
      messages there is a dot where they appear. Realised I'd applied the border styling to the message container div and not the 
      toasts themselves.
  - The information is all there and table filled with product information. Table should scroll horizontallly on smaller screens.
  - Confirmation email should have sent to user with correct information.
  - Back to shop button takes user back to shop page.
  - If showing an old order, back to profile button should do just that.

### Edit Product page
  - Need to add a product link takes user to add product page
  - Cancel links at top and bottom of page take user back to product details page.
    * Bottom cancel link took user back to shop page not product detail. Fixed href.
  - Form is prefilled with current information
  - File input, shows images that have been selected.
    * Input field was overflowing,causing horizontal scroll on mobile screen, changed bootstrap 
      classes.
    * On iphone a mini image view is beside the input field aswell as the image preview I coded. This is not on desktop or 
    android phone so left in.
  - Submit Changes button works and changes are reflected in database.
  - Form will not submit without required fields completed
  - Form will not submit where required fields are just whitespace.
    * I got an error and a success message at the same time. Realise in my view the getting files section
      and success message weren't within the if form.is_valid() block.

### Add Merchandise Page
### Profile page

### Events Page

### Add event page


### Contact Us Page
  - Cancel buttons take user back to shop page.
    * Hadn't added cancel buttons
  - Contact form will prefill if user has saved information to their profile.
  - Contact form will not submit without required personal details. 
  - Ratings work and on successful form submission, success message shown
  - Upon contact form submission user receives a personalised acknowledgment email.
  - Send button works, displays success message and adds record to database.
  
### Registration page
  - Registration form won't submit without required information.
  - Registration successfully adds a new user and their profile.

### Error pages
 

## Bugs

   ### Found and Fixed 


   ### Existing