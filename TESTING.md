# Testing

## Contents 
   - [Automated Testing](#automated-testing)
      * [HTML validation](#w3c-markup-validator)
      * [CSS validation](#w3c-css-validator)
      * [JS validation](#jshint-javascript-validator)
      * [Pep8 validation](#pep8-validation)
      * [Lighthouse testing](#lighthouse-testing-in-devtools)
   - [Testing User Stories](#testing-user-stories)
   - [Bugs](#bugs)
      * [Found and Fixed](#found)


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
   There was some trouble given over the length of some lines of code. But when I shortened them it gave the error of
   'SyntaxError: EOL while scanning string literal' so I decided to keep the lines longer for functionality and for me its easier to identify problems while working. But besides that I didn't have any errors in the pythong I wrote thankfully. 
    
    ### Initial/final testing
       ![settings pass](/media/pep8/settingspep8) 
       ![merch pass](/media/pep8/merchpep8) 
       ![profile pass](/media/pep8/profilepep8) 
       ![urls pass](/media/pep8/settingspep8) 
       ![checkout pass](/media/pep8/checkoutpep8) 
       ![news pass](/media/pep8/newspep8) 
       ![bag pass](/media/pep8/bagpep8) 
       

-   ## [Lighthouse testing in devtools](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 
   - There was issues with the performance part of the lighthouse testing on the index page and it seems to be from Stripe and Cloudinary that makes loading times a bit longer. Since the images would only appear in a css folder that appears on cloudinary but thankfully the merch and news do not have this issue.

    ### Home page
       + Mobile 

          ![Mobile lighthouse scores for home page](/media/lighthouse/mobilelh.png)

       + Desktop

          ![Desktop lighthouse scores for home page](/media/lighthouse/homelh.png)
       + Error source
          ![Error lighthouse performance for home page](/media/lighthouse/errorlh.png)
      + Error source
          ![Error lighthouse performance for home page](/media/lighthouse/error2lh.png)


    ### News page
       + Mobile 

          ![News Mobile lighthouse scores ](/media/lighthouse/mobilenewslh.png)

       + Desktop

          ![News Desktop lighthouse scores ](/media/lighthouse/newslh.png)

    ### Merch page
       + Mobile 

          ![Mobile lighthouse scores for merch page](/media/lighthouse/mobilemerchlh.png)

       + Desktop

          ![Desktop lighthouse scores for merch page](/media/lighthouse/merchlh.png)

    ### Profile page
       + Mobile 

          ![Mobile lighthouse scores for profile page](/media/lighthouse/mobileprofilelh.png)

       + Desktop

          ![Desktop lighthouse scores for profile page](/media/lighthouse/profilelh.png)

    ### Add/Edit page
       + Add 

          ![lighthouse scores for add merch page](/media/lighthouse/addlh.png)

       + Edit

          ![lighthouse scores for edit merch page](/media/lighthouse/editlh.png)

    ### Post detail/ Merch Info page
       + Post Detail 

          ![Post detail lighthouse scores ](/media/lighthouse/postdetaillh.png)

       + Merch info

          ![Merch Info lighthouse scores ](/media/lighthouse/merchinfolh.png)

     ### Bag page

       + Bag

          ![Desktop lighthouse scores for edit event page](/media/lighthouse/baglh.png)

    ### Checkout page
       + Checkout

          ![Desktop lighthouse scores for contact page](/media/lighthouse/checkoutlh.png)
        
        
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

             ![Image showing mobile home page](/media/readme/userstories/homepage.png)

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

        5. As a first time visitor, I expect the site to look good on my mobile device. This was designed with a mobile first point of view and easily navigable for a mobile user.

            ![Image mobile navbar](/docs/readme/userstories/mobilenav.png)
            ![Image mobile navbar](/docs/readme/userstories/mobilehome.png)
            ![Image mobile news](/docs/readme/userstories/mobilenews.png)
            ![Image mobile merch](/docs/readme/userstories/mobilemerch.png)

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
       
       

## Bugs

   ### Found  
   - There seems to be an issue with webhooks in Stripe and the email confirmation after an order sends occasionally but not always. I'm not sure how to fix that.
   - There are performance issues as shown in the lighthouse screenshots and it seems that the Stripe/Cloudinary make the web page load a bit slow.
