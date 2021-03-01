# What is duck typing?


**Typing** - is the feature of a programming language that allows to classify objects and, as a consequence, use them properly.

There are **static** and **dynamic** typing.  
Static typing performed at a compile-time.  
Dynamic - means 'at a runtime'.  

Python is dynamically typed language. It uses duck typing.

Duck typing (simple) - if it quacks and if it flies, that probably it is a duck. 
Duck typing (serious) - a test for suitability of the object.  
In **normal typing** it determines by object type, in **duck typing** - by presence certain methods and properties.  

In practice, duck typing means that if we define and use custom type,  
we need to implement only those protocol features that we need in order to state that our object is ready to use.  
