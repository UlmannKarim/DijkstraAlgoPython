# KARIM ABDUL ULMANN 119329701

from graphsAssignment import *
from APQ import *


class RouteVertex(Vertex):

    def __init__(self, element, gps):
        super().__init__(element)
        self._gps = gps

    def __str__(self):
        string = str(self._element) + ', ' + str(self._gps[0]) + ',' + str(self._gps[1])
        return string


class RouteMap(Graph):
    # override init
    def __init__(self, file):
        self._structure = dict()
        self._vertexElement = dict()  # dict to maintain vertex object reference as key and element as the value
        self._elementVertex = dict()  # dict to maintain element as key and vertex object reference as the value
        self._vertexCoordinates = dict()  # to maintain the coordinates according to the vertex
        self.graphreader(file)

    def add_vertex(self, element, gps):
        """ Add a new vertex with data element.
        """
        v = RouteVertex(element, gps)  # modified vertex
        self._structure[v] = dict()  # maybe this is causing the problem??
        self._vertexElement[v] = v._element  # store object as key and element as value
        self._elementVertex[v._element] = v  # store element as key and object as value
        self._vertexCoordinates[v._element] = gps  # store element as key and coordinates are the values in the form of tuple floats
        return v

    def sp(self, v, w):
        # call your implementation of Dijkstra's method for source v
        # and receive the table structure in return
        # (this should tell us, for each vertex, what the cost of the path from v was,
        # and what the preceding vertex was on that path. From this structure,
        # your method should create a list of the vertices and their costs in the path from v to w.
        # Build the list by traversing backwards from the entry for w, appending each vertex, until you reach v.
        # Then reverse the list.

        connections = []
        print('W is -->' + str(w) + '\n')  # find our target destination
        result = self.dijkstra(v)
        # print(result)
        tester = result.get(w)
        connections.append((w, tester))
        while w is not v:
            new = result.get(w)
            pred = new[1]
            ans = (pred, result.get(pred))
            connections.append(ans)
            w = pred


        connections.reverse()
        return connections

    def printvlist(self, path):  # path is a list of shortest path including cost and predecessors

        print('type\tlatitude\tlongitude\telement\tcost')
        for line in path:
            # print(line[0],line[1][0], line[1][1], '-----LINE')
            vertex = line[0]
            vertexEle = self._vertexElement.get(vertex)
            coord = self._vertexCoordinates.get(vertexEle)
            # print(coord)
            cost = line[1][0]
            print('w \t' + str(coord[1]) + '\t' + str(coord[2]) + '\t' + str(vertex._element)
                  + '\t' + str(cost))

    def get_vertex_by_label(self, element):
        """ Return the first vertex that matches element. """
        return self._elementVertex.get(element)  # if doesn't exist, default return none

    def __str__(self):
        if len(self._structure) > 100:
            print('TOO LONG TO PRINT!')
        else:
            # to finish off
            hstr = ('|V| = ' + str(self.num_vertices())
                    + '; |E| = ' + str(self.num_edges()))
            vstr = '\nVertices: '
            for v in self._structure:
                vstr += str(v) + '-'
            edges = self.edges()
            estr = '\nEdges: '
            for e in edges:
                estr += str(e) + ' '
            return hstr + vstr + estr

    def graphreader(self, filename):
        """ Read and return the route map in filename. """
        # graph = Graph()
        file = open(filename, 'r')
        entry = file.readline()  # either 'Node' or 'Edge'
        num = 0
        while entry == 'Node\n':
            num += 1
            nodeid = int(file.readline().split()[1])
            gps = file.readline().split()
            latitude = float(gps[1])
            longitude = float(gps[2])

            vertex = self.add_vertex(nodeid, gps)
            entry = file.readline()  # either 'Node' or 'Edge'
        print('Read', num, 'vertices and added into the graph')
        num = 0
        while entry == 'Edge\n':
            num += 1
            source = int(file.readline().split()[1])
            sv = self.get_vertex_by_label(source)
            target = int(file.readline().split()[1])
            tv = self.get_vertex_by_label(target)
            length = float(file.readline().split()[1])
            time = float(file.readline().split()[1])

            edge = self.add_edge(sv, tv, time)
            file.readline()  # read the one-way data
            entry = file.readline()  # either 'Node' or 'Edge'
        print('Read', num, 'edges and added into the graph')
