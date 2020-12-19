# `zip` function

## What is the purpose of `zip` function. Give some examples.

### Answer
Is a king of ~~mapping~~ combining elements into tuples,  
when every element from given objects ~~(two or more)~~  
combines with corresponding element of those objects.
Result of zip operation - is zip object, which can generate combined groups one at a time.
Iterator throws StopIteration as long as the shortest of the iterables is exhausted.

Example:  
```python
# 1
colors = ['red', 'green', 'blue']
color_values = [(256, 0, 0), (0, 256, 0), (0, 0, 256)]
zip_obj = zip(colors, color_values)
for col in zip_obj:
    print(col)
color_codes = list(zip_obj)  # result is [] as zip object is exhausted

# 2
dictionary = dict(zip(colors, color_values))
```

## Links:
* [python-course.eu: Zip Introduction](https://python-course.eu/python3_zip_tutorial.php)
