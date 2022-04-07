# Charli XCX - Merchandise

Here is a link to the live project. (https://charlixcx-merch.herokuapp.com/)

This website was created for Milestone 4 

![Image showing the website displayed on different screen sizes](/media/readme/responsive.png)

![link to testing.md](TESTING.md)

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
   * [Setting up Cloudinary](#setting-up-cloudinary)
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
        1. As superuser, I want to be able to add or edit merchandise.
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

-   Able to search for specific merchandise.

-   Able to read news posts and navigate to it.

-   'Back to top' footer link on the merchandise page, saves users from having to scroll up to Nav bar especially on mobile devices.

-   Logged in users can like a news post and it will be saved to their profile.

-   Logged in user can save their addresses and default address, pre-fills Checkout form

-   User can edit their own profile information

-   Admin users can add, edit and delete any merchandise. 

-   Admin can reduce or replenish the limited stock items.

-   Limited products can only be purchased once per order.

-   Limited products will show that there is 'limited stock' on merchandise page.

-   When product stock quantity is 0, add to cart buttons are not available and will display 'Out of Stock'.

-   Confirmation email on registration and on successful purchase.

-   Users can click on the heart button and it will be saved to their profile as news posts they loved so they can go back to them.

-   Users can donate 1€ to help Ukrainan refugees on the shopping page.

   #### Features to implement in the future

-  Add a wishlist on users profile that the can add products to.
-  Add a subscription newsletter users could sign up for
-  Include multiple images per product if needed
-  Include (filtered)comments on news posts
-  Make it easier to 'return' merchandise
-  On Add Merchandise that you can preview properly the merchandise image before upload

### Structure

-   Created a database schema using [GraphizOnline](https://dreampuf.github.io/GraphvizOnline/), as per Emmets     instructions on [slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1642276160282900) see [here](/media/readme/db.png) to view it better.

    ![image showing db scheme](/media/readme/db.png)


### Skeleton 

Wireframes were created on Balsamiq (see links below)

* [Mobile](/media/readme/mobilewf.png)
* [Tablet](/media/readme/tabletwf.png)
* [Desktop](/media/readme/desktopwf.png)

The finished project does differ a bit from the wireframes. There are less merchandise products per row on the page on tablet or mobile and I've changed the footer to better match the useful links. Also, on the profile page there is now the added functionality of seeing which news posts you like and going back to them. And on the news page, it is now more centered than left/right which is how I initially thought it would play out in the draft of wireframes. But I found that a centered design looked cleaner.

### Surface

 -  #### Colour Scheme
    Picked these colors from inspiration of Charli Xcx's own website. Her website is mostly black and white but I've added the hot pink to add that bright and sleek feel.

    ![image showing color scheme](/media/readme/colors.png)
        
-   #### Typography
         
    Used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site. Specifically the 'Bebas Neue' font used throughout.
      
-   #### Imagery
    The images I've chosen were taken from Charli Xcx's current website and RedBubble. The news posts images were from the respective articles or performances, etc. I tried to pick the styles and images that coincide with the release of the new album and focus on promotion of that while also enhancing the style of the website. The aim was for a 'sleek' and 'bright' design.

-   #### Design Choices
    I chose to merge the [CharliXcx](https://charlixcx.com/) website and the Boutique Ado project together and put necessary touches to bridge the gaps. Some of the structure in the merchandise is inspired from Boutique Ado but more fitting fonts and colours to match the artists profile.
    The text banner is on every page to really highlight the limited edition vinyl on display. It will display on each page but when it becomes out of stock the customer is not able to buy it anymore. 
    The news is styled similarly to a blog and more minimal so that the customer can focus on the content.

    
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
    - Google fonts were used to import the 'Bebas Neue' font. 
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
9. [Firefox inspect](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/open_the_inspector/index.html/)
    - This was used massively throughout development to troubleshoot, try out changes before 
   changing code, to test responsiveness and for testing performance. 
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
17. [coolors.com](https://coolors.com/)
    - For helping choose the right color of pink and how it matched with white and black.
18. [Cloudinary](https://cloudinary.com/)
    - For storing all the photos uploaded onto the site.

## Challenges 
Here are some of the issues I've encountered while writing this project.

-   Styling the AllAuth templates were more difficult than first thought. While most look like buttons, they range from buttons, inputs, links and input tags. And I wanted to change their initial style of black to pink and have it maintain that throughout site. That was more difficult than thought but besides one a tag on the sign out page there shouldn't be any changed in color that are very drastic.
    
-   Trying to create categories for news posts, which the user can click on as filters(similar to how its done in the Merchandise), was difficult. This is due to the difficulties of accessing the request method in a Django generic view. A lot of developers seem to have the same issue, but we were able to override the get_queryset method to achieve this.

-   I had trouble fully understanding how to link in django with the templating. But thankfully with the help of a mentor I was able to link up the site between different Django apps. 

-   Also I had the problem of Webhooks kept failing. When getting the information from the webhook I'd used my names and not theres, for instance county instead of state, town_or_city instead of just city, etc. The solution: Update to stripes field names to extract data from webhook.

-   Had issues with deploying properly to Heroku. I apparently had a space at the end of one of the Config vars but it took me a while before I figured that out. 

-   Had issues with the local images display so moved them onto Cloudinary and call them on the base.html in the script for css.

-   Depending on the browser for the user the banner image on index.html could be formatted slightly odd.


## Testing

Testing and results can be found [here](TESTING.md)

## Deployment

 - ### Creation 

    I created this repository by:<br>
    (a) Logging into Github and clicked the green new button.<br>
    (b) This took me to the page below. I selected the Code Institute template, input a repository name and clicked the green create repository button.<br>

    ![Image showing the create repository page](/media/readme/newtemplate.png)

    (c) Opened new repository and clicked green Gitpod button to create a workspace in Gitpod for editing.

  - ### Forking
    (a) To fork my project sign in to Github and go to my [repository]()<br>
    (b) Above and to the right of the settings there are three options and the far right one says Fork, select this.<br>
    (c) The fork is now in your repositories.

    ![Image showing fork button](/media/readme/fork.png)

  - ### Clone
    To clone my project sign in to Github and go to my [repository]()<br>
    See [Setting Up Stripe](#setting-up-stripe), [Setting Up Project](#setting-up-app), [Cloudinary]()
    and [Heroku Deployment](#heroku-deploment) for more information about what will be required to run Music to my ears.

    *  Clone using command line 
        +  Next to the green Gitpod button is a button that says code, select this. There is a few options as to how you 
        would like to clone, if you choose https, SSH or Github CLI, select the clipboard icon to copy the URL.
        +  In your workspace that you've created, in the terminal , type git clone, paste the URL and enter.

    *  Desktop Github
        + If you choose to clone by selecting open with desktop Github, it will guide you through the clone with prompts.<br>

    For more information or troubleshooting see the Github documentation 
    [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)

- ### Setting Up Project
   
    - Install requirements in terminal using pip3 install, see requirements below. If you have cloned my project you can use   pip3 install -r requirements.txt which will install everything for you.
    
      ![Image showing the requirements](/media/readme/requirements.png)

    - Create a SECRET_KEY for django to use. I used [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) for this. My settings.py file is set up to collect keys from the environment so name your variables accordingly. In github you go into settings from your dashboard and then variables. And add the following. You can complete the rest when you go through these sections. DEVELOPMENT value is set to True. Scope you can set to your repository name meaning its only accessible by that project or you can set it to */* meaning all your repositories can access them. 

    - Ensure you have requirements.txt file and Procfile. These are required by Heroku so ensure these are pushed to github prior to deployment. Ensure all requirements are saved by using pip3 freeze > requirements.txt

    - If using in development you will need to Run migrations usimg command python3 manage.py makemigrations and then python3 manage.py migrate. To create a superuser in the terminal to get access to admin panel, use command python3 manage.py createsuperuser and fill in details required.

    - ### Heroku deployment
    - Log in to Heroku, click 'New' and select 'Create New App'. In window give the app a name and choose region closest to you and then click 'Create App'. Then in Resources under Add-ons, select Heroku Postgres.

    - In new app page select settings from menu, click reveal config vars and complete the following, see Stripe and AWS sections for where to get their secret key values. DATABASE_URL will have been pre-filled when you selected Postgres. USE_AWS value is True for when we have set up AWS. SECRET_KEY was generated as before with Django Secret Key generator.
      
      ![Image showing the config vars required](/media/readme/configvars.png)

    - Next select 'Deploy' from menu, three options of deployment are available. If you select Heroku Git, it gives you step by step of what you need to do.

    - I chose to use Github, so you have to search and connect to your github repository. 
    
    - Click enable automatic deployment, below that in manual deploy section, you can pick and deploy a branch to ensure everything is set up correctly. 
    
    - You will now need to migrate and create superuser as above in Setting Up Project section.

    - Circle back to Heroku after setting up Cloudinary and Stripe and add the necesssary values to the Config Vars once completed. 


    - ### Setting up Cloudinary
    - Register with Cloudinary [here](https://cloudinary.com/) click on the copy to clipboard  link next to API environment variable we use this to connect our app to Cloudinary. 

    - Now we can go back to our ide and in our env.py file, we'll add another line at the bottom. “os.environ”.

    - We’ll set the CLOUDINARY_URL, and then we can paste in the value that we just copied. We still need to remove  "CLOUDINARY_URL ="    from the beginning, and then we'll copy this value again, so that we can paste it into Heroku as well.

    - So back to our Heroku dashboard we'll add a new config variable the same name CLOUDINARY_URL. And we'll paste in the value that we just copied. Now we also just need to add in one more temporary environment variable too, which is "disable_collect static".

    - Back in our settings.py file, go to the installed apps section and add in the  Cloudinary libraries that we installed before. So "cloudinary_storage" and this needs to go just above "django.contrib.staticfiles" and then the regular Cloudinary library can go underneath.

    ![Image showing the Setting.py](/media/readme/installedapps.png)

    - "STATICFILES_STORAGE" and in here we can tell it to use, "Cloudinary_storage.storage.StaticHashedCloudinaryStorage", so this is coming from the  library that we installed above, and put into our installed apps section. We also need to set our static files directories,   this is going to be a list but it's only going  to contain one item which is "os.path.join" our base directory which is defined  at the top of our settings py file, and we're going to connect that to static and we'll create our static direct

         ![Image showing the Setting.py](/media/readme/cloudinarysettings.png)

    - Then we're just going to set static route. So "os.path.join" base dir static files. We can do very similar now for the media.  Now our media is pictures, things like that, our  static files will be our CSS and our JavaScript. So again, we'll set a media URL and  we'll set the default file storage to  "Cloudinary_storage.storage.MediaCloudinaryStorage".

    - We also need to tell Django  where our templates will be stored. So back up to the top of settings.py and under the  base directory let's add in a templates directory. "TEMPLATES_DIR =  os.path.join(BASE_DIR, 'templates')" And now we just need to scroll down midway in  our settings.py file and change the D-I-R-S key, the dirs key, in our template setting to point  towards our new templates directory variable.

    - And that's pretty much it for setting up with Cloudinary!



## Credits
-   Code Institutes walk through project [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546)
-   [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library used for the layout and styling and modals.
-   [TechStacker](https://techstacker.com/how-to-responsive-youtube-videos/)
-   [Django Docs](https://docs.djangoproject.com/): Helped get the merchandise properly rendering with the limited function. 
-   [30SecondsofCode](https://www.30secondsofcode.org/css/s/hover-underline-animation): Helped get the hover animation over the nav bar.
-   [Stackoverflow](https://www.stackoverflow.com): Helped get the liked post functionality onto the Profile.
-   [DjangoBlog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/?child=last): I watched the first few videos to help me establish a starting point for the news pages.

### Code

-   Code Institutes walk through project [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546)
-   [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library used for the layout and styling and modals.

### Content

-   Content was created by Lane Sawyer Thompson.
    
-   README and TESTING layout and content from my MS1 which took inspirations and ideas from these excellent examples
    * [Code institute](https://github.com/Code-Institute-Solutions/SampleREADME)

### Media
-   Most of the product images were taken from [Charli Xcx](https://charlixcx.com/) and [RedBubble](redbubble.com) and news photos have their sources below on each post.

-   * [CharliXCX](https://charlixcx.com/): Index/home banner image. And Merchandise items. 
    * [Red Bubble](https://www.redbubble.com/shop/?query=charli%20xcx&ref=search_box): More Merchandise items from here as well. 
    * Any images on the news site has where its from sourced below each post as well.

 
### Acknowledgements

-   Code Institute for Boutique Ado walk through project and automated testing course material. Used the videos quite bit to get me started.
-   My mentor Matthew Rudge for his time and feedback.
-   The slack community.
-   Friends who tested the website and let me know when errors occured. 