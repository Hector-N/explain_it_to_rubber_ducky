# What is constant folding?

Constant folding is when a language replaces your constant expressions at compile time  
rather than computing them at runtime.  

It allows precomputing constants while compiling code, and use them at every run.  

Constant expressions - the expressions involving immutable types and returning immutable type.  

`days_ind_seconds = 24 * 60 * 60`

Python converts this to single value at bytecode time.  

Python tries to fold lots of constants, but not all.  
If precomputed value is too big - no folding occurs.  

**Advise**: Remember to not try to pre-compute constants while coding.  
Make them easy to read and Python will handle the optimization for you.  



