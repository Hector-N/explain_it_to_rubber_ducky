# Hashable in Python


**Hashable** - is a characteristic of an object to indicate whether the object has a hash value,  
which allows the object to serve as a key in a dictionary or be an element in set.  


An object is hashable if it has a hash value that doesn't change during its lifetime.  


Hashing an object can be thought as converting it to an integer based on its content,  
but not on the identity of the object itself.  


**Hashing function (hasher)** - A function that computes the hash.  
```raw_data_value --> hasher --> hash value```   
It must be consistent - return the same value for the same object.  
The same hash value for different (not equal) objects is computed - collision occurs.  


Hashable is closely tied with concept of **mutability**.  
All hashable objects are immutable.  
**Hashable** objects are integer, float, string, tuple, None  
**Non-hashable** - dictionary, set, list  


Object which are instances of custom defined classes are hashable. 
They all compare unequal, and their hash value is their id.  


Immutable data types in Python come with a built-in method `__hash__` for computing their hash value.  
The hash value depends only on the data stored, not on the identity of an object itself.  


Mutable objects doesn't have `__hash__` method.  

 
`__eq__()` function is used to compare the object with another object for equality,  
and it’s also required that objects that compare equal should have the same hash value.


By default, custom class instances are compared by comparing their identities using the built-in `id()`  

