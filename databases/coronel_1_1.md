# Coronel C., Morris S. -  Database Systems Design, Implementation, & Management, 13th edition - 2019

## Review questions. Part 1, chapter 1


### 1. Define such terms as 'data', 'field', 'record', 'file'

In the context of a File Based Data Management System these terms mean:  
A data - is a raw, structured information related to particular world objects or concepts.  
A field - is a particular characteristic of the data set, data property.  
A record - captured information about a particular object.    
A file - references to a collection of data about a specific domain.  


### 2. What is data redundancy, and which characteristics of the file system can lead to it?

Data redundancy - is when the same data is presented in different places.  
File system may store the same data in different places; data may be duplicated within one place.  


### 3. What is data independence, and why is it lacking in file systems?

The software that interact with file system rely on particular data format.  
There is a difference between the logical data format, and the physical data format.  
Programs that assess data must know not only what to do with data,  
but how to do it.  
In such a programs one must explicitly declare data characteristics and types.


### 4. What is a DBMS, and what are its functions?

In broadest sense, the DBMS is a complex of activities,  
created to maintain data in such a way that guarantee its integrity - the overall quality of the data.  
DBMS is a software that serves as intermediary between users and database,  
it manages and controls database activities.  
In other words DBMS creates, processes and administers the databases it controls.  


### 5. What is structural independence, and why is it important?

The ability to access to the data must not be dependent on changing its structure.  
For example, that's why using 'all' clause in 'select' query is considered bad practice.  
Thus, we eliminate structural dependence.  


### 6. Explain the differences among data, information, and a database.

Data - raw facts.  
Information - data + context + interpretation.  
Database - structured collection of related data.  


### 7. What is the role of a DBMS, and what are its advantages? What are its disadvantages?

DBMS allows safely store, process, retrieve data. It guarantees data integrity, security, persistence.  
It has higher cost to maintain as opposite to its advantages.   


### 8. List and describe the different types of databases.

Databases may be characterized based on a different criterion:

* Number of users:
    * personal - support single user at a time, no concurrency
    * organizational - can be used in small organizations, support security, concurrency.
    * corporate - support primary performance, used with big amounts of data.
* Purpose
    * analytical - provide tools to perform data analysis 'on the fly' or 'more deep analysis'
    * production - support large amount of transactions and concurrency
    * embedded - used in different devices as internal storage
    * cloud - provide service of maintaining database by third party organization
* partitioning
    * centralized - data is located in one place
    * distributed - data is distributed in different locations
* storage environment
    * in-memory
    * disk storage


### 9. What are the main components of a database system?

* Users
* DB applications
* DBMS
* database itself


### 10. What is metadata?

Data that explains other data that has particular interest to us.  
Databases store additional info about its data, data structure and characteristics.  
That's why database is self-described collection of related data.


### 11. Explain why database design is important.

In order to achieve quality of stored data, we need to define the way it stored, accessed and changed.  
Doing that allows escape common fails while maintaining database system.  
Database design - is a complex of steps to guarantee data quality.  


### 12. What are the potential costs of implementing a database system?


### 13. Use examples to compare and contrast unstructured and structured data. Which type is more prevalent in a typical business environment?


### 14. What are some basic database functions that a spreadsheet cannot perform?

* establish relationships
* maintain referential integrity of the data
* backup and recovery
* data access restrictions


### 15. What common problems do a collection of spreadsheets created by end users share with the typical file system?

Storing data in different places gives us so-called multiple islands of information.  
Each user introduces its own vision on the same data, and consequently represents data differently.  
It leads to data inconsistency and data anomalies.  


### 16. Explain the significance of the loss of direct, hands-on access to business data that end users experienced with the advent of computerized data repositories.


### 17. Explain why the cost of ownership may be lower with a cloud database than with a traditional, company database.
