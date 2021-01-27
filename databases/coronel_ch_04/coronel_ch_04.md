# Chapter 4. Entity Relationship Modelling


### Question 1

**What two conditions must be met before an entity can be classified as a weak entity?  
Give an example of a weak entity.**  

The first condition states that weak entity is existence-dependent,  
meaning that particular instance of weak entity can not exist without relating the existent parent instance.  
The second condition - entity must have strong identifying relationship,  
which means that primary key of weak entity must contain as component primary key of parent entity. 

Example:

Species (sp_id, sp_name) --> Subspecies ([sp_id, subsp_id], name)  


### Question 2

**What is a strong (or identifying) relationship, and how is it depicted in a Crow’s Foot ERD?**  

Relationship in which primary key of related entity consists primary key of parent entity.  
In ERD strong relationship is depicted by solid line connection.  


### Question 3

**Given the business rule “an employee may have many degrees,”  
discuss its effect on attributes, entities, and relationships.  
(Hint: Remember what a multivalued attribute is and how it might be implemented.)**  

We have two entities: employee and degree.  
As long as attributes need to be atomic to conform the 1NF, we can't place them all in one cell.  
We need to establish Many-to-many relationship.  
Within relational model, such a kind of relationship is established through lookup entity,  
also called associative or composite entity.  
So, initial M:N relationship between two tables we transform to two 1:M relationships between three ones.  


### Question 4

**What is a composite entity, and when is it used?**  

Composite entity is used to convert conceptual M:N relationship,  
which can not be implemented within relational database directly, to actual database structure.  
Composite entity contains composite key that consists of primary keys of conceptual M:N relationship.  
Composite entity is used to avoid duplicating data and Nulls.  


### Question 5

**Suppose you are working within the framework of the conceptual model in Figure Q4.5.**  
**Given the conceptual model in Figure Q4.5:**
1. **Write the business rules that are reflected in it.**
2. **Identify all of the cardinalities.**

Figure depicts "car service" business scenario.  
Rules:
* Customer may have many cars or may haven't got any.  
* Each car may receive maintaince
* Maintaince may include 1:M Lines
* every Line have one Part
* Not every Part may exists in Line table


### Question 6

**What is a recursive relationship? Give an example.**  

Recursive is a unary relationship, meaning that only one table is participating in it.  
Although a table can represent only one object, we can encapsulate some 'sub-instances' within a table.  
For example, classical "person --> manager" business theme; the manager is related to person,  
and manager is also person.  


### Question 7

**How would you (graphically) identify each of the following ERM components in a Crow’s Foot notation?**  
1. **an entity**
1. **the cardinality (0,N)**
1. **a weak relationship**
1. **a strong relationship**

An entity is represented by rectangular.  
The cardinality is denoted by special signs (0, |, 'crowd foot').  
A weak relationships are connected with dashed line.  
A strong relationships are connected with solid line.  


### Question 8

**Discuss the difference between a composite key and a composite attribute.  
How would each be indicated in an ERD?**

Composite key is the set of key attributes that can uniquely identify each row within a table.  
In the ERD usually denoted by 'CPK' mark and underlined.  
Composite attribute is the attribute which value can be subdivided in several other attributes.  
In some cases composite attributes should be avoided in the ERD.  


### Question 9

**What two courses of action are available to a designer who encounters a multivalued attribute?**  

As opposite to single-valued attribute, multivalued attributes should not be implemented in database table.  
The first option is to split a multivalued attribute into several component attributes within the same table.
The other one is to create new entity composed of original multivalued attribute's components.  


### Question 10

**What is a derived attribute? Give an example.  
What are the advantages or disadvantages of storing or not storing a derived attribute?**  

**Derived attribute (computed)** is the attribute which **value can be determined by the values of another attribute(s)**.  
In this case, storing derived attributes in database saves computational time when data is queried,  
decreases data access time, and can be used to keep track of historical data.  
As disadvantages, more storage is needed.  
For example, person's age is **derived attribute** that **can be computed** from "birth_date" attribute.  


### Question 11

**How is a relationship between entities indicated in an ERD?  
Give an example using the Crow’s Foot notation.**  

The special graphemes are used to represent relationship between entities in entity relational modelling.  
Different kinds of lines links entities.  
Special symbols, known as 'crowds foot notation', are used to represent cardinalities between entities.  


### Question 12

**Discuss two ways in which the 1:M relationship between COURSE and CLASS can be implemented.  
(Hint: Think about relationship strength.)**  

The rule is 'course can generate multiple classes & class belongs to one course'.  
1. Course (course_id PK, course_name) -||---0< Class (class_id PK, class_room)
1. Course (course_id PK, course_name) -||---0< Class (course_id CPK FK, class_room CPK)

The first is example of non-identifying relationship.  
The second is strong identifying relationship, Class is weak entity.  


### Question 13

**How is a composite entity represented in an ERD, and what is its function? Illustrate the Crow’s Foot notation.**  

Composite entity (bridge entity, associative entity, linking table) exists to represent M:N conceptual  
relationship in database through creating additional associative entity.  
Original entities are related to associative through 1:M relationships.  
The primary key of composite entity is composed of primary keys of original entities.  


### Question 14

**What three (often conflicting) database requirements must be addressed in database design?**  

1. Database design
2. Informational requirements
3. Processing speed


### Question 15

**Briefly, but precisely, explain the difference between single-valued attributes and simple attributes.  
Give an example of each.**  

Single-valued - may have only one value for each instance (not necessarily unique).  
Examples: hex_color, first_name, total_amount.  

Simple (not composite) - is attribute which value is atomic and can not be subdivided.  
Examples: vehicle_identification_number, current_date_time, full_name.  


### Question 16

**What are multivalued attributes, and how can they be handled within the database design?**  

There are two ways to handle multivalued attributes:
1. Split attribute into several component attributes 
2. Split attribute into several component attributes, create separate instance, link to original 


Questions 17–20 are based on the ERD in Figure Q4.17.

### Question 17/18

**Write the 10 cardinalities that are appropriate for this ERD.**  
**Write the business rules reflected in this ERD.**

Each employee may have several dependants.  Each dependent have only one mentor.  
Each employee belongs to one store. Each store may have various employees.  
Each store may have various orders. Each order belongs to one store.  
Order contains at least one line. Each line belongs to only one order.  
Order line may have only one product. Product may be included in various lines.  


### Question 19

**What two attributes must be contained in the composite entity between STORE and PRODUCT?  
Use proper terminology in your answer.**  

Store_Products (store_id CPK, product_id CPK)
In composite entity 'store_products' composite primary key contains PKs of original entities.  


### Question 20

**Describe precisely the composition of the DEPENDENT weak entity’s primary key.  
Use proper terminology in your answer.**  

Weak entity is the entity with strong identifying relationship - weak entity's composite  
primary key contains primary keys of original entities.  
Weak entity can not exist independently of parent entity.  


### 21. "Youth League" Modelling

**The local city youth league needs a database system to help track children who sign up to play soccer.  
Data needs to be kept on each team, the children who will play on each team, and their parents.  
Also, data needs to be kept on the coaches for each team.  
Draw a data model with the entities and attributes described here.**  

Entities required: Team, Player, Coach, and Parent  

Attributes required: 
* Team: Team ID number, Team name, and Team colors
* Player: Player ID number, Player first name, Player last name, and Player age
* Coach: Coach ID number, Coach first name, Coach last name, and Coach home phone number
* Parent: Parent ID number, Parent last name, Parent first name, Home phone number, and Home address (Street, City, State, and Zip code)

The following relationships must be defined:
* Team is related to Player.
* Team is related to Coach.
* Player is related to Parent.

Connectivities and participations are defined as follows:
* A Team may or may not have a Player.
* A Team may have many Players.
* A Player must have a Team.
* A Player has only one Team.
* A Team may or may not have a Coach.
* A Team may have many Coaches.
* A Coach must have a Team.
* A Coach has only one Team.
* A Player must have a Parent.
* A Player may have many Parents.
* A Parent must have a Player.
* A Parent may have many Players.

Answer: **scan_ch4_rq21.jpg**
