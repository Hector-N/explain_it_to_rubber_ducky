# Lambda expression'

## Explain lambda function and its common usage?

## My answer

Syntax:
    lambda args: expression

Functional programming is paradigm that imposes usage of functions.  
Function - is a correlation of one input value to output.  
On the same input function produces same output.  

Usually, we define function with `def` keyword, giving it name.    
Lambda - is the way to create anonymous function, throw away functions.  
Lambda function is mainly used in functions that apply another functions.  

For example, one can sort list not only alphabetically, redefining sorting condition:
```python
li = ['tomatoes', 'ham', 'spam', 'eggs', ]
sorted(li, key=lambda el: len(el))
```

Lambda function is commonly used with 'not pythonic' `map()`, `filer()`, `reduce()`.

## Links to study:
* [(+)python-course.eu: Lambda, filter, reduce and map](https://python-course.eu/python3_lambda.php)
* [realpython.com: How to Use Python Lambda Functions](https://realpython.com/python-lambda/)
