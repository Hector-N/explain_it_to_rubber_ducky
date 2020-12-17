# What is difference between iterator and iterable?

## Answer

Loop - is a constract that allows to perform repeated code block executioin. 

One type of the loop is for loop - is achieved by iterating through 'counter'.

Counter in this context is object, which can consequitively generate values from specific range.  
Counter is iterator.

Iterator has __next__ method and raises StopIterationError when exhausted.  
And it can only be used ones.  
 
Iterable - is an object from which we can derive an iterator.  
Sequential data types are iterables.

Python, often uses implicit iteration. We just pass to for loop iterable,  
that implicitly converted to iterator.

## Info to recap:
* [Iterators and Iterables](https://python-course.eu/python3_iterable_iterator.php)
