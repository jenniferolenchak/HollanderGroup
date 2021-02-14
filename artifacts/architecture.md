Populate each section with information as it applies to your project. If a section does not apply, explain why. Include diagrams (or links to diagrams) in each section, as appropriate.  For example, sketches of the user interfaces along with an explanation of how the interface components will work; ERD diagrams of the database; rough class diagrams; context diagrams showing the system boundary; etc. Do _not_ link to your diagrams, embed them directly in this document by uploading the images to your GitHub and linking to them. Do _not_ leave any section blank.

# Program Organization

You should have your context, container, and component (c4model.com) diagrams in this section, along with a description and explanation of each diagram and a table that relates each block to one or more user stories. 

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

See Code Complete, Chapter 3

# User Interface Design

You should have one or more user interface screens in this section. Each screen should be accompanied by an explaination of the screens purpose and how the user will interact with it. You should relate each screen to one another as the user transitions through the states of your application. You should also have a table that relates each window or component to the support using stories. 

See Code Complete, Chapter 3

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

See Code Complete, Chapter 3

# Error Processing

To ensure what information being entered by the user meets requirements and follows a proper format, IO errors will be detected at the field level. 

# Fault Tolerance

If a user enters invalid information into a field, the data will be disregarded an error message will be displayed containing the proper specifications of the field.

# Architectural Feasibility



# Overengineering



# Build-vs-Buy Decisions

Django is being used for data formating, display, and it's ORM feature to easily manipulate data.

See Code Complete, Chapter 3

# Reuse

This app will not reuse an pre existing software, test cases or data formats

# Change Strategy

Once a user sign in, Savester will notify the use when  a recurring payment is approaching. If time permits, a text api will be implemented which allows users to get this notfication without signing into the app. 
