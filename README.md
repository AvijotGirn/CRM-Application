# Django CRM Application

Welcome to the Django CRM Application! This is a customer relationship management (CRM) system built as a passion project in order to get hands on experience with the Django framework. 

## Project Overview

This Django CRM application provides (and is planned to include) features such as:

- User authentication and authorization
- Client/Customer Management (Add, Delete, Edit Clients)
- Administrative Controls/Privilege
- Real Time Updating Database to keep information up to date
- Simple & Intuitive User Interface

## Prerequisites

Make sure you have the following installed before running the application:

- Python 3.12 (Have not tested with older versions)
- Dependencies listed in `Requirements.txt`
```pip install -r requirements.txt```

Setup & Activate your Virtual Environment:
   ```bash
   python -m venv venv
```
```
   .\venv\Scripts\activate
```

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/AvijotGirn/CRM-Application.git)https://github.com/AvijotGirn/CRM-Application.git
```

Apply Migrations: 
   ```bash
   python manage.py migrate
```

Run the Server:
   ```bash
   python manage.py runserver
```

(Optional) Collect Static: 
   ```bash
   python manage.py collectstatic
```
