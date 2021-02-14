Populate each section with information as it applies to your project. If a section does not apply, explain why. Include diagrams (or links to diagrams) in each section, as appropriate.  For example, sketches of the user interfaces along with an explanation of how the interface components will work; ERD diagrams of the database; rough class diagrams; context diagrams showing the system boundary; etc. Do _not_ link to your diagrams, embed them directly in this document by uploading the images to your GitHub and linking to them. Do _not_ leave any section blank.

# Program Organization

[Context Diagram](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/documents/System%20Context%20Diagram.png)

Our context diagram gives an overall big-picture view of our project. We want the user to be able to interact with the budgeting system to track their expenses and savings, and also be reminded of these things in a timely and effective manner. This is what we wanted to achieve with user story 2, 4, and 10.

See Code Complete, Chapter 3 and https://c4model.com/

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

You should list the assumptions, rules, and guidelines from external sources that are impacting your program design. 

# User Interface Design

![UI Mock-Up](https://github.com/jenniferolenchak/Savester/blob/main/artifacts/UI%20Diagram%20_%20Dashboard.JPG)
**UI Mock-Up**
As a web application, the user will be able to access the system through the URL https://savesterapp.herokuapp.com/ on both a desktop and mobile platforms [user story 007]; While on the desktop version, a peripheral device (i.e. mouse) may be used to interact with the website, while the mobile version warrants touchscreen interaction. Once a user signs in[user story 001], they are brought to their dashboard (shown in the mock-up above). It is here that they may view their budget for their decided interval and view upcoming recurring payments[user story 002]. Users are also presented with a graphic representations of their budget plan, savings goal[user story 008], categories of spending [user story 003], and percent of budget spent. Beyond the dashboard, users may navigate to other pages to edit their financial data[user story 006 & 009 & 010], view savings suggestions[user story 004], edit their account information[user story 005], and see more details on upcoming payments[user story 002].

# Resource Management

Connection to the database will be opened when a database querry is made. The connection will be reused are remained open until error or max age is encountered.

# Security

User passwords will be hashed using the PBKDF2 hashing algorithm

# Performance

Web page contents will be preloaded to reduce loading times. Additionally, website contents will be loaded
in an order where the user can immediately start interacting with the page. While the website is loaded, a spinner will be displayed to maintain engagement
with the user. 

# Scalability

If an increase in users is experienced from different parts of the world, a CDN will be implemented to help decrease load times. If CPU and memory issues
are encountered, database will be moved to a seperate server to scale application and database seperately. If our single application server can no longer handle the
the current load, more application servers will be added aswell as a load balancer to distribute traffic within servers equally.

# Interoperability

Web app operates independently and does not communicate with any other software.

# Internationalization/Localization

Information of language is provided by the browser header. A resource file will be used that contains all available translations for a language. A resource
file is used because it is easier to automate.

# Input/Output

To ensure what information being entered by the user meets requirements and follows a proper format, IO errors will be detected at the field level

# Error Processing

The system will take an activate approach to error detection. Everytime a user enters data, it will automatically check for validity. If user input is invalid, data will be disregarded immediately. Additionally, error messages will be logged an outputed to file.

# Fault Tolerance

If a user enters invalid information into a field, the data will be disregarded an error message will be displayed containing the proper specifications of the field.

# Architectural Feasibility



# Overengineering

Classes are equally simple therefore over engineering is avoided

# Build-vs-Buy Decisions

Django is being used for data formating, display, and it's ORM feature to easily manipulate data.

# Reuse

This app will not reuse an pre existing software, test cases or data formats

# Change Strategy

Once a user signs in, Savester will notify the user when  a recurring payment is approaching. If time permits, a text api will be implemented which allows users to get this notfication without signing into the app. This feature will be implemented seperately and should not interfere with other processes.
