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

The W3C Markup Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no syntax errors in the project.

-   ## [W3C Markup Validator](https://validator.w3.org/) 

    - index.html
       * No errors found.

       ![index.html validation](/docs/readme-assets/testing_images/home-html.png)

    - base.html
       * No errors found.

       ![shop.html validation](/docs/readme-assets/testing_images/shop-html.png)

    - merchandise.html
       * Added the missing closing span tag and removed duplicate class attribute.

       ![product.html validation](/docs/readme-assets/testing_images/product-html.png)
  
    - merchandise_info.html
       * No errors found.

       ![basket.html validation](/docs/readme-assets/testing_images/basket-html.png)

    - checkout.html
       * Had put for="#idname" in label element like you do for collapsibles, removed the hashtag.

       ![checkout.html validation](/docs/readme-assets/testing_images/checkout-html.png)

    - checkoutsuccess.html
       * No errors found.

       ![checkoutsuccess.html validation](/docs/readme-assets/testing_images/checkoutsuccess-html.png)

    - add-merchandise.html
       * 

       ![add-vinyl.html validation](/docs/readme-assets/testing_images/addproduct-html.png)

    - edit-merchandise.html
       * Same issues as add-vinyl bar the genre issue, clearly had copied and pasted.

       ![edit-vinyl.html validation](/docs/readme-assets/testing_images/editvinyl-html.png)

    - news.html
       * Duplicate class element on each event card due to the for loop. Had introduced these duplicates when I was adding mr-2 class to everything, didn't obviously look for an existing class attribute first.

       ![event.html validation](/docs/readme-assets/testing_images/event-html.png)
      
    - post_detail.html
       * No errors found

       ![add-event.html validation](/docs/readme-assets/testing_images/addevent-html.png)

    - bag.html
       * No errors found

       ![edit-event.html validation](/docs/readme-assets/testing_images/editevent-html.png)

    - profile.html
       * Duplicate class as above. In forms.py my add placeholders section wasn't indented properly and therefore the "if field != 'default_country':" wasn't actually doing anything.

       ![profile.html validation](/docs/readme-assets/testing_images/profile-html.png)


-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    
       ![css validation](/docs/readme-assets/testing_images/css.png)
   

-   ## [JSHint JavaScript Validator](https://jshint.com/) 
    

    - stripe_elements.js
       * Same as base.js plus stripe variable required by stripe so justified.

       ![stripe_elements.js validation](/docs/readme-assets/testing_images/stripejs.png)
       ![stripe_elements.js validation](/docs/readme-assets/testing_images/stripejs2.png)

    - ratings.js
       * Same as base.js


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
        1. As an unregistered visitor, I want to be able to add products to my cart
           On the landing page, the spinning vinyl, call to action button opens shop page, aswell as there being a 
           shop link in the nav menu.

             ![Image showing landing page call to action button](/docs/readme-assets/testing_images/shop_btn.png)
             ![Image showing Shop nav link](/docs/readme-assets/testing_images/nav.png)

        2. As an unregistered visitor, I want to be able to view my cart
           The basket is on the top right of the page. When there are items the number is in 
           brackets beside the basket. In addition when a product is added to the basket, success 
           message contains a link to view basket.

             ![Image showing basket in nav menu](/docs/readme-assets/testing_images/basket.png)
             ![Image showing Success message view basket link](/docs/readme-assets/testing_images/view_basket.png)

        3. As an unregistered visitor, I want to be able to edit my cart
           In view basket page there are Update and Delete links that open collapsibles.

             ![Image showing edit and delete links in basket](/docs/readme-assets/testing_images/edit_basket.png)

        4. As an unregistered visitor, I want to be able to checkout
           In view basket page and in success message upon adding a product there is a checkout 
           button that takes user to checkout page.

             ![Image showing checkout button in basket](/docs/readme-assets/testing_images/checkout_btn.png)
             ![Image showing Success message checkout button](/docs/readme-assets/testing_images/message_checkout.png)

        5. As an unregistered visitor, I want to see an order confirmation
           When an order is put through, the checkout success page renders and the user will recieve 
           a confirmation email.

             ![Image showing checkout success page](/docs/readme-assets/testing_images/order_confirm.png)
             ![Image showing order confirmation email](/docs/readme-assets/testing_images/order_email.png)

        6. As an unregistered visitor, I expect the site to look good on my mobile device.
           The site was designed with mobile first in mind

             ![Image showing mobile home page](/docs/readme-assets/testing_images/home.png)
             ![Image showing mobile nav menu page](/docs/readme-assets/testing_images/mobile_nav.png)
             ![Image showing mobile shop page](/docs/readme-assets/testing_images/shop.png)
             ![Image showing mobile product details page](/docs/readme-assets/testing_images/details.png)
             ![Image showing mobile basket page](/docs/readme-assets/testing_images/basket_mobile.png)
             ![Image showing checkout page](/docs/readme-assets/testing_images/checkout.png)
             ![Image showing mobile contact page](/docs/readme-assets/testing_images/contact.png)

        7. As an unregistered visitor, I want to easily search the vinyls.
           The Shop page has the products grouped in genres of which the user can use the arrows to browse through.
           The "Browse Genre" heading above each carousel is a link so that the user can see all products of a genre at once.
           There is also a view all products link and a search box.
           
             ![Image showing browse genre, see all and search box](/docs/readme-assets/testing_images/browse_products.png)

   - #### First Time Visitor (in addition to above)
        1. As a first time visitor, I want to easily understand the main purpose of the site.
           The landing page has a call to action button that says "Shop Vinyl", there is also an about 
           section that explains what the site is for.
            
             ![Image showing call of action and about section](/docs/readme-assets/testing_images/about.png)

        2. As a first time visitor, I want to be able to intuitively use the site.
           I have kept the basket on the top right, the logo on the top left, the nav menu at the top 
           and other links in the footer where a user will expect to find them. This aids with single user
           learning and therefore intuitive use.

             ![Image showing nav bar](/docs/readme-assets/testing_images/nav_bar.png)
             ![Image showing footer links](/docs/readme-assets/testing_images/links.png)

        3. As a first time visitor, I expect to see an attractive, visually appealing site.
           Main landing page image colours are carried through the site for uniformity. The three images 
           used at top of each page are all music themed but prevent the user getting bored of the same image.

             ![Image showing shop page image](/docs/readme-assets/testing_images/shop_pic.png) 
             ![Image showing profile page image](/docs/readme-assets/testing_images/profile_pic.png)
             ![Image showing contact page image](/docs/readme-assets/testing_images/contact_pic.png)

        4. As a first time visitor, I expect an accessible site.
           All links are aria labelled, all images have alternative text and the colour contrast ratio passes 
           lighthouse testing.

        5. As a first time visitor, I want to easily register.
           Register link is in main nav menu and in footer links for non registered users. In addition the 
           banner for non signed in users is a link to register page.

            ![Image showing main nav link to register](/docs/readme-assets/testing_images/mobile_nav.png)
            ![Image showing sign in link in the footer](/docs/readme-assets/testing_images/links.png)
            ![Image showing banner registration link](/docs/readme-assets/testing_images/banner.png)

   - #### Registered Returning Visitor Goals
        1. As a returning visitor, I want to be able to view and add to the event board.
           Link in the main nav menu and in the banner for logged in users. On the event page there 
           is an Add event button at the top, this takes the user to the add event page.

             ![Image showing event link in main nav menu](/docs/readme-assets/testing_images/event_link.png)
             ![Image showing add event form](/docs/readme-assets/testing_images/add_event_form.png)
             ![Image showing banner event page link](/docs/readme-assets/testing_images/event_banner.png)
             ![Image showing add event button](/docs/readme-assets/testing_images/add_event.png)

        2. As a returning visitor, I want to follow on social media so I can hear of any new products.
           In the footer of each page are Social media links.

             ![Image showing social links](/docs/readme-assets/testing_images/social.png)
           
        3. As a returning visitor, I want to be able to change my password.
           On the users profile page, under My Account section is a link to change password.

             ![Image showing change password link](/docs/readme-assets/testing_images/my_account.png)
             ![Image showing change password page](/docs/readme-assets/testing_images/change_password.png)
           
        4. As a returning visitor, I want to be able to save my details
           User can save personal information via a button on the profile page that open a collapsible section
           or when placing an order via the save my information link.

             ![Image showing edit info button](/docs/readme-assets/testing_images/edit_info.png)
             ![Image showing save info checkbox](/docs/readme-assets/testing_images/save_info.png)

        5. As a returning visitor, I want to get feedback so I know that something has went through.
           Whenever as user adds, adjusts or deletes an item from their basket a pop up message appears. 
           In addition the user recieves emails upon registration, placing an order and submitting a contact form.
           Upon submitting an order the user is also taken to an order confirmation page. 
            
             ![Image showing registration email](/docs/readme-assets/testing_images/registration_email.png)
             ![Image showing order confirmation email](/docs/readme-assets/testing_images/order_email.png)
             ![Image showing contact email](/docs/readme-assets/testing_images/contact_email.png)
             ![Image showing success message](/docs/readme-assets/testing_images/view_basket.png)
             ![Image showing order confirmation page](/docs/readme-assets/testing_images/order_confirm.png)
             
   - #### Registered Frequent Visitor Goals
        1. As a frequent visitor, I want to be able to edit an event I’ve added to the event board.
           On the event page, if a user created an event they will have the option to edit or delete the event.

             ![Image showing edit event link](/docs/readme-assets/testing_images/edit_event.png)
             ![Image showing edit event form](/docs/readme-assets/testing_images/edit_event_form.png)

        2. As a frequent visitor, I want to be able to contact the owner.
           In the main nav there is a link to the contact page which take user to the contact form
           to complete. If user has completed their personal information, this will prefill the relevant fields.

             ![Image showing contact us nav link](/docs/readme-assets/testing_images/nav.png)
             ![Image showing contact form](/docs/readme-assets/testing_images/contact_form.png)

        3. As a frequent visitor, I want to be able to edit my profile information.
           On profile page, there is a My Info section with an edit info button,
           this opens the edit info section.

             ![Image showing edit info button](/docs/readme-assets/testing_images/edit_info.png)
             ![Image showing edit info section](/docs/readme-assets/testing_images/edit_info_form.png)
            
        4. As a frequent visitor, I want to be able to delete my account
           On profile page, under My account section is a delete account link,this opens a delete confirmation prior to deleting.

             ![Image showing delete account link](/docs/readme-assets/testing_images/delete.png)

        5. As a frequent visitor, I want to be able to see my order history.
           On users profile page there is a My Orders section, this lists date and truncated order number, this is a link
           which opens up original order confirmation page. Order table is horizontally scrollable on smaller screens.

             ![Image showing past order link](/docs/readme-assets/testing_images/my_orders.png)
             ![Image showing order information](/docs/readme-assets/testing_images/view_order.png)

        6. As a frequent visitor, I don't want to have never ending scrolling up or down.
           Every page has a back to top link in the footer.

             ![Image showing back to top link](/docs/readme-assets/testing_images/links.png)

        7. As a frequent visitor, I want to be able to search for events.
           On the event page at the top is a search bar. The user can search for name, location or details.

             ![Image showing events search bar](/docs/readme-assets/testing_images/search.png)

   - #### Superuser goals
        1. As superuser, I want to be able to add, delete or edit a product.
           In nav menu for superusers there is an Add Product link which opens the add vinyl page.

             ![Image showing add vinyl link in main menu](/docs/readme-assets/testing_images/add_vinyl.png)
             ![Image showing add vinyl form](/docs/readme-assets/testing_images/add_vinyl_form.png)

        2. As superuser, I want to be able to add a genre.
           In superusers main menu is a link to the admin panel where they can add new genres.

             ![Image showing add genre in admin panel](/docs/readme-assets/testing_images/add_genre.png)
             
        3. As superuser, I want to be able to delete or edit an event on the event board
           Superuser can edit or delete any event on the event board. This can be via the edit and delete links 
           at the bottom of each event card or via the admin panel.

             ![Image showing delete user in admin panel](/docs/readme-assets/testing_images/delete_event.png)
             ![Image showing delete event in admin panel](/docs/readme-assets/testing_images/admin_delete.png)
             ![Image showing edit event in admin panel](/docs/readme-assets/testing_images/admin_edit.png)
             
        4. As superuser, I want to be able to delete a user.
           User can enter admin through the Admin link on their main menu. In the admin panel they can select
           users from the left hand side, select the user they want to delete and in drop down choose delete selected users. Alternatively they can inactivate the user via the permissions option when they open the users record.

             ![Image showing delete user in admin panel](/docs/readme-assets/testing_images/delete_user.png)
             ![Image showing inactivate user in admin panel](/docs/readme-assets/testing_images/inactivate_user.png)

        5. As superuser, I want to be able to make another user an admin.
           As above but for inactivating a user but under permissions select staff and superuser permissions.

             ![Image showing admin permissisons in admin panel](/docs/readme-assets/testing_images/admin.png)

        6. As superuser, I don’t want users to be able to order product if there is none left in stock.
           If product has a stock_quantity of 0, the add to basket buttons are inactivated. In addition if user 
           adds to basket but then someone purchases the last one prior to them checking out, it'll be removed from basket and they will be informed. 

            ![Image showing out of stock message with no add to basket button available](/docs/readme-assets/testing_images/out_of_stock.png)
            ![Image showing error message due to stock no longer available](/docs/readme-assets/testing_images/error.png)
       
      
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
     
