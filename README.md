
# Nature line

Nature line is webapp that represents a directory for local food producers and local food lovers that creates bridge for interaction between the two. Users can create their profile and display their productsa nd get contacted by buyers. Users can also search producers database and view their profile with products they sell.
It was created with Python and Flask microframework. I also used MongoDb as database for storing user data and Materialize and jQuery for styling the page.


*[Live site]()


### User stories

- AS A USER I want to register an account.

- AS A USER I want to search local farmers find products.

- AS A USER I want log in and log out with ease.

- AS A USER I want to be able to navigate myself around the site with ease.

- AS A FARMER I want to set up my profile with basic information about myself(location and contact info).

- AS A FARMER I want to display products on my profile page.

- AS A FARMER I want to edit my information.

- AS A FARMER I want to add, remove, edit and delete products.

## Design

### Colours

- **Background color** - I used #E5F8BF as overall background color in combination with svg illustrations.

- **Forms color** - I used #c0ca33 from Materialize color presets which works well with other colors and gives natural contrast.

- **Button colors** - I used #8e24aa from Materialize color presets which pops out on forms. Also, I used #e53935 for delete and reset button which reflects action on button(DELETE and RESET)

- **Profile colors** - I used #c0ca33 from Materialize color presets which works well with other colors and gives natural contrast.


### Fonts

- [**MuseoModerno**](https://fonts.google.com/specimen/MuseoModerno) - I used this font on landing page and around different views to give unfied feel for visitors.

- [**Monoton**](https://fonts.google.com/specimen/Monoton) - I used this font for logo text in navbar.

### Wireframes



## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) - This was used for the overall structure of the website.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This was used for the overall styling of elements on the website.

- [jQuery](https://jquery.com/)- This was used to initialize Materialize components.

- [Python](https://www.python.org/) - This was used for all the backend coding of the website.

- [Flask](https://palletsprojects.com/p/flask/) - The flask micro-framework was used to help with backend code and to help display site through Jinja templating language.

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja templating language used for writing html and rendering it with Python.

- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - Werkzeug is used for password hashing and securely retriving them.

- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - This was used to connect to the database, MongoDB.

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - This was used as the NoSQL database that stores all user data.

- [Materialize](https://materializecss.com/) - This was used to utilize responsiveness of site, also providing different components utilized across site.

- [Google Fonts](https://fonts.google.com/) - Used for fonts across site.

- [GitHub](https://github.com/) - It was used for version controll.

- [Heroku](https://www.heroku.com/) - I used Heroku to deploy the live version of my site.

- [Figma](https://www.figma.com/)** - used for mockup.

- [Visual Studio Code](https://code.visualstudio.com/) - used this to write the code for my site.

- [Font Awesome](https://fontawesome.com/) - Used for icons in footer.

## Features

### Existing Features

- **Registration Page**
    - This is where user can register account, add location and contact information

- **LogIn/Logout Feature**

    - this is where user is able login into their account
    - also, user can use logout link to logout

  - **Profile Features**
    
        - On profile page user can find button to update their information.

        - On profile page user can find button to add product.

        - On profile page user can find button to edit product.

        - On profile page user can find button to delete product.

        - On profile page user can diplay their products with price and quantity.

        - On profile page user can display their location and contact information.

- **Add product Feature**

        - Here user can add product which includes product category, price and quatity.

- **Edit product Feature**

        - Here user can edit their exisiting products with same data points as Add product feature.

- **Update info Feature**

        - Here user can update their information(location and contact info).

- **Delete product feature**

        - here user can delete product from database and remove it from their profile.

- **Search feature and display local farmers**

        - here user can search food produces by location and username.

        - this page also diplays all the profiles created on Nature Line.

### Features to be implemented at later date

- **Another type of account - buyer account**

        - Enables users to create buyer account where they can add favorite producers and rate food producers.

- **Upload profile picture**

        -Here user can uplaod their profile picture.

- **Upload product picture**

        -Here user can upload pictures of their products.

- **Rating system**

        - Add rating system to profile pages for users who have buyer account.

## Testing

* **Automated testing**

    * **[CSS Validator](http://jigsaw.w3.org/css-validator/)** - no errors.

    * **[HTML Validator](https://validator.w3.org/)** - gave no errors.

    * **[PEP8]**(http://pep8online.com) - gave error with white specaes before and after '='

* **Manual Testing**

    * **Desktop**
        
        * **Google Chome**: everything is working good. Page loads, and all of the page features are working.

        * **Mozilla Firefox**: everything is working good. Page loads, and all of the page features are working.
        

    * **Mobile**

        * **Mozilla Firefox Dev Tools**

            * tested with Firefox Dev tools for all available devices (from Moto G4 to iPad),
            webpage works well. It is responsive as intended, no weird page deformations.

        **Real-world testing:**

        * **Huawei P20Pro** - site loads good. It is responsive as intended. All of the features are working.

        * **Samsung Galaxy S9** - site loads good. It is responsive as intended. All of the features are working.

        * **Samsung Galaxy A5** - site loads good. It is responsive as intended. All of the features are working.

        * **Xiaomi mi 9t** - site loads good. It is responsive as intended. All of the features are working.


## Deployment

 **[GitHub](https://github.com/)** - is used to host code and files for this project. The project has only one branch(master). Deployed version is most current version of repository.

 **[Heroku](https://www.heroku.com/)** -  was used to deploy this site.

 **How to run this project locally**
 **To clone this project from GitHub:** 
([Source](https://github.com/Edb83/penny-for-your-thoughts/blob/master/README.md#testing))

* Under the repository name, click "Clone or download".
* In the Clone with HTTPs section, copy the clone URL for the repository.
* In your local IDE open Git Bash.
* Change the current working directory to the location where you want the cloned directory to be made.
* Type git clone, and then paste the URL you copied in Step 3.
* Press Enter. Your local clone will be created.

**Some Issues I ran into developing with VS Code:**
- if you need to run venv in terminal:
	- go to .venv/scripts/activate.ps1 to activate venv in terminal


- if you can't find your app running at host='0.0.0.0',port=5000

    * Run your app by using **python app.py**

    * Go to the window cmd. Type **ipconfig** and get the get the IPV4 adress

    * Go to the browser and type the 192.168.X.X:5000(your IPV4 adress)

**Heroku errors** Push failed: cannot parse Procfile(UTF encoding issue )

        - Open your current Procfile with notepad. 
        - Create a new Procfile.txt and paste the content of your original Procfile .
        - Save your Procfile and replace it with your Procfile removing .txt filetype


## Credits

### Idea

* I was inspired to create this webapp reading about blockchain and decentralized finance. I wanted to create community drive platform which can be distributed to different enviroments.

### Code

* I followed new lessons provided by amazing [Tim Nelson](https://github.com/TravelTimN) which help immensly with development.

* I used Flask, Jinja and Werzeug documentation.

* Also without Stackowerflow, W3schools and MDN this would be impossible.

**Media**

* Background image was taken from **[drawkit.io](https://www.drawkit.io/product/nature-ecology-illustrations)**.

* Farmer image and product image taken from **[flaticon](https://www.flaticon.com/)**

**Acknowledgements**

* I want to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for his guidance and help.

* Slack community of Code Institute for inspiration.

* My girlfriend and my friends on their support and help with testing.:kissing_heart: