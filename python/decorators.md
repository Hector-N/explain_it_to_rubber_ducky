# Decorators

## Q: What is a decorator?
## My answer
Decorator is function that modifies behaviour of other function (or callable).  

## Q: The purpose of decorators?
## My answer
Decorator syntax is used for adding additional features to callables,  
while separating main semantics and introduced changes.  

## Q: Examples of decorators?
## My answer
```python
def calls_track(f):
    def wrapper(n):
        wrapper.calls += 1
        return f(n)
    wrapper.calls = 0
    return wrapper

@calls_track
def mult_2(n):
    return n * 2


```




## Link to study:
* [python-course.eu: Decorators](https://python-course.eu/python3_decorators.php)
