# Explain inheritance, encapsulation, abstraction, polymorphism


## Inheritance

Inheritance - is a basic concept of oop, according to which a child class inherits  
class attributes and class methods from parent class.  

BaseClass (parent class)   <--inherits--   DirectClass (child class)


## Encapsulation

**Encapsulation** - another fundamental concept of OOP, is wrapping data in the methods that work on data within one unit.  
This puts some restriction on accessing variables and methods, it can prevent accidental modification of data.

To prevent accidental change, an object variable can only be changed by an object's method.  
This type of variables is known as **privat variable**.  
In Python privat variable name is preceded with double underscore '__spam',  
and can be used only within class itself.  
Moreover, Python hides even the existence of privat variables and methods from users of the class.  
In such a way, Python implement protection of privat variables.  

Another type of attribute is **protected** - is supposed to be used only by child class.  
Python doesn't implement this concept and only has a naming convention to precede names of protected  
attributes with single underscore '_'.  

**Public** attributes - everybody has access to them, whenever you like.  


## Abstraction

**Abstraction** - natural extension of encapsulation.  

While programs become larger, we keep them logical and simple by applying principles of abstraction.
Each class should only exposes its mechanisms that need to be public.  
All the behind teh scenes mechanisms should only be encapsulated and left privat.  

Whenever you don't need to show the user what class doing behind the scenes, then just make method privat.  
Because only specific class has the need to access those specific method, then it should be privat.  
Otherwise, you should make the method public or protected.  


## Polymorphism

**Polymorphism** - having many forms; the same function but with different signature is being used for different times.  

In Python polymorphism allows us to define methods in the child class with the same method name as in parent class.  

In other words, it is possible to modify method in a child class, that did have inherited from the parent class.  
Reimplement method in the child class - is the process known as "method overriding".  
