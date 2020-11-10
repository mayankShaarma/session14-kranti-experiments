# Session 14 Iterables and Iterators
This assignment focuses on building and using custom python iterables and iterators
The test cases in this assignment are focused upon various properties of Polygon class like, immutable, lazy loading, and iterator functionality

Iterables:
Iterable is an object that
```bash
a) Implements __iter__ method <\n>
b) Method returns an iterator that can be used to iterate over the object
```

Iterator:
Iterator is an object which is used to iterate over an iterable object using __next__() method.
Iterators have __next__() method, which returns the next item of the object.
Every iterator is also an iterable, but not every iterable is an iterator.

LazyLoading:
Variables used in the generator expression are evaluated lazily in a separate scope when the next() method is called for the generator object
(in the same fashion as for normal generators). However, the in expression of the leftmost for clause is immediately evaluated in the current scope
so that an error produced by it can be seen before any other possible error in the code that handles the generator expression.

This assignment builds upon the preceding assignment on Sequence types (Session13) and the usage of property decorator
The following information is about Session13 assignment
The encapsualtion can be achieved by two approaches
1) getters and setters 2) Using property decorator

The code followed the 2nd approach i.e. using property decorator for the attributes
Sample usage of the property decorator is given below
```bash
@property
def attribute1(self):
	return self._attribute1
```
The above usage indicates to Python compiler to call the function whenever _attribute1 variable value to be fetched

By implementing the above methods, the attribute can be accessed, modified just as regular attribute
Some of the benefits of property decorator and setters are
1) Data validation before setting
2) Encapsulation of data [Hiding the internal formatting/validity checks etc.]
3) Lazy loading [The attributes will only be loaded at the time of retrieval]

```bash
Modules overview
```
#polygon.py
Contains Polygon classe which takes edges and circum radius as initializer arguments and computes various properties like interior angle, apothem etc.
Detailed list of properties are mentioned below
The test cases focused on whether lazy computation of attributes supported, the class is immutable or not
Along with computation of the properties, the Polygon class also supports the functionality to compare two Polygons for both equality and greater

#polygon_sequence_type.py
Contains Polygon_SeqType class which takes max edges and common circum radius as the initializer arguments and computes the maximum efficienct polygon
Also being Iterable, it also supports next(), iter() features.
The polygon objects, max_efficiency property are computed lazily and not pre-computed

#test_session14.py
Contains test cases for both Polygon and PolygonSeqType classes

```bash
Assignment objects are given below
```
Goal 1:
Refactor the Polygon class so that all the calculated properties are lazy properties,
i.e. they should still be calculated properties, but they should not have to get
recalculated more than once (since we made our Polygon class "immutable").

Goal 2:
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily
i.e. you can no longer use a list as an underlying storage mechanism for your polygons. You'll need to implement both an iterable, and an iterator.