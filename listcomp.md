# List Comprehensions

## Q: What we can achieve with 'list comprehension'?

## My answer
List comprehensions is the way to create lists.  
Listcomp - is a construct that simulates `for` loop to create list  
With it, code is more concise an compact.  

In some cases we can't substitute the `for` loop with list comprehensions.  
For example, when we need output additional info (counter, log)  
form the body of the `for` loop.  

## Q: Can we simulate nested loops with listcomps?

## My answer
Yes. Naturally, as we use deeper nesting to create a nested loop,  
the same way one can achieve identical result with listcomps.
For example, one can create time tuples with hours and minutes:
```python
time_points = [(hour, minute) 
               for hour in range(1, 13) 
               for minute in range(1, 61)]
time_points_2 = []
for hour in range(1,13):
    for minute in range(1, 61):
        time_points.append((hour, minute))
```

## Links to study:
* [python-course.eu: List Comprehension](https://python-course.eu/python3_list_comprehension.php)
*
