# session14.py

"""
Times how long a snipped of code takes to run
over multiple iterations
"""

from polygon import Polygon
from polygon_sequence_type import PolygonSeqType

def check_immutability_polygon():
    """
    Checks if Polygon class attributes can be changed or not
    """
    poly_one = Polygon(3, 4)
    id_one = id(poly_one)
    print(f'{poly_one.__repr__()}')
    print("Id(poly1): ", id_one)

    """
    Setting new values for the attirbuted edges
    This operation should throw Attribute Error
    """
    try:
        poly_one.edges = 4
        id_two = id(poly_one)
        if(id_one == id_two):
            print('Polygon class allowing to set the attributes and is not immutable - against its requirements')
        return False
    except AttributeError as e:
        print(e)
        return True


def check_lazy_property_loading_polygon():
    """
    Checks if Polygon class attributes are loaded into memory only when required or pre-computed before hand
    """
    poly_one = Polygon(3, 4)
    """
    poly_one object has multiple attributes such as apothem, edge_length, interior_angle, apothem etc
    All these properties should be computed only when required but not available always
    Calculate area again, since it was already computed when the object was created, the area should not be computed again
    """
    print(f'{poly_one.area}')
    if 'Calculating area' in f'{poly_one.area}':
        print('Area is recomputed - Not lazy loading')
        return False

    """
    Calculate interior angle again, since it was already computed when the object was created, the area should not be computed again
    """
    if 'Calculating interior angle' in f'{poly_one.interior_angle}':
        print('Interior Angle is recomputed - Not lazy loading')
        return False
    return True

def check_iterable():
    """
    Checks if PolygonSeqType class is an iterable or not
    """
    try:
        x1 = PolygonSeqType(5, 6)
        if '__iter__' not in dir(x1):
            return False
        iter(x1)
        return True
    except TypeError:
        return False

def check_iterator():
    """
    Checks if PolygonSeqType class is an iterator or not
    """
    try:
        x1 = PolygonSeqType(5, 6)
        for item in x1:
            pass
        return True
    except TypeError:
        return False

def check_lazy_property_loading_polygon_seq ():
    """
    Checks if PolygonSeqType class attributes are loaded into memory only when required or pre-computed before hand
    """
    poly_seq = PolygonSeqType(5, 4)
    """
    The attributes of poly_seq object are created only when an element is accessed
    Hence the value of maximum efficiency will be changing based on the objects accessed by the application
    """
    #Access Max Efficiency for the poly_seq object -> It returns zero since no item is accessed from poly_seq object
    if 'Yet to calculate' not in poly_seq.max_efficiency:
        print('Max Efficiency is non-zero, was it pre-computed?')
        return False
    #Creates a polygon with edges 3, circum_radius = 4
    #Also the maximum efficiency will be calculated only for this element
    poly_seq[0]
    if 'Max Efficiency Polygon is Polygon(Edges, n = 3' not in poly_seq.max_efficiency:
        print('Max Efficiency is not computed for Polygon of length \'3\'')
        return False
    return True
