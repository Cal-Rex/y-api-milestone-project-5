# Y - API
## Made with Django Rest

## Table of Contents
1. [INTRODUCTION](#introduction)
2. [DESIGN](#design)
3. [FEATURES](#features)
- [Design Features](#design-features)
- [404 and 500 Features](#404-and-500-error-pages)
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

<br>
___

# Design

## Data models

#### **Profile**
| field | type |
|-:|:-|
|date_created| DateTimeField(auto_now_add) |
|date_updated| DateTimeField(auto_now) |
|owner| OneToOneField(User) |
|image| ImageField |
|display_name| CharField |
|bio| TextField |

#### **Post**
| field | type |
|-:|:-|
|date_created| DateTimeField(auto_now_add) |
|date_updated| DateTimeField(auto_now) |
|owner| ForeignKey(User) |
|image| ImageField |
|title| CharField|
|content| TextField |

#### **Comment**
| field | type |
|-:|:-|
|date_created| DateTimeField(auto_now_add) |
|date_updated| DateTimeField(auto_now) |
|owner| ForeignKey(User) |
|post| ForeignKey(Post) |
|content| TextField |

#### **Follow**
| field | type |
|-:|:-|
|date_created| DateTimeField(auto_now_add) |
|owner| ForeignKey(User) |
|followed| ForeignKey(User) |

#### **Like**
| field | type |
|-:|:-|
|date_created| DateTimeField(auto_now_add) |
|owner| ForeignKey(User) |
|post| ForeignKey(Post) |

#### **Vote**
| field | type |
|-:|:-|
|date_created| DateTimeField(auto_now_add) |
|owner| ForeignKey(User) |
|comment| ForeignKey(Comment) |

