# Review Questions, chapter 2


## 1. Discuss the importance of data models.

Model - is conceptual representation of world objects or business themes.  
Developing data models helps to reveal business needs of storing and manipulating its data.  
Models, as it is visual tool, help in communication between database designer and customer.  


## 2. What is a business rule, and what is its purpose in data modeling?

Business rule - is a 'law' according to which the particular organization or event is behaved in its specific environment needs.  
Establishing models througs revealing business rules - main concept of data modelling.  


## 3. How do you translate business rules into data model components?

Within business rule, we need define entities and their relationship.  
For example: "Employee works for one and only one department. Department has multiple employees." is   
a business rule, from which we can conclude that there are 'employee' and 'department' entities, and  
they participate in particular relationship.  


## 4. Describe the basic features of the relational data model and discuss their importance to the end user and the designer.

Relational Data Model - model based on the mathematical theory of 'relations'.  
With help of relational modelling, we can consolidate and record all the business rules within organization.  
Each entity set within this model are represented as two dimentional table,  
that allows to keep track of each entity's instance state through entity attributes.  


## 5. Explain how the entity relationship (ER) model helped produce a more structured relational database design environment.

Structural design - separating businness concepts and establiching relationships among them.  


## 6. Consider the scenario described by the statement “A customer can make many payments, but each payment is made by only one customer.” Use this scenario as the basis for an entity relationship diagram (ERD) representation.


## 7. Why is an object said to have greater semantic content than an entity?

An object can represent its behaviour and state through methods, while entity has only attributes.  
This peculiarity allows to have more meaning to object.


## 8. What is the difference between an object and a class in the object-oriented data model (OODM)?

Class in data oriented modelling - is objects set, that share the same set of attitbutes and logically connected.  
Object - is particular instance of class.  


## 9. How would you model Question 6 with an OODM? (Use Figure 2.4 as your guide.)



## 10. What is an ERDM, and what role does it play in the modern (production) database environment?

Extended relational data model - adds some object oriented features in relational database structure.  
Encapsulation of data and methods in objects, custom data types based on classes, inheritance.  
ERDM allows to simplify interaction with complex data.  


## 11. What is a relationship, and what three types of relationships exist?

Relationship within relational model is logical connection between instances in entities.  
Establishing relationships through values in common attributes allows maintain referential integrity.  

* 1:1
* 1:M
* M:N


## 12. Give an example of each of the three types of relationships.

* One-to-one - employee -- reports to -- manager(employee)
* One-to-many - manager -- manages -- department
* Many-to-many - movie -- belongs to -- genre


## 13. What is a table, and what role does it play in the relational model?

Table represent entity set - two-dimentional structure that holds track of each instance's state.  
Entity set - logically grouped instances that have same set of attributes (almost all).  
Table allows to maintain entity integrity through establishing primary keys.  


## 14. What is a relational diagram? Give an example.

Method of representing relational data model.  
Entities are in entity rectangles, attributes are in attribute rectangles below entities,  
lines connect entities and capture relationships types and cardinalities.  


## 15. What is connectivity? (Use a Crow’s Foot ERD to illustrate connectivity.)

Connectivity - the term to describe 'type' of relationship: 1:1, 1:M, M:N.   


## 16. Describe the Big Data phenomenon.

The need of another approach of handling large amount of semi-structured data dictated by fast growing of internet technologies and amount of data from different kind of sensors triggered arrival of Big Data phenomenon.  
This movement created to address problem of fast analysis of large amount of data and retrieving business insights from it.  

## 17. What does the term 3 Vs refer to?

Three basic characteristics of Big Data: Volume, Velocity, Variety.  


## 18. What is Hadoop, and what are its basic components?

Hadoop is Java-based, open-source, high-speed, fault-tolerance distributed storage and computational framework.  
It uses low-cost hardware to create clusters and perform parallel processing.  


## 19. What are the basic characteristics of a NoSQL database?

Not only SQL databases characterized as highly distributed systems can handle huge amount of strucrured and semi-structured data.  


## 20. Using the example of a medical clinic with patients and tests, provide a simple representation of how to model this example using the relational model and how it would be represented using the key-value data modeling technique.



## 21. What is logical independence?

A condition in which internal model can be altered without affecting conceptual model.  


## 22. What is physical independence?

A condition when the phisical model can be changed without affecting internal model.  
Phisical model describe data storage format, and location.  
