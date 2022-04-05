# Charli XCX - Merchandise

Here is a link to the live project. (https://charlixcx-merch.herokuapp.com/)

This website was created for Milestone 4 

![Image showing the website displayed on different screen sizes]()

## Contents 

- [User Experience (UX)](#user-experience-ux)
   * [Strategy](#strategy)
   * [User Stories](#user-stories) 
   * [Scope](#scope)
      + [Current Features](#current-features)
      + [Features to implement in the future](#features-to-implement-in-the-future)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
     + [Colour Scheme](#colour-scheme)
     + [Typography](#typography)
     + [Imagery](#imagery)
     + [Design Choices](#design-choices)
- [Technologies](#technologies)
   * [Languages used](#languages-used)
   * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

   - [Challenges](#challenges)

- [Testing](#testing)
   
- [Deployment](#deployment)
   * [Creation](#creation)
   * [Forking](#forking)
   * [Clone](#clone)
   * [Setting up AWS](#setting-up-aws)
   * [Setting Up Stripe](#setting-up-stripe)
   * [Setting Up Project](#setting-up-project)
   * [Heroku Deployment](#heroku-deployment)

- [Credits](#credits)
   * [Code](#code)
   * [Content](#content)
   * [Media](#media)
   * [Acknowledgements](#acknowledgements)

## User Experience (UX)

   ### Strategy 
   - User goals 
     * I want to be able to buy different types of merchandise from this artist.
     * I want to buy physical music from this artist.
     * I want to check the updates for this artist.
     * I would like it to be easily navigable on any screen size and remember my purchase details.

   - Site owner/ business goals
     * As the site owner, I would like to prioritise sales of music and apparel.
     * As the site owner, I would like to be able to update customers/fans on the artist.
     * As the site owner, I would want it to be easily navigable so that customer feel welcomed back.

   ### User Stories

   - #### Unregistered Visitor
        1. As an unregistered visitor, I want to be able to add products to my bag.
        2. As an unregistered visitor, I want to be able to view my bag.
        3. As an unregistered visitor, I want to be able to edit my bag.
        4. As an unregistered visitor, I want to be able to checkout and pay.
        5. As an unregistered visitor, I want to see an order confirmation.
        6. As an unregistered visitor, I expect the site to look good on my mobile device.
        7. As an unregistered visitor, I want to easily Search the website for products
        8. As an unregistered visitor, I want to be able to easily register.

   - #### First Time Visitor (in addition to above)
        1. As a first time visitor, I want to easily understand the main purpose of the site.
        2. As a first time visitor, I want to be able to intuitively use the site.
        3. As a first time visitor, I expect to see an attractive, visually appealing site.
        4. As a first time visitor, I expect an accessible site.
        5. As a first time visitor, I expect the site to look good on my mobile device.

   - #### Registered Returning Visitor Goals
        1. As a returning visitor, I want to be able to see previous order history.
        2. As a returning visitor, I want to be able to purchase more merchandise with previous details saved.
        3. As a returning visitor, I want to look at new updates or news from this artist
        4. As a returning visitor, I want to be able to save my details or liked news posts.
        5. As a returning visitor, I want to search for specific merchandise.
      
   - #### Registered Frequent Visitor Goals
        1. As a frequent visitor, I want to be able to easily look at my liked news posts.
        2. As a frequent visitor, I want to be able to edit my profile information.
        3. As a frequent visitor, I want to be able to see my order history.
        4. As a frequent visitor, I want to be able to search for merchandise.

   - #### Superuser goals
        1. As superuser, I want to be able to add, delete or edit merchandise.
        2. As superuser, I want to be able to add updates about the artist.
        3. As superuser, I want to be able to make another user admin.
        4. As superuser, I want to be check availability of limited products.
        5. As superuser, I want to be able to keep customers up to date on the artists via news posts.
        6. As superuser, I don’t want users to be able to order product if there is none left in stock.


   ### Scope

   Within project conception, a list of features were compiled, these were the scored 
   between 1 & 5 for importance and feasibility/ viability which then decided which features 
   could be included for initial launch.    

   #### Current features 

-   Responsive on all device sizes

-   Accessible 

-   Easy to navigate (Single use learning)

-   Interactive elements

-   Social Links 

-   Contact form prefills the personal information for logged in users.

-   Changing nav menu and footer links and buttons in depending on the users log in status, admin status and what event if any they have added.

-   Able to search products for song, artist or album name.

-   Can search events for name of event, location or details.

-   'Back to top' footer link on each page, saves users from having to scroll up to Nav bar especially on mobile devices.

-   Logged in users can add events to event board.

-   Logged in user can save their addresses and default address, pre-fills Checkout form

-   User can edit events on event board that they themselves added. 

-   User can edit their own profile information

-   Admin users can add, edit and delete any merchandise.

-   When product stock quantity is 0, add to cart buttons are not available and will display 'Out of Stock'.

-   Confirmation email on registration and on successful purchase.

   #### Features to implement in the future

- 

### Structure

-   Created a database schema using [GraphizOnline](https://dreampuf.github.io/GraphvizOnline/), as per Emmets     instructions on [slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1642276160282900) see [here](/media/readme/db.png) to view better.

### Skeleton 

Wireframes were created on Balsamiq (see links below)

* [Mobile](/media/readme/mobilewf.png)
* [Tablet](/media/readme/tabletwf.png)
* [Desktop](/media/readme/desktopwf.png)

The finished project does differ a bit from the wireframes. There are less merchandise products per row on the page and I've changed the footer to better match the useful links. Also, on the profile page there is now the added functionality of seeing which news posts you like and going back to them. And on the news page, it is now more centered than left/right which is how I initially thought it would play out in the draft of wireframes.

### Surface

 -  #### Colour Scheme
    
    
    ![image showing color scheme](/media/readme/db.png)
        
-   #### Typography
         
    Used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site. Specifically the 'Bebas Neue' font used throughout.
      
-   #### Imagery
    The images I've chosen were taken from Charli Xcx's current website and RedBubble. The news posts images were from the respective articles or performances, etc. I tried to pick the styles and images that coincide with the release of the new album and focus on promotion of that while also enhancing the style of the website. 

-   #### Design Choices

    
## Technologies 

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

1. [Bootstrap v4.6.0](https://getbootstrap.com/docs/4.6.0/getting-started/introduction/)
    - Bootstrap was used for the initial layout and styling before customising it.
2. [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the Tangerine and Gentium Book Basic. 
3. [Font Awesome](https://fontawesome.com/)
    - The icons used throughout.
4. [Git](https://git-scm.com/)
    - Version control.
5. [GitHub](https://github.com/)
    - For storing project.
6. [Gitpod](https://www.gitpod.io/)
    - Used for editing my code.
7. [Balsamiq](https://balsamiq.com/)
    - Wireframe creation
8. [Am I responsive](http://ami.responsivedesign.is/)
    - This was used to generate the image at the top of this README.
9. [Chrome devtools](https://developer.chrome.com/docs/devtools/)
    - This was used massively throughout development to troubleshoot, try out changes before 
   changing code, to test responsiveness and for testing performance of the final site with lighthouse. 
10. [jQuery](https://jquery.com/)
    - Required for some of the bootstrap elements such as collapsibles, modal and tooltips.
11. [Heroku](https://dashboard.heroku.com/apps)
    - For deploying the application
12. [Postgres](https://www.postgresql.org/)
    - Database used for our data
13. [Django](https://www.djangoproject.com/)
    - Framework for building applications.
14. [Stripe](https://stripe.com/gb)
    - Used for our online payment system
15. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    - Used to generate secret key
16. [GraphizOnline](https://dreampuf.github.io/GraphvizOnline/)
    - Used to create the database schema.
17. [convertingcolors.com](https://convertingcolors.com/color-bucket.html)
    - For making my colour palette picture

## Challenges 


## Testing

Testing and results can be found [here](TESTING.md)

## Deployment

 - ### Creation 

    I created this repository by:<br>
    (a) Logging into Github and clicked the green new button.<br>
    (b) This took me to the page below. I selected the code institute template, input a repository name and clicked the green create repository button.<br>

    ![image showing green new button]()
    ![Image showing the create repository page]()

    (c) Opened new repository and clicked green Gitpod button to create a workspace in Gitpod for editing.

  - ### Forking
    (a) To fork my project sign in to Github and go to my [repository]()<br>
    (b) Above and to the right of the settings there are three options and the far right one says Fork, select this.<br>
    (c) The fork is now in your repositories.

    ![Image showing fork button]()

  - ### Clone
    To clone my project sign in to Github and go to my [repository](https://github.com/natalie-kate/music_to_my_ears)<br>
    See [Setting Up Stripe](#setting-up-stripe), [Setting Up Project](#setting-up-app), [Cloudinary]()
    and [Heroku Deployment](#heroku-deploment) for more information about what will be required to run Music to my ears.

    *  Clone using command line 
        +  Next to the green Gitpod button is a button that says code, select this. There is a few options as to how you 
        would like to clone, if you choose https, SSH or Github CLI, select the clipboard icon to copy the URL.
        +  In your workspace that you've created, in the terminal , type git clone, paste the URL and enter.

        ![Image showing the cloning options](docs/readme-assets/readme-images/clone.png)

    *  Desktop Github
        + If you choose to clone by selecting open with desktop Github, it will guide you through the clone with prompts.<br>

    For more information or troubleshooting see the Github documentation 
    [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)

- ### Setting Up Project
   
    - Install requirements in terminal using pip3 install, see requirements below. If you have cloned my project you can use   pip3 install -r requirements.txt which will install everything for you.
    
      ![Image showing the requirements]()

    - Create a SECRET_KEY for django to use. I used [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) for this. My settings.py file is set up to collect keys from the environment so name your variables accordingly. In github you go into settings from your dashboard and then variables. And add the following. You can complete the rest when you go through these sections. DEVELOPMENT value is set to True. Scope you can set to your repository name meaning its only accessible by that project or you can set it to */* meaning all your repositories can access them. 

        ![Image showing the github variable set up]()

    - Ensure you have requirements.txt file and Procfile. These are required by Heroku so ensure these are pushed to github prior to deployment. Ensure all requirements are saved by using pip3 freeze > requirements.txt

    - If using in development you will need to Run migrations usimg command python3 manage.py makemigrations and then python3 manage.py migrate. To create a superuser in the terminal to get access to admin panel, use command python3 manage.py createsuperuser and fill in details required.


- ### Setting up Stripe
    - Register with stripe [here](https://stripe.com/gb) if you don't already have an account. Didn't activate account as will be using free tier.
    - In dashboard from main menu and then select developers and then API keys. Here you will get the publishable and secret keys. These shouldn't go into version control so add them as variables in your github environment for development and in Config Vars in Heroku if you are deploying this project. 

        ![Image showing the Developer menu]()

    - We are also using webhooks in this project and so below API keys in the menu there is a Webhooks option, click into it and then select add endpoint.

        ![Image showing add endpoint button]()
    
    - You'll be asked for a url, this is your github workspace url with /checkout/wh/ added onto the end. When you deploy to Heroko you'll want to create an endpoint for it also, again with the /checkout/wh/ at the end. You then need to select events you want webhooks for. You can select all events but we only really need payment_intent.succeeded and payment_intent.payment_failed. as this is what we have wrote webhandlers for. Select Add Events and then Add Endpoint.

        ![Image showing add endpoint url]()
        ![Image showing add webhook events]()

    - Now in your new webhook, reveal Signing secret, copy this and this is the value for the STRIPE_WH_SECRET variable in your github settings. When you make a new endpoint for Heroku you will get a another Signing Secret to use.

        ![Image showing Reveal signing secret link]()


- ### Heroku deployment
    - Log in to Heroku, click 'New' and select 'Create New App'. In window give the app a name and choose region closest to you and then click 'Create App'. Then in Resources under Add-ons, select Heroku Postgres.

       ![Image showing the Heroku menu]()
       ![Image showing the Add-on section]()

    - In new app page select settings from menu, click reveal config vars and complete the following, see Stripe and AWS sections for where to get their secret key values. DATABASE_URL will have been pre-filled when you selected Postgres. USE_AWS value is True for when we have set up AWS. SECRET_KEY was generated as before with Django Secret Key generator.
      
      ![Image showing the config vars required]()

    - Next select 'Deploy' from menu, three options of deployment are available. If you select Heroku Git, it gives you step by step of what you need to do.

      ![Image showing the deployment options]()

    - I chose to use Github, so you have to search and connect to your github repository. 
    
    - Click enable automatic deployment, below that in manual deploy section, you can pick and deploy a branch to ensure everything is set up correctly. 

      ![Image showing manual deployment]()
    
    - You will now need to migrate and create superuser as above in Setting Up Project section.

## Credits

### Code

-   Code Institutes walk through project [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546)
-   [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library used for the layout and styling and modals.

### Content

-   Content was created by Natalie Alexander.
    
-   README and TESTING layout and content from my MS1 which took inspirations and ideas from these excellent examples
    * [Code institute](https://github.com/Code-Institute-Solutions/SampleREADME)

### Media
-   Most of the product images were taken of my own collection and a friends who very kindly sent them to me.

-   Some images and info were from wikipedia as I wanted to showcase more than two genres which seemed to be the majority of the products we had.

-   * [CharliXCX](https://charlixcx.com/): Index/home banner image. And Merchandise items. 
    * [Red Bubble](https://www.redbubble.com/shop/?query=charli%20xcx&ref=search_box): More Merchandise items from here as well. 

 
### Acknowledgements

-   Code Institute for Boutique Ado walk through project and automated testing course material. Used the videos quite bit to get me started.
-   My mentor Matthew Rudge for his time and feedback.
-   The slack community.
