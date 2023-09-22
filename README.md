# Y - API
## Made with Django Rest

## Table of Contents
1. [INTRODUCTION](#introduction)
2. [DESIGN](#design)
    - [Development Planes](#development-planes)
        - [Strategy](#strategy)
            - User Stories
        - [Scope](#scope)
            - Project aims/Learning Outcomes
        - [Structure](#structure)
            - Database Model
            - Database Schema
        - [Skeleton](#skeleton)
    
3. [DEVELOPMENT](#development)
    - Agile Principles overview
    - Milestone 1
    - Milestone 2
    - Milestone 3
    - Milestone 4
    - Milestone 5
    - Milestone 6

3. [FEATURES](#features)
- [Design Features](#design-features)
- [Features to Implement in Future](#features-to-implement-in-future)

4. [BUGS](#bugs)
- [Resolved Bugs](#resolved-bugs)
- [Unresolved Bugs](#unresolved-bugs)

5. [TECHNOLOGIES](#technologies)
- [Languages Used](#languages-used)
- [Frameworks](#frameworks--libraries--programs)
- [Libraries](#frameworks--libraries--programs)
- [Programs](#frameworks--libraries--programs)

6. [TESTING](testing.md)

Contained as a seperate document [here](testing.md)

7. [DEPLOYMENT](#deployment)

Step-by-step guide on how to deploy

8. [CREDITS](#credits)

9. [ACKNOWLEDGEMENTS](#acknolwedgments)

___

# Introduction

"Y" is a satirical copy of a recently rebranded social media site. The site will allow users to post public questions or images, and ask the opinions of other authenticated users. Users can then vote on their favourite response. The response with the most votes will be deemed the "Right answer"

This project houses the API for the front-end of the site developed in react. [check out the front-end repo here](https://github.com/Cal-Rex/y-react-milestone-project-5)

<br />

___

# Design
## Development Planes

### <ins>Strategy</ins>

#### User Stories

The following user stories were ascertained for the project as a whole:

**Navigation**
- _As a user, i want to be able to a navigate every page with a central navigation feature_
- _As a user, i want to be prompted to log in to view content that can only be viewed by people with accounts_
- _As a user, i want to be able to navigate through pages and posts with minimal waiting time_

**Authentication**
- _as a user, i want to be able to create an account so that i can access the platform_
- _as a user, i want to be able to log in with my own account so i can partake in user-only features_
- _as a user, i want to be able to see if i am logged in at any given moment, so i know to log out or switch accounts if i need to_
- _as a user, i want to be able to remain logged-in to my account until i decide to sign out_

**Creating and viewing content**
- _As a user, i want to be able to make my own posts/pose my own questions for people to interact with_
- _As a user, i want to be able to view questions/posts people have posted_
- _As a user, i want to be able to view comments/answers and their vote count_
- _As a user, i want to be able to vote on answers that i think are the best for a question/post_
- _As a user, i want to be able to see the Profiles of the people that make posts and comments_
- _As a user, i want to be able to comment/answer other people's posts

**posts / individual posts**
- _As a user, i want to view the most recent posts whenever i log in_
- _As a user, i want to be able to filter posts by profiles that i am interested in_
- _As a user, i want to be able to keep track of all the posts i have interacted with_
- _As a user, i want to be able to seemlessley scroll through posts without having to wait for another page to load_
- _As a user, i want to see what the most popular answer/comment is for a post when i am scrolling through posts to see what the general opinion is_
- _As a user, i want to be able to view all the comments/answers to a post_
- _As a user, i want to be able to edit any content that i publish, to amend spelling errors or upload a better picture_
- _As a user, i want to be able to edit any comments that i make so i can amend spelling errors_
- _As a user, i want to be able to see posts that have been voted on the most, to see what is trending on the site_

**Profiles**
- _As a user, i want to be able to view other user's public profiles and see what they have contributed to_
- _As a user, i want to be able to Follow other users, so i have easier access to the content they create_
- _As a user, i want to be able to edit my own profile at any time, so i can keep my profile photo and details up to date_
- _As a user, i want to see what the top-voted comments/answers a profile has made_
- _As a user, i want to be able to see the questions/posts a profile has made so i can decide if i like their content_
- _As a user, i want to be able to update my username and password to keep my account secure_


### <ins>Scope</ins>

#### <ins>Project Aims:</ins>

This API is built with the focus of achieveing the following learning outcomes from the Portfolio 5 Assessment guide:

#### LO3: Create an Application Programming Interface (API) for consumption by 3rd party applications.
1. > Build a Back-End for a Full-Stack web application that allows users to store and manipulate data records about a particular domain.

2. > Design a database structure relevant for your domain, consisting of a minimum of TWO custom models (excluding user and profile models).

3. > Write Python code that is consistent in style and conforms to the PEP8 style guide.

4. > Include custom Python logic to demonstrate your proficiency in the language, e.g.: loops, if statements, DRF framework specific functions and classes.

5. > Include Back-End framework specific features, e.g., class-based/generic views, permissions, serializers.

6. > Develop the models (minimum two required) into a usable database where data is stored in a consistent and well-organized manner.

7. > Create a complete set of CRUD functionality for records in the API.

8. > Apply login and registration functionality.

9. > Users should not be permitted write access to restricted content or functionality.

10. > Implement manual testing and document the procedures and results in the README file for the Back-End application.

11. > Use Git & GitHub for version control of the Back-End application up to deployment, using commit messages to document the development process.

12. > Deploy a final version of the Back-End application code to a cloud-based hosting platform and test to ensure it matches the development version.

13. > Ensure the security of the deployed version of the Back-End application, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off.

14. > Document the deployment process for the API in the README file for the Back-End application.


### Structure

#### <ins>Data Model</ins>

|               Database ER Diagram                |
| :----------------------------------------------: |
| ![Database model](/readme-assets/data-model.png) |

#### <ins>Database Schema</ins>

##### **Profile**
|      Field   | Type          | Details                                          |
| -----------: | :------------ | :----------------------------------------------- |
|           id | PrimaryKey    | BigAuto Unique                                   |
| date_created | DateTimeField | (auto_now_add)                                   |
| date_updated | DateTimeField | (auto_now)                                       |
|        owner | OneToOneField | links to **User** Table                          |
|        image | ImageField    | upload to 'images/' (cloudinary db), default img |
| display_name | CharField     | max length (100), blank                          |
|          bio | TextField     | blank                                            |
- the Profile table acts as an extension to the **User** table, adding more fields to allow the user to have a more personalised experience on the front-end UI
- Display name is left optional, will be configured on the front end that if the `display_name` field is blank, then it will use their first name or username, further allowing individual users decide how they wish to represent themselves
- a bio is also an optional field which users can enter a information about themselves

##### **Post**
|        Field | Type          | Details                                          |
| -----------: | :------------ | :----------------------------------------------- |
|           id | PrimaryKey    | BigAuto Unique                                   |
| date_created | DateTimeField | (auto_now_add)                                   |
| date_updated | DateTimeField | (auto_now)                                       |
|        owner | ForeignKey    | links to **User** Table                          |
|        image | ImageField    | upload to 'images/' (cloudinary db), default img |
|        title | CharField     | max length (200), blank required                 |
|      content | TextField     | blank                                            |
- posts will require to have a title but not content, as the title could just be a straight question or as the saying goes "a picture is worth a thousand words"

##### **Comment**
|        field | type          | Details                 |
| -----------: | :------------ | :---------------------- |
|           id | PrimaryKey    | BigAuto Unique          |
| date_created | DateTimeField | (auto_now_add)          |
| date_updated | DateTimeField | (auto_now)              |
|        owner | ForeignKey    | links to **User** Table |
|         post | ForeignKey    | links to **Post** Table |
|      content | TextField     | required                |
- comments will be linked ot the post they are created under by the `post` field
- text will be a required field. as blank comments give a possibility for unnecessary spam

##### **Follow**
|        Field | Type          | Details                 |
| -----------: | :------------ | :---------------------- |
|           id | PrimaryKey    | BigAuto Unique          |
| date_created | DateTimeField | (auto_now_add)          |
|        owner | ForeignKey    | links to **User** Table, using "following" related name |
|     followed | ForeignKey    | links to **User** Table  using "followed" related name  |
- in this table, the owner "owns" a follow object which targets another user, who is to be considered "followed"
- related names are used to prevent conflict when making queries to the same table simultaneously

##### **Like**
|        Field | Type          | Details                  |
| -----------: | :------------ | :----------------------- |
|           id | PrimaryKey    | BigAuto Unique           |
| date_created | DateTimeField | (auto_now_add)           |
|        owner | ForeignKey    |  links to **User** Table |
|         post | ForeignKey    |  links to **Post** Table |
- pretty self explanatory, a like table that determines what users like what posts
- a user ca only like a post/ own one like for a post

##### **Vote**
|        Field | Type          | Details                     |
| -----------: | :------------ | :-------------------------- |
|           id | PrimaryKey    | BigAuto Unique              |
| date_created | DateTimeField | (auto_now_add)              |
|        owner | ForeignKey    | links to **User** Table     |
|      comment | ForeignKey    | links to **Comment** Table  |
- works the exact same as likes, but for comments, votes are used to determine the top comment or answer for a post


<br />

___

# Development

This project was Developed using Agile methodology, user stories and learning outcomes were achieved by completing the following documented Agile sprints, documented in GitHub Projects

Due to the nature of this project being created in 2 seperate repositories, user stories were documented as project milestones to group tasks under relevant user stories in both repositories

## Milestone 1 - Setup, admin account, and base models

| Learning Outcomes / Acceptance Criteria covered in this milestone                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------: |
| Build a Back-End for a Full-Stack web application that allows users to store and manipulate data records about a particular domain. |
| Use Git & GitHub for version control of the Back-End application up to deployment, using commit messages to document the development process. |
| Include custom Python logic to demonstrate your proficiency in the language, e.g.: loops, if statements, DRF framework specific functions and classes. |
| Include Back-End framework specific features, e.g., class-based/generic views, permissions, serializers. |
| Develop the models (minimum two required) into a usable database where data is stored in a consistent and well-organized manner. |

| User Stories covered in this milestone                                                                | details |
| :---------------------------------------------------------------------------------------------------- | :------ |
| _As a user, i want to be able to see the Profiles of the people that make posts and comments_         | Profile List view will show all profiles |
| _As a user, i want to be able to make my own posts/pose my own questions for people to interact with_ | use of `generics` in Djagno allows for easy form creation on all list views in tables |
| _As a user, i want to be able to view questions/posts people have posted_                             | Post List view will display this data |
| _As a user, i want to be able to view comments/answers and their vote count_                          | Comment List view will display this data |
| _As a user, i want to be able to vote on answers that i think are the best for a question/post_       | use of `generics` will allow creation of new votes for comments via form |
| _As a user, i want to view the most recent posts whenever i log in_                                   | all tables will have a `date-created` field and will be ordered by most recent entries by default, though filtering will be added later to the API |
| _As a user, i want to be able to filter posts by profiles that i am interested in_                    | the follows app, table and views will allow users to follow other users, allowing filtering on the front end of the application, though filtering will be added later to the API |
| _As a user, i want to be able to keep track of all the posts i have interacted with_                  | use of the likes and votes tables will allow users to see what content they have interacted with on the front end application, though filtering will be added later to the API |

| Tasks This Sprint | Sprint overview |
| :---------------- | :-------------: |
| project setup. Create all of the base models. Create an admin user. use admin user to check tables accept new data. There were no issues completing any of the tasks during this sprint. a self-created guide to create apps with generic views was made during the walkthrough modules of the course and was referred to to efficiently create all of the required apps in the tasks highlighted by the user stories. | ![sprint 1](/readme-assets/sprint-1-project-view.png)|


<br />
<br />

## Miletsone 2 - Build Detail views and create user-facing account creation/registration

| Learning Outcomes / Acceptance Criteria covered in this milestone                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------: |
| Include Back-End framework specific features, e.g., class-based/generic views, permissions, serializers. |
| Develop the models (minimum two required) into a usable database where data is stored in a consistent and well-organized manner. |
| Create a complete set of CRUD functionality for records in the API. |
| Apply login and registration functionality. |

| User Stories covered in this milestone                                                                | details |
| :---------------------------------------------------------------------------------------------------- | :------ |
| _as a user, i want to be able to create an account so that i can access the platform_ | achieved by importing/using `dj_rest_auth` and `allauth` apps |
| _As a user, i want to be able to comment/answer other people's posts_ | functionality achieved already in ListCreate views, but enhanced by detail views |
| _As a user, i want to be able to edit any content that i publish, to amend spelling errors or upload a better picture_ | details views created with generics `Update` and `Destroy` views |
| _As a user, i want to be able to edit any comments that i make so i can amend spelling errors_ | comment detail view created with `Update` and `Destroy` generics |
| _As a user, i want to be able to Follow other users, so i have easier access to the content they create_ | with ability to create accounts, there are now accounts to follow |
| _As a user, i want to be able to edit my own profile at any time, so i can keep my profile photo and details up to date_ | create profile detail view with `Retrieve` and `Update` generics |
| _As a user, i want to be able to update my username and password to keep my account secure_ | create profile detail view with `Retrieve` and `Update` generics |

| Tasks This Sprint | Sprint overview |
| :---------------- | :-------------: |
| create all detail oriented views for API using `generics`, therefore allowing the use of prefrabricated functionality from `Create` `Retrieve` `Update` and `Destroy` view tags. Create custom serialized data from related fields between models in their List and Detail views. implement registration apps and urls to create accounts outside of admin panel | ![sprint 2](/readme-assets/sprint-2-project-view.png) |


<br />
<br />

## Miletsone 3 - Implement Filters, sorting and searching

| Learning Outcomes / Acceptance Criteria covered in this milestone                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------: |
| Build a Back-End for a Full-Stack web application that allows users to store and manipulate data records about a particular domain. |
| Include custom Python logic to demonstrate your proficiency in the language, e.g.: loops, if statements, DRF framework specific functions and classes. |
| Include Back-End framework specific features, e.g., class-based/generic views, permissions, serializers. |
| Develop the models (minimum two required) into a usable database where data is stored in a consistent and well-organized manner |

| User Stories covered in this milestone                                                                | details |
| :---------------------------------------------------------------------------------------------------- | :------ |
|  _As a user, i want to be able to see posts that have been voted on the most, to see what is trending on the site_ | add serializer vote count on post view and implement filters |
| _As a user, i want to see what the most popular answer/comment is for a post when i am scrolling through posts to see what the general opinion is_ | add serializer vote count on comment view and implement filters |
| _As a user, i want to be able to view all the comments/answers to a post_ | implement filters on comments to filter by post |
| _As a user, i want to be able to view other user's public profiles and see what they have contributed to_ | add filters to post comment, vote and like to filter by user/owner | 
| _As a user, i want to see what the top-voted comments/answers a profile has made_ | add serializer vote count on comment view and implement filters |
| _As a user, i want to be able to see the questions/posts a profile has made so i can decide if i like their content_ | add filters to post comment, vote and like to filter by user/owner |

| Tasks This Sprint | Sprint overview |
| :---------------- | :-------------: |
| Create import the `django_filters` app and implement filters on all views and serializers to fulfil needs of user stories and ensure veratile filtering and searching capabilities to take advantage of when building front-end. And also, to fulfil learning outcomes. encountered some issues trying to manipulate data between post <-> votes. have pushed to backlog to be revisited when building front-end as could be achieved with React logic| ![sprint 3](/readme-assets/sprint-3-project-view.png) |

<br />
<br />

## Miletsone 4 - implementing Permissions and enforcing authentication for data manipulation

| Learning Outcomes / Acceptance Criteria covered in this milestone                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------: |
| Include custom Python logic to demonstrate your proficiency in the language, e.g.: loops, if statements, DRF framework specific functions and classes. |
| Include Back-End framework specific features, e.g., class-based/generic views, permissions, serializers. |
| Users should not be permitted write access to restricted content or functionality. |

| User Stories covered in this milestone                                                                | details |
| :---------------------------------------------------------------------------------------------------- | :------ |
|  _As a user, i want to be prompted to log in to view content that can only be viewed by people with accounts_ | implement permissions on all views |
|  _As a user, i want to be able to log in with my own account so i can partake in user-only features_ | write custom permission so only users that created an object can modify it |

| Tasks This Sprint | Sprint overview |
| :---------------- | :-------------: |
| Install and implement ther permission library from django. Implement `IsAuthenticatedOrReadOnly` permission class to all views. Create a custom permission of `IsOwnerOrReadOnly` to allow only owners of database records to modify and delete them | ![Sprint 4](/readme-assets/sprint-4-project-view.png) |

<br />
<br />


## Miletsone 5 - Live Deployment

| Learning Outcomes / Acceptance Criteria covered in this milestone                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------: |
| Deploy a final version of the Back-End application code to a cloud-based hosting platform and test to ensure it matches the development version. |
| Ensure the security of the deployed version of the Back-End application, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off. |
| Document the deployment process for the API in the README file for the Back-End application. |

| User Stories covered in this milestone                                                                | details |
| :---------------------------------------------------------------------------------------------------- | :------ |
| _As a user, i want to be able to seamlessley scroll through posts without having to wait for another page to load_ | implement pagination into API so that record data is chunked on the front end, allowing incremental loading of content for user, lowering load times and data demand |

| Tasks This Sprint | Sprint overview |
| :---------------- | :-------------: |
| implement use of JWT tokens for deployed production version, setting JSON export of data from API as default in production, format date fields to be user-friendly, add a root-route to API that gives a prompt to users. add pagination to List views to help manage data load on front end | ![sprint 5](/readme-assets/sprint-5-project-view.png) |


<br />
<br />

## Milestone 6 - PEP8 Compliance

| Learning Outcomes / Acceptance Criteria covered in this milestone                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------: |
| Write Python code that is consistent in style and conforms to the PEP8 style guide. |

This sprint was conducted with the idea that code for the API is correct and completely functional ahead of Front-end/React project development.

| Tasks This Sprint | Sprint overview |
| :---------------- | :-------------: |
| run all code through certified linting tool/s to ensure PEP8 compiance and that code is structured correctly | ![sprint 6](/readme-assets/sprint-6-project-view.png) |

A number of unresolvable errors were found in the project when linting the code with the **Pylint** extension. However, these errors were revealed to be obsolete when cross-checking project through the **CI Pyton Linter** app provided by Code Institute. More details on these errors can be found in the [Bugs](#bugs) section.

Subsequent Milestones were conducted on the front end repository. [Check it out here](https://github.com/Cal-Rex/y-react-front-end-milestone-project-5/blob/main/README.md)

___

# Features

### Root
when a user visits the API, if connected successfully, the following object will be returned as a welcome message:
```py
{
    "message": "welcome to the Y API",
    "instructions 1": "suffix the url with /admin to log in",
    "instructions 2": "Or, view the different tables with:",
    "instructions 3": [
        "/profiles",
        "/posts",
        "/comments",
        "/follows",
        "/likes",
        "/votes"
    ]
}
```

### Admin
The API has a working admin page, though it does not adopt styling in production view, it can still be accessed to manipulate data in all tables as an admin. simply append the environment url with `/admin` to log in with admin credentials

### registration
new accounts can be created using `dj-rest-auth/registration/` thanks to the `dj-rest-auth` package
- when an account is created with this method, the profile model will create a new profile record and link it to the profile via it's `pk`

### Profiles
`/profiles` will return a list of all profiles in the Api database in the Profile table. Every profile is linked to a `User` record in the database and is done so immediately when a user is created.
- items of the list returned are paginated in groups of `10`, this is to allow for data chunk and manageable sizing of payloads sent/requested from the front-end.

data can be ordered on thie page as follows:
- by posts_count (ascending/descending)
- followers_count (ascending/descending)
- following_count (ascending/descending)
- comments_count (ascending/descending)
- date a follow was created (ascending/descending)
- date another user followed that profile (ascending/descending)

data can be filtered by:
- profiles a user has followed
- profiles that are following the user

A wide array of ordering/filters were predetermined in the backend to maximize functonality and verstility for growath of the front-end project in the long run.

A search feature allows users to make a keyword search on all profiles in the table by `username`

A `display_name` variable has been impletemented as there was going to originally be a display name in the original scope of the project, however, this is now out of scope. field remains in place for same reason as above

Additional fields are generated using a serializer by incorporting data from other tables:
- posts_count
- followers_count 
- following_count 
- comments_count 
- is_owner
- following_id 

`/profile/<:id>` allows for a detail view odf a single profile. using `generics` the record can be retreived or updated by form

### posts
`/posts` will return a list of all posts in the Api database in the Post table.

data can be ordered on thie page as follows:
- likes_count (ascending/descending)
- comments_count (ascending/descending)

data can be filtered by:
- posts by a followed user
- posts by user
- posts user has liked
- posts user has commented on

A search feature allows users to make a keyword search on all posts in the table by `title` and `owner`

Using the `generics` library, new posts can be created within the api with a simple form in the list view

Additional fields are generated using a serializer by incorporting data from other tables:
- is_owner
- liked_id 
- likes_count 
- comments_count

`/posts/<:id>` allows for a detail view of a single post. using `generics` the record can be retreived, updated by form or destroyed

### comments
`/comments` will return a list of all posts in the Api database in the Comment table.

data can be ordered on thie page as follows:
- votes_count (ascending/descending)
- post (id) (ascending/descending)

data can be filtered by:
- comments by a user
- comments by post
- comments user has voted on

A search feature allows users to make a keyword search on all comments in the table by `content` and `owner`

Using the `generics` library, new comments can be created within the api with a simple form in the list view

Additional fields are generated using a serializer by incorporting data from other tables:
- profile_id
- profile_image
- post_title 
- voted_on_id 
- votes_count 
- is_owner

`/comments/<:id>` allows for a detail view of a single comment. using `generics` the record can be retreived, updated by form or destroyed.

### follows
`/follows` will return a list of all follow instances between profiles in the Api database in the Follow table.

Additional fields are generated using a serializer by incorporting data from other tables:
- owner_id
- owner_image
- followed_username
- followed_user_image
- is_owner

Using the `generics` library, new follow instances can be created within the api with a simple form in the list view

`/follows/<:id>` allows for a detail view of a single follow. using `generics` the record can be retreived, or destroyed

the `UniqueConstraint` method is used to make sure that every follow instance created is unique, there can only be one of each type/combination of users

### likes

`/likes` will return a list of all like instances between a user and a post in the Api database in the Like table.

data can be ordered by:
- owner (ascending/descending)
- post (ascending/descending)
- post with most likes (ascending/descending)
- post with most comments (ascending/descending)

data can be filtered by:
- post
- owner

Additional fields are generated using a serializer by incorporting data from other tables:
- post_id
- owner_id
- owner_image
- is_owner

A search feature allows users to make a keyword search on all likes in the table by `owner` and `post`

Using the `generics` library, new like instances can be created within the api with a simple form in the list view

`/likes/<:id>` allows for a detail view of a single like. using `generics` the record can be retreived, or destroyed

the `UniqueConstraint` method is used to make sure that every like instance created is unique, there can only be one of each type/combination of users and post

### votes
`/votes` will return a list of all votes instances between a user and a comment in the Api database in the Vote table.

data can be ordered by:
- owner (ascending/descending) 
- comment (ascending/descending) 
- number of votes on comment (ascending/descending) 

data can be filtered by
- user
- post
- comment

Additional fields are generated using a serializer by incorporting data from other tables:
- owner_id
- owner_image
- post
- comment
- is_owner

A search feature allows users to make a keyword search on all votes in the table by `owner`, `post` and `comment`

Using the `generics` library, new vote instances can be created within the api with a simple form in the list view

the `UniqueConstraint` method is used to make sure that every vote instance created is unique, there can only be one of each type/combination of users and comment

`/votes/<:id>` allows for a detail view of a single vote. using `generics` the record can be retreived, or destroyed

___

# Bugs 

### Resolved bugs:
Connection refused error when creating an account
- User record would be created but not profile and an error would be thrown during authentication
- added following code from stack overflow source and resolved issue. As email vericfication is mandatory this was changed to `True`
```py
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_AUTHENTICATION_METHOD = 'username'

ACCOUNT_EMAIL_REQUIRED = True
```
- [source](https://stackoverflow.com/questions/45006190/connectionrefusederror-in-django-rest-api-while-registration-process)

### Unresolved Bugs:
Like Model accidentally has 2 identical fields:
- `post_id` serialized field produces identical result to `post` field. easy fix but there is not enough tie in this sprint to rectify



Programs:
- [Code Institute PEP8 Python Linter](https://pep8ci.herokuapp.com/#)