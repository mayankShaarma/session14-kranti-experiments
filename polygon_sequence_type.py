#polygon_sequence_type.py
from polygon import Polygon

class PolygonSeqType:
    def __init__(self, max_vertices, common_radius):
        '''
        Class Initializer - Runs once an instance is created for the class
        Before setting values, checks for the validity of input variables and raise ValueError for invalid inputs
        '''
        if(max_vertices <= 0 or common_radius <= 0 or not isinstance(max_vertices, int) or
            (not isinstance(common_radius, int) and not isinstance(common_radius, float))):
            raise ValueError(f'Not Supported Inputs {max_vertices}, {common_radius}')
        self._max_vertices = max_vertices
        self._common_radius = common_radius
        self._polygons = []

    def __iter__(self):
        return self.PolygonIter(self)#self._max_vertices, self._common_radius, self._polygons)

    class PolygonIter:
        def __init__(self, poly_obj):#, max_vertices, common_radius, polygons):
            #self._max_vertices = max_vertices
            #self._common_radius = common_radius
            #self._polygons = polygons
            self._poly_obj = poly_obj
            self.index = 3

        def __iter__(self):
            return self

        def __next__(self):
            if self.index > self._poly_obj._max_vertices:
                raise StopIteration
            else:
                try:
                    result = self._poly_obj._polygons[self.index]
                except IndexError:
                    result = Polygon(self.index, self._poly_obj._common_radius)
                    self._poly_obj._polygons.append(result)
                self.index += 1
                return result

    def __len__(self):
        '''
        Getter function for length of the sequence type
        For a polygon, minimum number of vertices = 3
        Keeping that in mind, input is of maximum number of vertices,
        working it backward subtracting 2 from maximum vertices gives the possible number of polygons
        '''
        return (self._max_vertices - 2)

    def __getitem__(self, p):
        '''
        Getter function for next Polygon item
        '''
        if isinstance(p, int):
            if p < 0:
                p += len(self)
            if p < 0 or p >= len(self):
                raise IndexError(f'{type(self).__name__} __getitem__ index [{p}] is out of range')
            try:
                result = self._polygons[p+3]
            except IndexError:
                result = Polygon(p+3, self._common_radius)
                self._polygons.append(result)
                self._max_efficiency = None
            return result

    @property
    def max_vertices(self):
        '''
        Getter function for edges variable
        Returns the edges of the Polygon to the caller
        '''
        return self._max_vertices

    @property
    def common_radius(self):
        '''
        Getter function for circum_radius variable
        Returns the circum_radius of the Polygon to the caller
        '''
        return self._common_radius

    @property
    def max_efficiency(self): #A
        '''
        Getter function for max efficient Polygon
        This is a private variable and computed as highest area to perimeter ratio of available Polygons
        '''
        try:
            print('Calculating Max Efficiency Polygon')
            sorted_polygons = sorted(self._polygons, key=lambda p: p.area/p.perimeter, reverse=True)
            self._max_efficiency = sorted_polygons[0]
            return f'Max Efficiency Polygon is {self._max_efficiency.__repr__()}'
        except IndexError:
            self._max_efficiency = 0
            return f'Yet to calculate Max Efficiency [{self._max_efficiency.__repr__()}]-- access some objects of Polygon'

    def __repr__(self):
        return f'PolygonSeqType(Vertices (of largest Polygon) = {self._max_vertices}, Common Circum_Radius, R = {self._common_radius})'