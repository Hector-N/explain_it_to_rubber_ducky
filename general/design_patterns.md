# What is design pattern? Explain strategy design pattern.

Design patterns - is the language independent recepies to common tasks or problems.  
Language independent means that we have general schemas to solve problems.  
But the specifics of each programming language often modifies implementatioin and usage of classic set of design patterns.  

Strategy design pattern is needed when we want to modify algorythm according to some external attributes or context.  
The schema consists of:
* abstract base class - strategy 
* set of concrete classes - variations of the stratgy
* context - user of the strategy

Computing discounts based on customer fidelity and order characteristics is a good example of strategy design pattern. 
