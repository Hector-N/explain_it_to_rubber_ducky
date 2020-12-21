# Memoization in computing

## What is memoization?
## My answer
Memoization is a technique, that allows functions to avoid computing  
output twice.  
It is a trade between computational time and disk storage.  
When there is the same input to function, and the function doesn't have  
side effects (pure), function can use an inner cache to store already  
calculated results and reuse them.  
In general, this technique is known as caching, and it is not new.  

Memoization can be used effectively:
* when function's computation is intensive and function called repeatedly
* the function is recursive


## Q: Ok, what is 'pure' function?
## Answer
A function may be considered 'pure' when it does not have side effects.  
In context of programming language it means that function doesn't modify  
any objects outside its scope.  
Often, there may be intentionally programmed side effects in functions.  

## Links to study:
* [python-course.eu: Memoization with Decorators](https://python-course.eu/python3_memoization.php)
* [medium: WTF is Memoization](https://chialunwu.medium.com/wtf-is-memoization-a2979594fb2a)
