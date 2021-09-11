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

[Back to Top](#table-of-contents)
##  2. User Experience
User experience is one of the most significant things when building a webpage. To do this properly, you should consider:
* who is your target audience,
* what they want to achieve by visiting your page, 
* which features will meet their expectations.

In this case, potential customers are:

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
| Workspace consideration | ws_consideration | None | `ObjectId` | ref: > provisions._id, not null |

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


[Back to Top](#table-of-contents)

## 5. Testing

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

## 6. Deployment

[Back to Top](#table-of-contents)

## 7. Credits
### Code
### Content
[Resources](/research.md)
### Media
- Images
### Acknowledgements
[Back to Top](#table-of-contents)

## 8. Disclaimer

[Back to Top](#table-of-contents)
