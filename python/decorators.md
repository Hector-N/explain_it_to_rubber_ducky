# Decorators

## Q: What is a decorator?
## My answer
~~Decorator is function that modifies behaviour of other function (or callable).~~  
Decorator is a callable object that takes as parameter another callable object  
and returns this object modified.  
Decorators are used to modify function, method or class behaviour.  

## Q: The purpose of decorators?
## My answer
Decorator syntax is used for adding additional features to callables,  
while separating main semantics and introduced changes.  

## Q: Usecases for decorators?
## My answer
* validating arguments
* function call count
* tracking function execution time
* memoization

## Q: Write a decorator that do not override original function's attributes?
## Answer
```python
def prefix(mr_ms):
    def add_prefix_decorator(f):
        def wrapper(x):
            return f"{mr_ms}{f(x)}"
        # overriding wrapper function attributes
        # so when decoration will be performed, it preserves original function's attributes
        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        wrapper.__module__ == f.__module__
        return wrapper
    return add_prefix_decorator


def greet(name):
    return f"{name}, ¡buenos dias!"


greeting_mr = prefix('Mr. ')(greet)
greeting_ms = prefix('Ms. ')(greet)

print(greeting_mr('Igor'))
print(greeting_ms('Marisha'))
```

## Link to study:
* [python-course.eu: Decorators](https://python-course.eu/python3_decorators.php)
