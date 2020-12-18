# Iterators and Generators

## Explain difference between this terms

### My answer:
Iterator is abstraction, that allows to access elements of data object one at a time,  
without any knowledge of internal structure or this object.  
It operates on predefined set of values, and while exhausted, throws StopIteration.  
Iterators use lazy evaluation principle - delay the evaluation until value is needed.  
Iterator can be seen as a pointer to specific element of a container.

Generator - is a construct that allows to create iterators.  
We can implement generators using OOP approach, but it isn't a pythonic way.  
Pythonic way is to use generator function.  
The main difference with ordinary python function is that generator preserves  
its state among the calls.

Work of generator:
* define function with yield statement
* initialize generator to get generator object (is iterator)
* use generator object in a loop, or it's __next__ method to produce results

After `next()` is calls on generator object, it produces a result  
and interrupt its execution, preserving state of variables.  
After a generator receives another `next()` it resumes execution of body.  
When body of generator exhausted it raises `StopIterationError`.  
In generator body, `return` statement is equivalent to StopIteration exception.

Generator not only capable of sending data, but receiving too.  
Using `next()` we implicitly send to generator object `None`.  
Using `send()` we assign value to variable to the left of `yield` statement.  
Also, there is `throw` method, which allows sending Exception to generator.  
This exception must be caught inside the body of generator function.

## [Practice task list](https://python-course.eu/python3_generators.php#Exercises):
- [x] Write a generator which computes the running average.
- [ ] Write a generator frange, which behaves like range but accepts float values.
- [ ] Write a generator trange, which generates a sequence of time tuples.
- [ ] Write a version "rtrange" of the previous generator, which can receive messages to reset the start value.
- [ ] Write a program, using the newly written generator "trange" to create a file "times_and_temperatures.txt".  
- [ ] Write a generator with the name "random_ones_and_zeroes".
- [ ] Rewrite a class Cycle in the beginning of this chapter. 

## Info to study:
* [python-course.eu -> Generators and Iterators (+-)](https://python-course.eu/python3_generators.php)
