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

[MongoDB]() is a NoSQL, document-based database which groups data as key-value pairs within documents grouped into collections. MongoDB excels at storing and providing access to unstructured data at scale. 

#### Database collections structure

##### Employees collection

Collection name: employees

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | `ObjectId` | Primary Key, unique, not null |
| First Name | employee_first_name | `text`, `maxlength=100`, `required` | `String` | not null  |
| Last Name | employee_last_name | `text`, `maxlength=100`, `required` | `String` | not null  |
| Disabilities IDs | employee_disabilities_ids | None | `Array` | Array of ObjectIds ref: > disabilities._id |
| Provisions IDs | employee_provisions_ids | None | `Array` | Array of ObjectIds ref: > provisions._id |

note: 
* use a different key other than default ObjectId for employee id? 
* include age, gender, job_title fields?


##### Disability category collection

Collection name: disability_categories

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | `ObjectId` | Primary Key, unique, not null |
| Name | disability_category_name | `text`, `maxlength=100`, `required` | `String` | not null, unique |


##### Disabilities collection

Collection name: disabilities

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | `ObjectId` | Primary Key, unique, not null |
| Name | disability_name | text, `maxlength=100`, `required` | `String` | not null, unique |
| Category ID | disability_category_id | None | `ObjectId` | ref: > disability_types._id |
| Provisions IDs | disability_provisions_ids | None | `Array` | Array of ObjectIds ref: > provisions._id |


##### Provisions collection

Collection name: provisions

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | ObjectId | Primary Key, unique, not null |
| Name | provision_name | text, `maxlength=50`, `required` | string | not null |
| Description | provision_description | `maxlength=5000`, `required` | string | not null  |


[Back to Top](#table-of-contents)
## 4. Technologies Used

* HTML, 
* CSS, 
* JavaScript, 
* Python,

#### Libraries, frameworks, tools used
* Flask,

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
