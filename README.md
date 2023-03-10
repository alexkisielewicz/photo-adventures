<h1 align="center">Photo Adventures Website - Full-Stack Toolkit Project</h1>

### Developer: Aleksander Kisielewicz

<b>[View live website here](https://photo-adventures.herokuapp.com/)</b> :computer:

![Program mockup](docs/img/responsive_mockup.png)

Photo Adventures Website was created as Portfolio Project #4 (Full-Stack Toolkit) for Diploma in Full Stack Software Development at [Code Institute](https://www.codeinstitute.net).

Project purpose was to build a full-stack site using agile methodology to plan and design web application using MVC framework and related contemporary technologies.

Application offers such functionalities as:
- **Secure user registration** Users can register with captcha protection and e-mail verification
- **Password reset via email** Users can easily reset their forgotten password with just a few clicks
- **Sign in/out** Users can conveniently sign in and out of their account
- **Role-based access** Access to functionalities is granted based on the user's assigned role
- **User dashboard** Users can view their own personalized dashboard, complete with user content
- **Post management** Users can view, add, edit, and delete their posts with ease (CRUD)
- **Saving drafts and publishing** Users can save their edited posts as drafts or publish them (send to modaration)
- **Moderation** Admins can moderate posts and comments
- **Commenting** Users can leave comments on posts and have their Gravatar user picture displayed
- **Liking** Users can add likes to posts to show their appreciation
- **Messages/feedbac** Users receive feedback and confirmation to their actions
- **Social media sharing:** Posts can be easily shared on Facebook and Twitter
- **Contact form:** Users can send messages to the admin through a contact form that includes captcha protection

# Table of content

*   [Project](#project)
    *   [Strategy/Scope](#strategyscope)
    *   [Site owner goals](#site-owner-goals)
    *   [External user's goal](#external-users-goal)
*   [User Experience (UX/UI)](#user-experience-ux)
    *   [Colour Scheme](#colour-scheme)
*   [Logic and features](#logic-and-features)
    *   [Python logic](#python-logic)
    *   [Database structure](#database-structure)
    *   [Features](#features)
        *   [Main menu](#main-menu)
        *   [Add book](#add-book)
        *   [Edit book](#edit-book)
        *   [Remove book](#remove-book)
        *   [View all books](#view-all-books)
        *   [Change sorting method](#change-sorting-method)
        *   [Show book details](#show-book-details)
        *   [Quit](#quit)
*   [Technology](#technology)
    *   [Software used](#software-used)
    *   [Python libraries/modules](#python-librariesmodules)
*   [Testing](#testing)
    *   [Accessibility](#accessibility)
    *   [Validation](#validation)
    *   [Manual testing](#manual-testing)
    *   [Bugs/known issues](#bugsknown-issues)
*   [Deployment](#deployment)
    *   [Git and GitHub](#git-and-github)
    *   [Deployment to Heroku](#deployment-to-heroku)
*   [Possible future development](#possible-future-development)
*   [Credits](#credits)
    *   [Code](#code)
    *   [Media](#media)
    *   [Acknowledgements](#acknowledgements)

#   Project
##  Strategy/Scope

I chose to develop an web application that can be used in real life. My main focus was always on providing an excellent user experience, which is why I decided to create a web application that is both practical and engaging. Photo Adventures is a user-friendly blog-style website where users can share their photo adventures by creating visually appealing blog posts that include both images and text.
Application should have clean and intuitive user interface and offer easy access and navigation to all functionalities. Application should also be responsive on devices of all screen sizes.

To achieve the strategy goals I implemented following features:

- a clean and intuitive user interface for ease of navigation and readability,
- a menu that provides easy access to all website sections, including personalized content via user dashboard,
- cloud hosting of images for optimized website speed and user experience,
- media queries to ensure responsiveness across all types of devices,
- feedback to users for all actions taken on the website.

![Agile](docs/img/agile.png)

## Site owner goals

##  External user's goal

#   User Experience (UX)

##  Colour Scheme

Colour palette was selected using <b>coolors.co</b> generator. 

![Colour Scheme](docs/img/design_palette.png)

# Logic and features

## Python Logic

## Database structure

## Features

### Navbar and main menu

Default nabvar

![navbar-default](docs/img/navbar_default.png)

Nabar for authenticated user

![navbar-loggedin-user](docs/img/navbar_loggedin_user.png)

Navbar for admin user

![navbar-admin](docs/img/navbar_admin.png)

Mobile navbar for medium screen devices

![navbar-mobile1](docs/img/navbar_mobile1.png)

Mobile navbar for small screen devices

![navbar-mobile2](docs/img/navbar_mobile2.png)

### Footer

![footer](docs/img/footer.png)

### Index page / Carousel

![index-carousel](docs/img/index_carousel.png)

![index-hero](docs/img/hero.png)

![index-counters](docs/img/counters.png)

![index-most-liked](docs/img/most_liked_posts.png)

### Blog

![blog](docs/img/blog.png)

![blog](docs/img/blog_tags.png)

### Full Post

![full_post1](docs/img/full_post1.png)

![full_post2](docs/img/full_post2.png)

![full_post3](docs/img/comments.png)

![full_post3](docs/img/full_post_guidelines.png)

### About Page

![about1](docs/img/about_top.png)

![about2](docs/img/about_faq.png)

### Contact Page

![contact1](docs/img/contact.png)

### Admin Panel

![admin](docs/img/admin_posts.png)

### User Dashboard

![dashboard1](docs/img/dashboard_top.png)

![dashboard2](docs/img/dashboard_drafts.png)

![dashboard3](docs/img/dashboard_awaiting.png)

![dashboard1](docs/img/dashboard_published.png)

![dashboard1](docs/img/dashboard_delete.png)

### Accounts Templates

![accounts1](docs/img/accounts_signup.png)

![accounts1](docs/img/accounts_signup_captcha.png)

![accounts1](docs/img/accounts_email_account_exists.png)

![accounts1](docs/img/accounts_verify_email.png)

![accounts1](docs/img/accounts_email_confirm.png)

![accounts1](docs/img/accoints_bad_token.png)

![accounts1](docs/img/accounts_confirm_email.png)

![accounts1](docs/img/accounts_signin.png)

![accounts1](docs/img/accounts_password_reset.png)

![accounts1](docs/img/accounts_password_reset_sent.png)

![accounts1](docs/img/accounts_password_reset_email.png)

![accounts1](docs/img/accounts_change_password.png)

![accounts1](docs/img/accounts_change_password_confirmation.png)

#   Technology
    
##  Languages used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5) - markup language used for structuring webpage content
-   [CSS3](https://en.wikipedia.org/wiki/CSS) - stylesheet language
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - high-level, imperative, programming language.
-   [Python](https://www.python.org/) - high-level, imperative, general-purpose programming language.
-   [Markdown](https://en.wikipedia.org/wiki/Markdown) - markup language used to write README and TESTING documents.

##  Software used
- [Bootstrap5](https://blog.getbootstrap.com/2022/11/22/bootstrap-5-2-3/) - CSS framework developed by Twitter. 
- [Cloudinary](https://cloudinary.com/) - cloude-based image and video API
- [Django](https://www.djangoproject.com/) - python-based web framework with MTV architectural pattern.
- [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) - web template engine for python/django apps
- [Coolors.co](https://coolors.co/) - was used to create colour palette for terminal display page.
- [Favicon.io](https://www.favicon.io) - tool used to create favicon.
- [Font Awesome:](https://fontawesome.com/) - Font Awesome icons were used for social links in terminal display page.
- [Git](https://git-scm.com/) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) - GitHub is used to store the project's code after being pushed from Git.
- [Heroku](https://heroku.com) - online app used to deploy project.
- [Pexels.com](https://www.pexels.com/) - was used to source bacground picture for terminal display page.
- [WebAIM](https://webaim.org/resources/contrastchecker/) - online tool to check colour contrast/accesibility.
- [Gravatar](https://en.gravatar.com/)
- [EmailJS](https://www.emailjs.com/) - JavaScript library used to send emails usung only client-side technologies.
- [GoogleMaps](https://www.google.com/maps)
- [GooglereCaptchav2](https://developers.google.com/recaptcha/docs/display?hl=en)
- [Gmail](https://mail.google.com/)
- [Canva](https://www.canva.com/) - used to design logo picture
- [Convertio.io](https://convertio.co/) - used to convert images to webp format

##  Python libraries/modules

- [os](https://docs.python.org/3/library/os.html) - built-in pythod module - used to save and import env variables.
- [cloudinary](https://pypi.org/project/cloudinary/)
- [CrispyBootstrap5](https://pypi.org/project/crispy-bootstrap5/)
- [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/)
- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/)
- [django-allauth==0.52.0](https://pypi.org/project/django-allauth/) - integrated django accounts management
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
- [django-social-share](https://pypi.org/project/django-social-share/) - used for facebook and twitter share buttons
- [django-summernote](https://pypi.org/project/django-summernote/) - WYSIWYG editor widget used for writing/editing post content 
- [django-taggit](https://pypi.org/project/django-taggit/) - used for post categorizing by tag name
- [gunicorn](https://pypi.org/project/gunicorn/) - python WSGI HTTP Server for UNIX
- [oauthlib](https://pypi.org/project/oauthlib/) - 
- [psycopg2](https://pypi.org/project/psycopg2/) - 
- [PyJWT](https://pypi.org/project/PyJWT/)
- [pytz](https://pypi.org/project/pytz/) 
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuth library suppor for python requests
- [sqlparse](https://pypi.org/project/sqlparse/) - non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

#    Testing

##   Accessibility

[WebAIM](https://webaim.org/resources/contrastchecker/) online tool was used to check terminal colour contrast. All used colours passsed the test satisfactory.

![color1](docs/img/contrast1.png)

![color2](docs/img/contrast2.png)

![color3](docs/img/contrast4.png)

![color4](docs/img/contrast5.png)

## Validation

### PEP8

## Manual testing

Details of manual testing can be found in [TESTING.md file](link)

##   Bugs/known issues

- <b>Issue #1:</b> 

- <b>Solution:</b> Putting "break" instruction in the correct place, that allows to "escape" from the while loop.

- <b>Issue #2:</b> 

- <b>Solution:</b> 

#   Deployment

## Git and GitHub

## Deployment to Heroku

1. I visited [https://heroku.com/](https://heroku.com/) and opened dashboard. Then I clicked button "New" and selected "Create new app" button.

2. I entered my app name as "photo-adventures", chose region to Europe and clicked on "Create app" button

3. The next step was to go to "Deploy" tab and then to "Deployment method" section to authorize and connect my GitHub account.

4. Upon succesfull connection I selected main branch from "photo-adventures" repository.

5. Then I went to "Settings" tab...

6. In the next step I went to "Config Vars" section and added KEY "CREDS" - that maches my token name defined in python constant in [api/google_sheets_api.py](https://github.com/alexkisielewicz/home-library-app/blob/main/api/google_sheets_api.py) - with value of my credentials token (copy all and paste).

7. I added key "PORT" with value "8080" and save changes.

8. In the next step I went back to "Deploy" tab and decided to use automatic deploys, however manual mode is also available to deploy chosen branch.

9. The link to my deployed app was shown on screen: [https://photo-adventures.herokuapp.com/](https://photo-adventures.herokuapp.com/)

<br>

# Possible future development

If I had more time or decide to develop app further I would add/improve following functionalities: 

#   Credits

##  Code

##  Media

- [Photos Pawel Zygmunt](https://www.breakinglightpictures.com/) - thanks to my friend Pawel for 3 photos from Tenerife, Connemara and Dolomites.  
- [Alek Kisielewicz Photography](https://www.facebook.com/alex.perfect.photo) - all other post images are my own photographs.

- [Pexels.com](https://www.pexels.com) - post placeholder image/background image/accounts background

## Learning resources

- [Code Institute course and learning platform](https://codeinstitute.net/)
- [The book "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction To Programming"](https://nostarch.com/pythoncrashcourse2e)
- [StackOverflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/python/default.asp)
- [Django](https://www.djangoproject.com/) - Django documentation.
- [Bootstrap](https://blog.getbootstrap.com/2022/11/22/bootstrap-5-2-3/) - Bootstrap documentation.
- Documentation of python modules and libraries used in the project.

##  Acknowledgements

-   My Mentor Reuben Ferrante for helpful feedback and guidance at all stages of the project.
-   Code Institute Slack Community for being invaluable knowledge base.

## Disclaimer
-   Photo Adventures Website was created for educational purpose only. 