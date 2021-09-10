# SODA_hackathon_team_12 project


# Information Architecture


### Database choice

[MongoDB]() is a NoSQL, document-based database which groups data as key-value pairs within documents grouped into collections. MongoDB excels at storing and providing access to unstructured data at scale. 

### Database collections structure

#### Employees collection

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


#### Disability category collection

Collection name: disability_categories

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | `ObjectId` | Primary Key, unique, not null |
| Name | disability_category_name | `text`, `maxlength=100`, `required` | `String` | not null, unique |


#### Disabilities collection

Collection name: disabilities

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | `ObjectId` | Primary Key, unique, not null |
| Name | disability_name | text, `maxlength=100`, `required` | `String` | not null, unique |
| Category ID | disability_category_id | None | `ObjectId` | ref: > disability_types._id |
| Provisions IDs | disability_provisions_ids | None | `Array` | Array of ObjectIds ref: > provisions._id |


#### Provisions collection

Collection name: provisions

| Title | Key in DB | Validation | Data Type | Details |
| --- | --- | --- | --- | --- |
| ID | _id | None | ObjectId | Primary Key, unique, not null |
| Name | provision_name | text, `maxlength=50`, `required` | string | not null |
| Description | provision_description | `maxlength=5000`, `required` | string | not null  |


