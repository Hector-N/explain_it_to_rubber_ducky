# Chapter 4. Entity Relationship Modelling


### Question 1

What two conditions must be met before an entity can be classified as a weak entity?  
Give an example of a weak entity.  

Answer:

The first condition states that weak entity is existence-dependent,  
meaning that particular instance of weak entity can not exist without relating the existent parent instance.  
The second condition - entity must have strong identifying relationship,  
which means that primary key of weak entity must contain as component primary key of parent entity. 

Example:

Species (sp_id, sp_name) --> Subspecies ([sp_id, subsp_id], name)  


### 2. Question 2

What is a strong (or identifying) relationship, and how is it depicted in a Crow’s Foot ERD?  

Relationship in which primary key of related entity consists primary key of parent entity.  
In ERD strong relationship is depicted by solid line connection.  


### 3. Question 3

Given the business rule “an employee may have many degrees,”  
discuss its effect on attributes, entities, and relationships.  
(Hint: Remember what a multivalued attribute is and how it might be implemented.)  

Answer:

We have two entities: employee and degree.  
As long as attributes need to be atomic to conform the 1NF, we can't place them all in one cell.  
We need to establish Many-to-many relationship.  
Within relational model, such a kind of relationship is established through lookup entity,  
also called associative or composite entity.  
So, initial M:N relationship between two tables we transform to two 1:M relationships between three ones.  


### Question 4

What is a composite entity, and when is it used?

Composite entity is used to convert conceptual M:N relationship,  
which can not be implemented within relational database directly, to actual database structure.  
Composite entity contains composite key that consists of primary keys of conceptual M:N relationship.  
Composite entity is used to avoid duplicating data and Nulls.  


### Question 5

Suppose you are working within the framework of the conceptual model in Figure Q4.5.  
Given the conceptual model in Figure Q4.5:
    a. Write the business rules that are reflected in it.
    b. Identify all of the cardinalities.

Answer:

Figure depicts "car servise" business scenario.  
Rules:
* Customer may have many cars or may haven't got any.  
* Each car may receive maintaince
* Maintaince may include 1:M Lines
* every Line have one Part
* Not every Part may exists in Line table


### Question 6
6. What is a recursive relationship? Give an example.


### Question 7
7. How would you (graphically) identify each of the following ERM components in a Crow’s Foot notation?
    a. an entity
    b. the cardinality (0,N)
    c. a weak relationship
    d. a strong relationship


### Question 8
8. Discuss the difference between a composite key and a composite attribute. How would each be indicated in an ERD?


### Question 9
9. What two courses of action are available to a designer who encounters a multivalued attribute?


### Question 10
10. What is a derived attribute? Give an example. What are the advantages or disadvanages of storing or not storing a derived attribute?


### Question 11
11. How is a relationship between entities indicated in an ERD? Give an example using the Crow’s Foot notation.


### 12. Discuss two ways in which the 1:M relationship between COURSE and CLASS can be implemented. (Hint: Think about relationship strength.)


### 13. How is a composite entity represented in an ERD, and what is its function? Illustrate the Crow’s Foot notation.


### 14. What three (often conflicting) database requirements must be addressed in database design?


### 15. Briefly, but precisely, explain the difference between single-valued attributes and simple attributes. Give an example of each.


### 16. What are multivalued attributes, and how can they be handled within the database design?

Questions 17–20 are based on the ERD in Figure Q4.17.

### 17. Write the 10 cardinalities that are appropriate for this ERD.


### 18. Write the business rules reflected in this ERD.


### 19. What two attributes must be contained in the composite entity between STORE and PRODUCT? Use proper terminology in your answer.


### 20. Describe precisely the composition of the DEPENDENT weak entity’s primary key. Use proper terminology in your answer.


### 21. "Youth League" Modelling

The local city youth league needs a database system to help track children who sign up to play soccer.  
Data needs to be kept on each team, the children who will play on each team, and their parents.  
Also, data needs to be kept on the coaches for each team.  
**Draw a data model with the entities and attributes described here.**  

Entities required: Team, Player, Coach, and Parent  

Attributes required: 
    * Team: Team ID number, Team name, and Team colors
    * Player: Player ID number, Player first name, Player last name, and Player age
    * Coach: Coach ID number, Coach first name, Coach last name, and Coach home phone number
    * Parent: Parent ID number, Parent last name, Parent first name, Home phone number, and Home address (Street, City, State, and Zip code)

The following relationships must be defined:
• Team is related to Player.
• Team is related to Coach.
• Player is related to Parent.

Connectivities and participations are defined as follows:
• A Team may or may not have a Player.
• A Player must have a Team.
• A Team may have many Players.
• A Player has only one Team.
• A Team may or may not have a Coach.
• A Coach must have a Team.
• A Team may have many Coaches.
• A Coach has only one Team.
• A Player must have a Parent.
• A Parent must have a Player.
• A Player may have many Parents.
• A Parent may have many Players.






