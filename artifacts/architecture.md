Populate each section with information as it applies to your project. If a section does not apply, explain why. Include diagrams (or links to diagrams) in each section, as appropriate.  For example, sketches of the user interfaces along with an explanation of how the interface components will work; ERD diagrams of the database; rough class diagrams; context diagrams showing the system boundary; etc. Do _not_ link to your diagrams, embed them directly in this document by uploading the images to your GitHub and linking to them. Do _not_ leave any section blank.

# Program Organization

![Context Diagram](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/System%20Context%20Diagram.png)

Our context diagram gives an overall big-picture view of our project. We want the user to be able to interact with the budgeting system to track their expenses and savings, and also be reminded of these things in a timely and effective manner. This is what we wanted to achieve with user story 2, 4, and 10.

Our budget system is essentially what provides
the main function of our web app. It will contain
everything that a user may want to use ourapp for,
which will all be accessible through our dashboard

The email system is responsible
for the essential communication
from the app to the user when the user
is not physically present on the web app.
It's a key to our apps functionality,
because in order for us to deliver an 
experience worth while, we need to 
make sure that our users are actually
given relevant information real time.

![Container Diagram](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/Container%20Diagram.png)

Our Container Diagram shows an overall view of the kind of systems and servers our project will be working with. In order to satisfy the needs of user story 1, 2, and 5, we had to make sure we had an email system capable of sending emails at the right time, as well as a database that can store information properly and for usage of the application

Using Django, we intend
to code the functionality and 
features of our app, such as the
budgeting, saving, and income 
implementation. It will contain the 
actual features of the app that we 
want to deliver.

The email system is responsible
for the essential communication
from the app to the user when the user
is not physically present on the web app.
It's a key to our apps functionality,
because in order for us to deliver an 
experience worth while, we need to 
make sure that our users are actually
given relevant information real time.

For our database, we ended up going
with a PostgreSQL database, due to its
easy to use interface, as well as it being 
very easy to implement with heroku. It 
will be used to keep track of important 
user information, and be open to other parts
of the app so that we can use the data to
deliver functionality of our features that 
require it. 

This container is what handles the bulk of 
the information side of our web app.
Communication between the web app and
the database is essential for delivering both
the correct and relevant information to our 
users. When a user enters information into
the web app, it will be stored into our database,
and the database will securely store this 
information so that we can keep track of it
and use it for other functionalities of the app.

![Component Diagram](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/Component%20Diagram.png)

Our component diagram provides a more in depth look at our web app and the things it will communicate with to develop features. For user stories involving account information and settings, such as 1 and 4, we are using features that Django has, such as the sign and login features, which will communicate with our database to provide a login system that allows users to change their passwords and safely log in when needed. Our sav esuggestion and budget component will work together with our email component to provide some of the key functionalities of the app, such as letting people know what they can save in, and what kind of expenses they have, satisfying user stories 4, 8, 9 and 10.

The sign in feature
will be behind 
the log in page,
allowing users 
to enter their account 
details and log in

The forgot password feature
will allow users to reset their 
passwords using djangos functionality

Our budget component featured in our
dashboard will allow the user a big-picture
view of their spending over as given period
of time



The security component will ensure that
sensitive user data is kept safe using 
Django's features. 

The email component will work
with the email system to ensure the 
right information is being sent to it,
and eventually, the user.

Our saving suggestion is a central
component to the functionality of
our app. Using existing user data,
we take into account what the user is spending
and other information that they have
entered to deliver relevant saving
opportunities that the user can start
implementing right away without 
changing anything about the way they 
spend their money.

Our admin feature container
provides a look into the behind-the-scenes
aspect of the app. The information a user enters
will be both very personal and handled privately,
while still being used in a secure way to deliver
full functionality of our web app

For our database, we ended up going
with a PostgreSQL database, due to its
easy to use interface, as well as it being 
very easy to implement with heroku. It 
will be used to keep track of important 
user information, and be open to other parts
of the app so that we can use the data to
deliver functionality of our features that 
require it. 

The email system is responsible
for the essential communication
from the app to the user when the user
is not physically present on the web app.
It's a key to our apps functionality,
because in order for us to deliver an 
experience worth while, we need to 
make sure that our users are actually
given relevant information real time.

# Code Design

![Class UML](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/classUML.png)  
**Class UML**  
Indicated in the Class diagram is each user story that relates to a given class. The custom and admin classes are in the diagram to show that there will be two main users. The customer class has access to the createIncome and createBudget which both have respective classes.  
![Activity UML](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/activityUML.png)  
**Activity UML**  
The Activity diagram shows the process of a customer requesting a password reset.  
![Sequence UML](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/sequenceUML.png)   
**Sequence UML**  
The Sequence diagram shows how each class interacts with the other. 

# Data Design

![Database ER Diagram](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/ERdatabase.png)  
**Database ER Diagram**  
The database contains four entities: Users, Settings, BudgetLists, and CashFlows. The user stores hold attributes for Username and Password alongside relationships with Settings and BudgetLists. The settings contain key information about the user alongside their preferences. The BudgetList contains attributes for savings goals and balance alongside a relationship with the Cashflows. Cashflows are either payments or expenses that are store to track the user income and spending habits. 

# Business Rules

Users will be allowed to enter information such as income/expenses which should quickly be factored into their budget and graphically represented by charts. This process should happen instantanously to allow for a good user experience.  

# User Interface Design

![UI Mock-Up](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/UI%20Diagram%20_%20Dashboard.JPG)
![Page Connectivity](https://github.com/jenniferolenchak/Savester/blob/main/Graphics/UI%20Diagram%20_%20Page%20Connectivity.JPG?raw=true)
**UI Mock-Up**
As a web application, the user will be able to access the system through the URL https://savesterapp.herokuapp.com/ on both a desktop and mobile platforms [user story 007]; While on the desktop version, a peripheral device (i.e. mouse) may be used to interact with the website, while the mobile version warrants touchscreen interaction. Once a user signs in[user story 001], they are brought to their dashboard (shown in the mock-up above). It is here that they may view their budget for their decided interval and view upcoming recurring payments[user story 002]. Users are also presented with a graphic representations of their budget plan, savings goal[user story 008], categories of spending [user story 003], and percent of budget spent. Beyond the dashboard, users may navigate to other pages to edit their financial data[user story 006 & 009 & 010], view savings suggestions[user story 004], edit their account information[user story 005], and see more details on upcoming payments[user story 002].

# Resource Management

Connection to the database will be opened when a database querry is made. The connection will be reused are remained open until error or max age is encountered.

# Security

When users create an account, they will be asked for to enter a username and passowrd. User passwords will be hashed by undergoing mutliple iterations of a hashing algorithm. This ensures password security.

# Performance

Web page contents will be preloaded to reduce loading times. Additionally, website contents will be loaded
in an order where the user can immediately start interacting with the page. While the website is loaded, a spinner will be displayed to maintain engagement
with the user. 

# Scalability

If an increase in users is experienced from different parts of the world, a CDN will be implemented to help decrease load times. If CPU and memory issues
are encountered, database will be moved to a seperate server to scale application and database seperately. If our single application server can no longer handle the
the current load, more application servers will be added aswell as a load balancer to distribute traffic within servers equally.

# Interoperability

Web app operates independently and does not communicate with any other software. (subject to change)

# Internationalization/Localization

Information of language is provided by the browser header. A resource file will be used that contains all available translations for a language. A resource
file is used because it is easier to automate.

# Input/Output

Users will be required to enter data into a variety of fields, to ensure that information being entered by the user meets requirements and follows a proper format, IO errors will be detected at the field level.

# Error Processing

The system will take an activate approach to error detection. Everytime a user enters data, it will automatically check for validity. If user input is invalid, data will be disregarded immediately. Additionally, error messages will be logged an outputed to file.

# Fault Tolerance

If a user enters invalid information into a field, the data will be disregarded an error message will be displayed containing the proper specifications of the field.

# Architectural Feasibility

At the initial stages of product deployment, it is expected to have a relatively low user count therefore, our single application server should be able to meet performance targets. However, if a increase in users is experienced, the app will be appropriately scaled. The scalability section contains information about how we plan on doing so. 


# Overengineering

Classes are equally simple therefore over engineering is avoided

# Build-vs-Buy Decisions

Django is being used for data formating, display, and it's ORM feature to easily manipulate data.

# Reuse

This app will not reuse an pre existing software, test cases or data formats

# Change Strategy

Once a user signs in, Savester will notify the user when  a recurring payment is approaching. If time permits, a text api will be implemented which allows users to get this notfication without signing into the app. This feature will be implemented seperately and should not interfere with other processes.
