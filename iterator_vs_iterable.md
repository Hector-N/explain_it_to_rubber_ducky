# Iterator vs Iterable

## Q: What is difference between iterator and iterable?

### Answer:

Loop - is a constract that allows to perform repeated code block executioin. 

One type of the loop is for loop - is achieved by iterating through 'counter'.

Counter in this context is object, which can consequitively generate values from specific range.  

Counter is iterator.

Iterator has `__next__` method and raises StopIterationError when exhausted.  
And it can only be used ones.  
 
Iterable - is an object from which we can derive an iterator,  
it must have either `__iter__` or `__getitem__` methods.
Sequential data types are iterables, containers too.

Python, often uses implicit iteration.  
We just pass to for loop iterable, that implicitly converted to iterator.  
Moreover, when we call `sum(list_ints)`, it also implicitly iterates over passed list.

## Q: Can you implement an iterator?

### Answer:
```python
class Iterator(object):
    """
    Create iterator for looping over sequential data type object.
    """
    
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.index:
            raise StopIteration
        else:
            self.counter += 1
            return self.data[self.counter - 1]


it = Iterator('magic in the air')
for word in it:
    print(word)
```

## And what about iterator over 'set'?

### Answer - 

-------> TODO <------

## Info to recap:
* [Iterators and Iterables (+)](https://python-course.eu/python3_iterable_iterator.php)
