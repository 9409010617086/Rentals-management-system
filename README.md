
# RENTAL MANAGEMENT SYSTEM

RHMS is a web-based application developed using the _Django framework_. The aim is to help tenants and rental house managers track 
rental arears and utility(water and electricity) payments while at the same time providing a communication chain, manager &harr; tenants
that is free from disruptions. Both parties are able to view and visualize previous payments and consumption details (for electricity and water)
at any particular time.


**Currently included functionalities for the managers**
```

Utility (Electricity & Water) Tracking and Management
Payments Management
Adding Rental Houses
Building updates
Add Managers
Tenant Management
Hired Personnel Management
Work Order Management
Reports, complaints and Maintenance Management
Visits Scheduling and Management 
Email Communications and Notifications Management
Eviction Management
Managing Move Out Notices
```
**Currently included tenants' functionalities**
```

- [x] Personal Rent and utility tracking (visualizing electricity & water consumtion)
- [ ] Online payments submission (Mpesa Integration & stripe)
- [x] View payments history
- [x] Keep track of notices made by managers
- [x] View receieved notices & create moveout notice
- [x] View and send tenancy related emails using the platform
- [x] Make Complaints
- [x] Create house reports
- [x] Submit service rating (30 days from preveous rating)
```
**Shared Funtionalities**
```
Account Management
    - SignUp & login, password change/reset, email confiration, profile update
Online messaging
Contact
Scheduling visits
Searching
```

## Modules


- [Accounts](https://github.com/shumwe/rental-house-management-system/tree/main/accounts)
    - User
    - Profiles
    - Managers
    - Tenants

- [Core](https://github.com/shumwe/rental-house-management-system/tree/main/core)
    - Contact
        - Contacts Reply
    - Unit Tour | Visits
    - Move OutNotice
    - Eviction Notice
    - Service rating
    - Communications & Emails

- [Complaints & Reports ](https://github.com/shumwe/rental-house-management-system/tree/main/complaints)
    - Unit Report Type
    - Unit Report
    - Unit Report Album
    - Complaints
    - Help Contacts

- [Rental Property](https://github.com/shumwe/rental-house-management-system/tree/main/rental_property)
    - Counties
        - Estate
        - Building
            - Unit Type
            - Rental Unit
                - Unit Album
            - MaintananceNotice

- [Utilities & Rent](https://github.com/shumwe/rental-house-management-system/tree/main/utils)
    - Payment Methods
    - Rent Details
        - Rent Payment
    - Water Billing
        - Consumption Tracking
        - Payments
    - Electricity Billing
        - Consumption Tracking
        - Payments

- [Work Order](https://github.com/shumwe/rental-house-management-system/tree/main/work_order)
    - Hired Personnel
        - Personnel Contact
    - Work Order
        - WorkOrderPayments

- [Reporting](https://github.com/shumwe/rental-house-management-system/tree/main/reporting)
    - ** Reports

The entire relaltionship structure can be found [here](https://github.com/shumwe/rental-house-management-system/tree/main/relationships/relationships.png) or a view the dot [file](https://github.com/shumwe/rental-house-management-system/tree/main/relationships/dotfile.dot)

[Requirements](https://github.com/shumwe/rental-house-management-system/tree/main/requirements.txt )

# Running the project

### .env variables is needed
~~~
DJANGO_SECRET_KEY = #random secret string
SENDGRID_EMAIL_HOST_PASSWORD = # from your sendgrid account
CLOUDINARY_API_KEY=#from cloudinary account
CLOUDINARY_CLOUD_NAME=#from cloudinary account
CLOUDINARY_API_SECRET=#from cloudinary account
STRIPE_PUBLISHABLE_KEY=#from stripe account
STRIPE_SECRET_KEY=#from cloudinary account
~~~

- ```chmod +x run-project.sh```
- ```./run-project.sh``` and provide the env variables when prompted.
