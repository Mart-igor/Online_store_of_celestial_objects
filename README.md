What celestial object are you looking for?
=
[![GitHub Stars](https://img.shields.io/github/stars/Mart-igor/Online_store_of_celestial_objects.svg)](https://github.com/Mart-igor/Online_store_of_celestial_objects/stargazers)
[![GitHub release (latest by semver)](https://img.shields.io/github/v/release/Mart-igor/Online_store_of_celestial_objects?color=60be86&label=Latest%20release&style=social&sort=semver)](https://github.com/Mart-igor/Online_store_of_celestial_objects/releases)
[![Watchers](https://img.shields.io/github/watchers/Mart-igor/Online_store_of_celestial_objects?style=social)](https://github.com/Mart-igor/Online_store_of_celestial_objects/watchers)
 
Come in and choose your favorite while the discounts are on  
*(anyway make sure you have enough money... ;)*
![Chat Preview](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/Clipchamp6-ezgif.com-resize.gif)

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
1. To populate the ***database*** I used:  
-- **ORM**  
-- **admin-panel**  
-- **PostgreSQL**
1. In order to be able to roll back in case of a fatal error (actually mostly as an artificial ***team experience***), I used:  
-- **Git & GitHub**
1. To keep it in Internet I use two ways:
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
  ![Chat Preview](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/plan.png) 
- **Workflow Visualization**:  
  ![Chat Preview](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/screenshots/work_flow.png)  



## Deployment  

1. Клонирование репозитория  
```bash  
git clone https://github.com/Mart-igor/Online_store_of_celestial_objects.git  
cd celestial_site  
```  

2. Настройка виртуального окружения  

**Для Linux/MacOS:**  
```bash  
python -m venv venv  
source venv/bin/activate  
```  

**Для Windows:**  
```bash  
python -m venv venv  
venv\Scripts\activate  
```  

3. Установка зависимостей  
```bash  
pip install -r requirements.txt  
```  

4. Восстановление базы данных  
Дамп БД доступен в репозитории:  
https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/db

Импортируйте дамп БД (предварительно создав БД `your_db_name`):  
```bash  
pg_restore -d your_db_name celestial_site.dump  
```  

5. Настройка Stripe  
Создайте файл `.env` и добавьте ключи:  
```env  
STRIPE_PUBLIC_KEY='ваш_публичный_ключ'  
STRIPE_SECRET_KEY='ваш_секретный_ключ'  
```  

## 🌍 Публичный деплой (для доступа в интернете)

### Необходимые подготовительные шаги:
1. **Приобретение доменного имени**
2. **Аренда сервера**
3. **Подключение к серверу (спользуйте Termius или аналогичный SSH-клиент)**
4. **Используются заранее подготовленные конфигурации для контейнеров**
- [Dockerfile](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/Dockerfile)
- [docker-compose.yml](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/docker-compose.yml)
- [nginx.conf](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/nginx.conf)
5. **Инструкция по настройке сервера**
- [инструкция](https://github.com/Mart-igor/Online_store_of_celestial_objects/blob/main/deploy_guid.txt)


## Feedback

Feel free to send us feedback on Twitter or file an issue. Feature requests are always welcome. If you wish to contribute, please take a quick look at the guidelines!