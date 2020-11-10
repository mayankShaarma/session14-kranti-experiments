#polygon.py
import math

class Polygon:

    def __init__(self, edges_val, circum_radius_val):
        '''
        Class Initializer - Runs once an instance is created for the class
        Before setting values, checks for the validity of input variables and raise ValueError for invalid inputs
        '''
        if(edges_val <= 2 or circum_radius_val <= 0 or not isinstance(edges_val, int) or
            (not isinstance(circum_radius_val, int) and not isinstance(circum_radius_val, float))):
            raise ValueError(f'Not Supported Inputs {edges_val}, {circum_radius_val}')
        self._edges = edges_val #n
        self._circum_radius = circum_radius_val #R
        self._vertices = None
        self._angle = None
        self._apothem = None
        self._area = None
        self._edge_len = None
        self._perimeter = None
        self._strictconvex = None
        self._vertices = None


    def __iter__(self):
        return None

    def __next__(self):
        return None

    @property
    def edges(self):
        '''
        Getter function for edges variable
        Returns the edges of the Polygon to the caller
        '''
        return self._edges

    @property
    def circum_radius(self):
        '''
        Getter function for circum_radius variable
        Returns the circum_radius of the Polygon to the caller
        '''
        return self._circum_radius

    @property
    def vertices(self): #n
        '''
        Getter function for verices variable
        This is a private variable and is same as edges for a Convex Polygon
        '''
        if self._vertices is None:
            print('Setting vertices')
            self._vertices = self._edges
        return int(f'{self._vertices}')

    @property
    def interior_angle(self): #A
        '''
        Getter function for interior_angle variable
        This is a private variable and computed using the formula: (n-2)*180/n [n - Edges]
        '''
        if self._angle is None:
            print('Calculating interior angle')
            self._angle = ((self._edges - 2) * 180/self._edges)
        return float(f'{self._angle:.4f}')

    @property
    def edge_length(self): #s
        '''
        Getter function for edge_length variable
        This is a private variable and computed using the formula: 2*R*Sin(Pi/n) [R: CircumRadius, n: Edges]
        '''
        if self._edge_len is None:
            print('Calculating edge_len')
            self._edge_len = (2 * self._circum_radius * math.sin(math.pi/self._edges))
        return float(f'{self._edge_len:.4f}')

    @property
    def apothem(self): #a
        '''
        Getter function for apothem variable
        This is a private variable and computed using the formula: R*Cos(Pi/n) [R: CircumRadius, n: Edges]
        '''
        if self._apothem is None:
            print('Calculating apothem')
            self._apothem = (2 * self._circum_radius * math.cos(math.pi/self._edges))
        return float(f'{self._apothem:.4f}')

    @property
    def area(self): #nsa/2
        '''
        Getter function for area variable
        This is a private variable and computed using the formula: (n*s*a)/2 [n: Edges, s: Apothem]
        '''
        if self._area is None:
            print('Calculating area')
            self._area = (self._edges * self.edge_length * self.apothem)/2
        return float(f'{self._area:.4f}')

    @property
    def perimeter(self): #ns
        '''
        Getter function for perimeter variable
        This is a private variable and computed using the formula: (n*s) [n: Edges, s: Apothem]
        '''
        if self._perimeter is None:
            print('Calculating perimeter')
            self._perimeter = (self._edges * self.edge_length)
        return float(f'{self._perimeter:.4f}')

    @property
    def isstrictconvex_polygon(self):
        '''
        Getter function for is strict convex polygon property
        This is a private variable and is computed based on interior angle and edge length
        A strict regular convex polygon is a polygon, with all its interior angles < 180 and all sides have equal length
        '''
        if self._strictconvex is None:
            print('Setting strictconvex polygon or not')
            self._strictconvex = (self._angle < 180)
        return self._strictconvex

    def __repr__(self):
        return f'Polygon(Edges, n = {self._edges}, CircumRadius, R = {self._circum_radius})'

    def __str__(self):
        return f'Polygon Edges, n = {self._edges} CircumRadius, R = {self._circum_radius}'

    def __eq__(self, other):
        '''
        Equality Comparison
        If the input object is of type Polygon
            its vertices and circum_radius are same as that of the current object
            then
                returns True
            else
                returns False
        Else
            Raises ValueError
        '''
        if isinstance(other, Polygon):
            return (self.vertices == other.vertices and self._circum_radius == other._circum_radius)
        else:
            raise ValueError(f'The input object{other} is not of Polygon type')

    def __gt__(self, other):
        '''
        Greater Than Comparison
        If the input object is of type Polygon
            Compares the vertices of both objects and returns True or False
        Else
            Raises ValueError
        '''
        if isinstance(other, Polygon):
            return self.vertices > other.vertices
        else:
            raise ValueError(f'The input object{other} is not of Polygon type')