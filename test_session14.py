import pytest
import string
import os
import inspect
import re
import string
import polygon
import polygon_sequence_type
import session14

README_CONTENT_CHECK_FOR = [
    'polygon',
    'property',
    'decorator',
    'iterable',
    'iterator',
    'immutable',
    'lazy'
]

INPUT_MODULES = [session14, polygon, polygon_sequence_type]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    for module in INPUT_MODULES:
        lines = inspect.getsource(module)
        spaces = re.findall('\n +.', lines)
        for space in spaces:
            assert len(space) % 4 == 2, "Your script contains misplaced indentations"
            assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    for module in INPUT_MODULES:
        functions = inspect.getmembers(module, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_doc_string():
    #Checking the functions written in Polygon and PolygonSeqType classes
    for module in INPUT_MODULES:
        functions = inspect.getmembers(module, inspect.isfunction)
        for function in functions:
            print(function)
            assert len(function[1].__doc__) > 50, "In a hurry? Not all functions have >50 docstring!"

def test_immutability():
    #Checking the immutability of the class Polygon
    assert True == session14.check_immutability_polygon(), "Polygon Class is not immutable"

def test_lazy_loading_polygon():
    #Checking whether Polygon class attributes are computed only required or pre-computed
    assert True == session14.check_lazy_property_loading_polygon(), "You lazy person! Pre-computing all the properties, beforehand!"

def test_iterable_polygon_seq():
    #Checking whether the PolygonSeqyType class is iterable or not
    assert True == session14.check_iterable(), "PolygonSeqType is not an Iterable!"

def test_iterator_polygon_seq():
    #Checking whether the PolygonSeqyType class is iterator or not
    assert True == session14.check_iterator(), "PolygonSeqType is not an Iterator!"

def test_lazy_loading_polygon_seq():
    #Checking whether PolygonSeqType class attributes are computed only required or pre-computed
    assert True == session14.check_lazy_property_loading_polygon_seq(), "You lazy person! Pre-computing all the properties, beforehand!"
