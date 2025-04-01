What celestial object are you looking for?
=
[![GitHub Stars](https://img.shields.io/github/stars/Mart-igor/GUI_for_identifying_stationary_mode.svg)](https://github.com/Mart-igor/GUI_for_identifying_stationary_mode/stargazers)
[![GitHub release (latest by semver)](https://img.shields.io/github/v/release/Mart-igor/GUI_for_identifying_stationary_mode?color=60be86&label=Latest%20release&style=social&sort=semver)](https://github.com/Mart-igor/GUI_for_identifying_stationary_mode/releases)
[![Watchers](https://img.shields.io/github/watchers/Mart-igor/GUI_for_identifying_stationary_mode?style=social)](https://github.com/Mart-igor/GUI_for_identifying_stationary_mode/watchers)
 
Come in and choose your favorite while the discounts are on  
*(anyway make sure you have enough money... ;)*
![Chat Preview](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/7ca5f89cbd6c3c3ac835544437d8f915ffd5fcbb/screenshots/Clipchamp6-ezgif.com-resize.gif)

***
***

## Introduction

To demonstrate my skills and abilities, I created a website.  
The following features have been implemented:  

0. I orginiezed a menagment of this project by myself
     - **Jira** - *organizer and manage your task from staging to deployment*
1. The site consists of several ***apps*** that do their job  
-- **main** - *display of celestial objects (taking into account their categories)*  
-- **cart** - *display of shopping list*  
-- **users** - *interaction with users (login, logout, registration)*  
-- **orders** - *create order*  
-- **payment** - *payment for goods*
1. When creating ***templates*** I used:  
-- **html5**  
-- **jinja**  
   - *to make the templates look beautiful I used:*  
-- **bootstrap**  
-- **css**  
-- **cdnjs**
1. To populate the ***database*** I used:  
-- **ORM**  
-- **admin-panel**  
-- **PostgreSQL**
1. In order to be able to roll back in case of a fatal error (actually mostly as an artificial ***team experience***), I used:  
-- **Git & GitHub**
1. To keep it in Internet I use two ways:
   - use web-server
   - use Linux server and nginx

---
## Table of content
- [What celestial object are you looking for?](#what-celestial-object-are-you-looking-for)
  - [Introduction](#introduction)
  - [Table of content](#table-of-content)
  - [Tech Stack](#tech-stack)
  - [Demo](#demo)
    - [📌 Home Page](#-home-page)
    - [🗂 Categories Page](#-categories-page)
    - [🪐 Product Page](#-product-page)
    - [🔐 Login Page](#-login-page)
    - [🛒 Shopping Cart](#-shopping-cart)
    - [📦 Order Page](#-order-page)
    - [✅ Review Your Order](#-review-your-order)
    - [💳 Payment Page (Stripe)](#-payment-page-stripe)
  - [Development Workflow](#development-workflow)
    - [📝 Planning with Jira](#-planning-with-jira)
      - [Screenshots:](#screenshots)
      - [Why Jira?](#why-jira)
  - [Deployment](#deployment)
  - [Feedback](#feedback)

## Tech Stack

**Management** Jira

**Client:** Django, PosgreSQL, Docker

**Server:** Linux, nginx

## Demo

The Celestial Objects Online Store offers a user-friendly interface for purchasing stars, planets, and other cosmic bodies. Below is an overview of the key pages on the website.

### 📌 Home Page  
- **Description**: Displays the most popular items (by sales volume).  
- **Features**:  
  - The header includes navigation elements: login/signup buttons, links to social media, and the shopping cart.  
  - A slider or product grid highlighting "best sellers."  
- **Screenshot**:  
  ![Home Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/home_gif.gif)  

### 🗂 Categories Page  
- **Description**: Users can browse products by category (e.g., "Stars," "Planets," "Galaxies").  
- **Features**:  
  - Responsive product grid with brief descriptions.  
- **Screenshot**:  
  ![Categories Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/categories_gif.gif)  

### 🪐 Product Page  
- **Description**: Detailed information about a selected celestial object.  
- **Features**:  
  - Images, price, description, and specifications (mass, diameter, distance from Earth).  
  - "Add to Cart".  
- **Screenshot**:  
  ![Product Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/product_gif.gif)  

### 🔐 Login Page  
- **Description**: Authentication or registration form.  
- **Features**:  
  - Email/password fields.  
  - Links for password recovery and signup.  
- **Screenshot**:  
  ![Login Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/login_gif.gif)  

### 🛒 Shopping Cart  
- **Description**: Review selected items before checkout.  
- **Features**:  
  - Remove items.  
  - Total cost and a "Proceed to Payment" button or "Continue shopping".  
- **Screenshot**:  
  ![Cart Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/cart_gif.gif)  

### 📦 Order Page  
- **Description**: Enter delivery details.  
- **Screenshot**:  
  ![Order Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/order_gif.gif)  

  ### ✅ Review Your Order  
- **Description**: EReview your order and confirm the order.  
- **Screenshot**:  
  ![Order Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/payment_gif.gif) 

### 💳 Payment Page (Stripe) 
- **Description**: Integrated payment system (e.g., Stripe).  
- **Note**: Use test card details for demo transactions:  
  `4242 4242 4242 4242` (Expiry: `12/34`, CVC: `123`).  
- **Screenshot**:  
  ![Payment Page](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/strip_gif.gif)

## Development Workflow  

### 📝 Planning with Jira  
I began by breaking down the project into structured milestones using **Jira**, which helped organize tasks and track progress efficiently.    

#### Screenshots:  
- **Project Plan**:  
  ![Chat Preview](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/7ca5f89cbd6c3c3ac835544437d8f915ffd5fcbb/screenshots/plan.png) 
- **Workflow Visualization**:  
  ![Chat Preview](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/7ca5f89cbd6c3c3ac835544437d8f915ffd5fcbb/screenshots/work_flow.png)  

#### Why Jira?  
- **Agile Management**: Enabled iterative development with sprints.  
- **Transparency**: Clear task ownership and deadlines.  


## Deployment

If you want deploy this project you should use Linux to make a sever 
Here's two ways to do it: 
1. Your main oparating system is Linux
2. Use VirtualBox


## Feedback

Feel free to send us feedback on Twitter or file an issue. Feature requests are always welcome. If you wish to contribute, please take a quick look at the guidelines!