# Ch. 3 - The Relational Database Model - review questions


## 1. What is the difference between a database and a table?

A table may be considered as a persistent entity set.  

Database is a collection of tables.  

 
## 2. What does it mean to say that a database displays both entity integrity and referential integrity?

Database structure guarantees presence of primary keys (ensure entity integrity)  
and foreign keys (ensure referential integrity) as well as mechanism to maintain integrity.  


## 3. Why are entity integrity and referential integrity important in a database?

They are the basis for a data consistency.  


## 4. What are the requirements that two relations must satisfy to be considered union-compatible?

To be considered union compatible two relations must have the same number of attributes and  
corresponding attributes must be of the same domain type.  


## 5. Which relational algebra operators can be applied to a pair of tables that are not union-compatible?

To make tables union compatible one can apply 'project' operator that yields vertical subset of the relation.  


## 6. Explain why the data dictionary is sometimes called “the database designer’s database.”

Data dictionary stores the definition of data elements and their relationships.  
The DBMS uses data dictionary to lookup the required by application data component structures and relationships,  
thus providing data abstraction and removing structural and data dependence from the system.  


## 7. A database user manually notes that “The file contains two hundred records, each record containing nine fields.”  Use appropriate relational database terminology to “translate” that statement. 

The _table_ contains _N_ _rows_, each row contains nine _attributes_.  


## 8. Using the STUDENT and PROFESSOR tables, illustrate the difference between a natural join, an equijoin, and an outer join.

Natural join - yields a product of joined tables, restricted by intersection of common attributes.  

Equijoin - analog of natural join but doesn't get rid of common attribute (included several times in result).  

Outer join - is an extension of join; result of applying several relational algebra operators:
* A JOIN returns the matched tuples
* DIFFERENCE operator applied to find unmatched tuples
* unmatched tuples combined with NULL values through a PRODUCT
* UNION combines results.


## 9. Create the table that would result from πstu_code (student).

Here we required to apply unary 'project' operator to the table to get a vertical subset of the table.  
Vertical subset - all values of specified attribute or attributes in order that they appear.  


## 19. What are homonyms and synonyms, and why should they be avoided in database design?

Homonyms - the names of attributes that have similar sounding but different meaning.  
For example C_NAME may be referred both as 'customer name' or as 'consultant name'.  

Synonyms - within a database, indicates the use of different names to describe the same attribute.  
Car and Auto are synonyms.  
