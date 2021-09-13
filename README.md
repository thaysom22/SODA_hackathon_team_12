# SODA_hackathon_team_12 project README
## Table of Contents

1. [Introduction](#Introduction)

2. [User Experience](#User-Experience)
    - [User stories](#User-stories)
    - [Admin stories](#HR-stories)

3. [Design](#Design)
    - [Design and colors](#Design-and-colors)
    - [Wireframes](#Wireframes)
    - [Features](#Features)
    - [Information Architecture](#Information-Architecture)

4. [Technology Used](#Technology-Used)

5. [Testing](#Testing)

6. [Deployment](#Deployment)

7. [Credits](#Credits)

8. [Disclaimer](#Disclaimer)

[Back to Top](#table-of-contents)

## 1. Introduction

![Workability (https://github.com/[thaysom22]/[SODA_hackathon_team_12]/blob/[main]/image.jpg?raw=true)

[Back to Top](#table-of-contents)
##  2. User Experience
Modern apps should meet one of the most significant things which is UX. As developers, we need to think as our potential user, we should clearly describe the potential user, his/her needs and implement the best solutions, which will meet these criteria.
To do it as well as possible we assumed, that our potential users are:
Employee with different types of disabilities


### Employee with different types of disabilities
As user I would like to easily navigate through the whole app
As a user I want the application to be accessible to me via a realisable
I would like to read about the purpose of the page
Easily find section with most frequently asked questions
Create my own profile (future feature)
Get an info about that the account is successfully created (future feature)
Fill the form with my needs 
Send the form 
get confirmation about that the form is send (future feature)
### Human Resources Team needs (in further implementation)
As a HR team member, I would like to be able to easily navigate through the whole app
I would like to easily browse all employee records,
Search by provisions and considerations,
I also want to add/edit and delete some provisions and considerations.


### User stories

As a potential visitor (first time visitor) I would like to:
+ Easily navigate through the whole page,
    + return to home page when logo is clicked,
    + open desired subpages (login/home etc) in main nav,
    + open in new window all links inserted into the footer/navbar,

[Back to Top](#table-of-contents)

## 3. Design

### Design and colors

### Wireframes
[View Figma File](https://www.figma.com/file/AXzOgQx0EmB36cpDxdPCT4/Wireframes)

### Features
#### Global
#### Home page
### Information Architecture
#### Database choice

[MongoDB]() is a NoSQL, document-based database which groups data as key-value pairs within documents grouped into collections. MongoDB excels at storing and providing access to unstructured data at scale. MongoDB Atlas is the cloud hosted service used for this application.

#### Database collections structure

##### Employees collection

Collection name: employees

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | `ObjectId` | Primary Key, unique, not null |
| First Name | first_name | `text`, `maxlength=100`, `required` | `String` | not null  |
| Last Name | last_name | `text`, `maxlength=100`, `required` | `String` | not null  |
| Provisions IDs | provisions_ids | None | `Array` | Array of ObjectIds ref: > provisions._id |
| Other Information | other_info | `textarea`, `max_length=5000` | `String` | |

note:
* use a different key other than default ObjectId for employee id?
* include age, gender, job_title fields?


##### Workspace considerations collection

Collection name: ws_considerations

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | `ObjectId` | Primary Key, unique, not null |
| Name | name | `text`, `maxlength=100`, `required` | `String` | not null, unique |
| Description | desc | `textarea`, `maxlength=500`, `required` | string | not null |


##### Provisions collection

Collection name: provisions

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | ObjectId | Primary Key, unique, not null |
| Name | name | `text`, `maxlength=50`, `required` | `String` | not null |
| Short Description | short_desc | `textarea`, `maxlength=500`, `required` | `String` | not null |
| Long Description | long_desc | `textarea`, `maxlength=5000`, `required` | `String` | not null |
| Workspace consideration | ws_consideration | None | `ObjectId` | ref: > ws_considerations._id, not null |

[Back to Top](#table-of-contents)

## 4. Technologies Used

#### Languages

* HTML,
* CSS,
* JavaScript,
* Python,


#### Libraries, frameworks, tools

* Flask,
* Bootstrap
* jQuery
* pyMongo
## 5. Features
### Features
#### Global
##### Logo 
Was created in Freelogodesin.org and transformed into the SVG format in online-convert.com to allow us to change the colours just like we wanted and replace the font to be much more visible for people with distubed vision. The logo itself contains a monitor with a green confirmation tick in the centre and the monitor is in the centre of a circle. This clear imagery gives our users easy visual access to the homepage as the logo is also a link to the index.html.
##### Favicons
We used the new logo to quickly generate a favicon for our app. To do so we used the favicon.io
##### Navbar
The navbar is responsive and has a logo and a few pages, which are described below. We used the same pattern and colour palette to create the app much more readable for people with reduced degree of visibility. The navbar provides simple and clear navigation through the site's pages so users can quickly and easily access the relevant information. This structure and design is consistent throughout the site to ensure the highest quality User Experience possible.
##### Footer
The footer also is responsive and has the same colour as navbar to keep the consistency of the whole app. Here we have also included the copyright marks. The footer is consistent throughout all pages of our website and also includes a fun footnote saying “made with coffee (logo) and love (icon).
#### Home page
There users meet our app for the first time and are able to easily navigate through the whole app from here by using a lightly covered navigation bar which contains a Home, About and FAQ section link. 
Below the navigation bar we have outlayed our hero image as the Workability logo and title name as well as a short description of the purpose of the application “Get recommendations based on your needs to help you be more productive in the workplace.”.
Below this we have built a registration page to get started. Initially we thought of adding in email and password registration but thought the purpose of this app is to make the site as easy as possible so any user can access the relevant information by just entering the first and last name.
Beneath this we have an animated image of people on laptops at work and a final note underneath this to summarise the app developers ethos which sets the tone for the rest of the app. “There are many types of disabilities and not all of them are visible. As employers we need to consider how we can accommodate disabled employees and empower them to be productive whether they are in the office or working from home.”.
Finally the footer is below this and described as above.
#### About page
         This page describes the purpose of the app as well as Workabilities origin story and ethos. As part of       the about section it's important for us to be extremely clear as to the functions of Workability and what we set out to achieve. 
In order to deliver a strong and clear message about Workability we open this page with our Mission Statement “Workability is a global non-profit technology based organization established in 2021. The goal set out by Workability is to help all disabled people from all around the world to gain access to various forms of employers by bridging the gap between employee skill sets and employer needs.”. 
This message sets the tone for the remainder of the about section which is split in two halves.
The first half continues the above message to elaborate on how the employers have evolved and now encourage practical views towards disabled employees. 
At this point on the site we included another statement and image to highlight our stance on equality in the workplace. “True Inclusivity Requires an Accessible Workplace.”, this statement is supported by an image of a disabled man in a wheelchair.
Beneath this statement we have our closing section to the about page which summarises the goals, ethos and a footnote about the founders/ developers who created the application. 
#### FAQ page
This page gives users the answers for most commonly asked questions to save time and avoid unnecessary disruptions in the HR Team.  For any questions not answered on this page we have also provided a contact us page so users can send in direct queries.
When dealing with disabilities it is important to allow an open environment for questions where people can feel comfortable in asking legitimate questions about what requirements need to be met for certain disabilities. 
The tools and functions of the app clearly meet this criteria however at Workability we encourage employers to go the extra mile for all staff so providing some of the most common questions and answers is a great way to resolve any issues or questions as quickly as possible.
We outlined 6 of the most common questions the Workability app receives on a regular basis and actively encouraged those who did not get their question answered to contact us directly.
 


[Back to Top](#table-of-contents)

## 5. Testing

* As user I would like to easily navigate through the whole app
 we achieved that by clear and well thought out
* As a user I want the application to be accessible to me via a realisable
* I would like to read about the purpose of the page
* Easily find section with most frequently asked questions
* Create my own profile (future feature)
* Get an info about that the account is successfully created (future feature)
* Fill the form with my needs 
* Send the form 
* Get confirmation about that the form is send (future feature)
* All user stories above (except the marked as a future feature) working well. 


#### Browser Compatibility 
* Google Chrome
* Firefox
* Edge
* Safari
our app working fine in mentioned browser 

#### Responsiveness (add report from am I responsible?)

to check the app is responsive we used:
Dev Tools,
Am I responsive page

Lighthouse Report 
* Performance = 100%
* Accessibility = 97%
* Best Practices = 93%
 * SEO = 89%

Validations
To check the app we used:
[HTML Validator](https://validator.w3.org/)
[CSS](https://jigsaw.w3.org/css-validator/)
[JavaScript Validator](https://jshint.com/)
[Python Validator](http://pep8online.com/)
Mozzilla and Google Chrom Dev Tools
LightHouse report to improve the app
Grammar and spelling
Was made during the design process and after finishing the work.


#### User Stories


| Nr | Test          | Action | Test result |
| --- |:----------------|:--------------| :-----: |

### Browser Compatibility
* Google Chrome
* Firefox
* Edge
* Safari

### Responsiveness (add report from am I responsible?)

### Lighthouse Report

### Knowns Bugs

[Back to Top](#table-of-contents)

### Left to implement/ Future development


As this application is built for a developing and growing market of disbaled employers there were certain features we hope to implement in the future which we have outlined below:
* Currently we have an open login meaning anyone can get access to the information regardless of email/ password requirements. This would be one of the future goals for the app itself to ensure regular and return users.
* Alongside this we would also include email verification features so each user will automatically receive an email verifying their account has been made successfully.
* With the login feature we would also want to give the ability for users to change their password and recover their password should it be lost at any stage.
* A further future goal of the development of this project would be to include a networking forum that would allow users to provide feedback and advice from their own experiences which could benefit future employers/ disabled employees.
* As a final page on this site we wanted to input a direct contact poage to ensure a clear method of contacting Workability for advice, feedback or support. Due to the time constraints we decided not to input an additional page we found creating a Workability email address and providing the direct link and contact information would be more practical to implement and more practical for the users.
* HR Team Members - this part will be implemented in future.


## 6. Deployment



This project is stored on GitHub repository and hosted on Heroku.
### Github
To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into GitHub.
2. From the list of repositories on the screen, select thaysom22/SODA_hackathon_team_12
3. From the menu items near the top of the page, select Settings.
4. Scroll down to the GitHub Pages section.
5. Under Source click the drop-down menu labelled None and select Master Branch
6. On selecting Master Branch the page is automatically refreshed, the website is now deployed.
7. Scroll back down to the GitHub Pages section to retrieve the link to the deployed website.

#### Run this project locally (clone this project into Gitpod) you will need:

Create a Github account here
use the browser with extension for Gitpod Then follow these steps:
1. Install the Gitpod Browser Extensions for your browser
2. After installation, restart the browser
3. Log into Gitpod with your gitpod account.
4. Navigate to the Project GitHub repository
5. Click the green "Gitpod" button in the top right corner of the repository
6. This will trigger a new gitpod workspace to be created from the code in github where you can work locally.

#### Heroku
1. Create a new application using the Heroku dashboard.
2. Go to settings tab, and then click on "reval config vars" and add:
IP (0.0.0.0),
PORT (5000),
MongoDB Name,
MongoDB URI (URL with DB name and password)
3. Install Heroku via the console log using "npm install -g Heroku"
4. Log into Heroku via console using "heroku login" and follow on the screen instructions to log in.
5. Create a requirements.txt file using the " pip3 freeze > requirements.txt " command.
6. Create a Procfile (remember it does not have any extensions) using the " echo web: python app.py > Procfile " command.
7. Push your code into Github repository
8. Connect GitHub to Heroku to do that go to Heroku page in Deploy tab go to "App connected to GitHub" type your username in Github and the repository name (which you want to connect with Heroku)
9. In Deploy Tab go to Automatic deploys section and click "Enable Automatic Deploys"
10. To see deployed app click "'Open App" on the top of the page
11. In the Settings tab in the Domains section will be a link to your app.
12. 
#### Run project on GitPod
1. Select the Repository from the GitHub Dashboard
2. Click the green button labelled 'GitPod'
3. Install the necessary libraries specified in the requirements.txt
4. Set your environment variables by creating and adding them into a env.py file as shown below:
os.environ.setdefault("SECRET_KEY", <SECRET_KEY>) 
os.environ.setdefault("MONGO_URI", "mongodb+srv://workability:LhrKOPR9FAwIBgrS@cluster0.pcrpf.mongodb.net/main?retryWrites=true&w=majority") ) 
os.environ.setdefault("MONGO_DBNAME", )

##### Remember to replace the content inside <>

1. Create a  .gitignore file in the root directory and add the env.py file to avoid it being pushed to GitHub
2. Import the env.py file into the app.py file.
3. Run the application.


[Back to Top](#table-of-contents)

## 7. Credits

### Code
we wanted create our own solutions, but some inspitations are in resources.md file
Content (here is the link to the resources file)
### Media
#### Images and icons
The illustrations are from [unDraw](https://undraw.co/) and some of the icons are from [Heroicons](https://heroicons.com/) and [Iconmonstr](https://iconmonstr.com/) respectively.
### Acknowledgements 
We would like to thanks:
Code Institute, Soda and  Ecosia for an opportunity to be a part that great hackathon family and for new great experience,
ourselves for an extraordinary team work,
and finally our families for understanding and support :)
 
### Content
[Resources](/research.md)
### Media
- Images
### Acknowledgements
[Back to Top](#table-of-contents)

## 8. Disclaimer
This project was created by young coders from Code Institute during the Trust in SODA Hackathon, which took place 9 – 13 September 2021. 
Our [CTIS12 Team]( https://hackathon.codeinstitute.net/teams/95/)
The project is not a live company however we hope the information and tools made available on the application will be beneficial to employers and disabled employees.
Thank you for visiting our project :)
Sean Young,
Thomas Hayson,
Arland Torres,
Magdalena Ruszaj,
Vincent Brown

[Back to Top](#table-of-contents)
