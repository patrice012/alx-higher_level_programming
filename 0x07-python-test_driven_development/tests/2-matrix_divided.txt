The ``2-matrix_divided.py`` module
==================================

Using: ``matrix_divided``
------------------------

Usage: ``matrix_divided`` divides all elements of a matrix.
-----
by the given number

::
	>>> matrix_divided = __import__("2-matrix_divided_1").matrix_divided
	
test module docstring
    >>> m = __import__("2-matrix_divided").__doc__
	>>> len(m) > 1
	True

test function docstring
    >>> f = __import__("2-matrix_divided").matrix_divided.__doc__
    >>> len(f) > 1
    True

	>>> matrix_0 = [
	...	[1, 2, -4],
	...	[0, 0, 0]]
	>>> matrix_divided(matrix_0, 2)
	[[0.5, 1.0, -2.0], [0.0, 0.0, 0.0]]
	>>> matrix_1 = [
	...	[1, 2, 3],
	...	[4, 5, 6]]
	>>> matrix_divided(matrix_1, 1)
	[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
	>>> matrix = [
	... [1, 2, 3],
	... [4, 5, 6],
	... [12, 48, 7845]]
	>>> matrix_divided(matrix, 5)
	[[0.2, 0.4, 0.6], [0.8, 1.0, 1.2], [2.4, 9.6, 1569.0]]
	>>> matrix_2 = [
	... [12, 45],]
	>>> matrix_divided(matrix_2, 5)
	[[2.4, 9.0]]
	>>> matrix_3 = [
	... [125, 45, 789, 1, 45],
	... [44, 87,]]
	>>> matrix_divided(matrix_3, 5)
	Traceback (most recent call last):
		...
	TypeError: Each row of the matrix must have the same size
	>>> matrix_4 = [
	... ["hello", 4, 47],
	... [8, 5, 9]]
	>>> matrix_divided(matrix_4, 5)
	Traceback (most recent call last):
		...
	TypeError: matrix must be a matrix (list of lists) of integers/floats
	>>> matrix_4_1 = [
	... [145, 7, 5],
	... [8, "ALX", 9]]
	>>> matrix_divided(matrix_4_1, 5)
	Traceback (most recent call last):
		...
	TypeError: matrix must be a matrix (list of lists) of integers/floats
	>>> matrix_5 = [
	... "hello", 2, [1, 5, 8]]
	>>> matrix_divided(matrix_5, 5)
	Traceback (most recent call last):
		...
	TypeError: matrix must be a matrix (list of lists) of integers/floats
	>>> matrix_divided(matrix, 0)
	Traceback (most recent call last):
		...
	ZeroDivisionError: division by zero
	>>> matrix_divided(matrix, -4)
	[[-0.25, -0.5, -0.75], [-1.0, -1.25, -1.5], [-3.0, -12.0, -1961.25]]
	
	
testing function with scalar division with double digit div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 22)
    [[0.05, 0.09, 0.14], [0.18, 0.23, 0.27]]

testing function with scalar division with negative div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], -2)
    [[-0.5, -1.0, -1.5], [-2.0, -2.5, -3.0]]

testing function with scalar division with zero div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

testing function with scalar division with string div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], "2")
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

testing function with scalar division with list div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], [2])
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

testing function with scalar division with tuple div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], (2,))
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

testing function with scalar division with dict div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], {2: 2})
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

testing function with scalar division with float div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2.0)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

testing how function handles None argument
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], None)
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

testing how function handles None matrix
    >>> matrix_divided(None, 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

testing how function handles non-list matrix
    >>> matrix_divided(2, 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

testing how function handles non-list matrix
    >>> matrix_divided("2", 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

testing how function handles non-list matrix
    >>> matrix_divided((2,), 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

testing how function handles non-list matrix
    >>> matrix_divided({2: 2}, 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

test single element in matrix
    >>> matrix_divided([[3]], 3)
    [[1.0]]

test with negative div
    >>> matrix_divided([[3, 9], [12, 15]] , -3)
    [[-1.0, -3.0], [-4.0, -5.0]]
