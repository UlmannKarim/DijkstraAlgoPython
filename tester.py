from graphsAssignment import *

if __name__ == '__main__':
    pass
    # testing module for all

    # ------------------------------------tester--------------------------

    # elem0 = Element(13, 'ant', 0)
    # elem1 = Element(14, 'bed', 1)
    # elem2 = Element(24, 'cat', 2)
    # elem3 = Element(22, 'dog', 3)
    # elem4 = Element(27, 'egg', 4)
    # elem5 = Element(25, 'fox', 5)
    #
    # print(elem5)

    # my_heap = APQ()
    # bed = my_heap.add(14, 'bed')
    # dog = my_heap.add(22, 'dog')
    # cat = my_heap.add(24, 'cat')
    # ant = my_heap.add(35, 'ant')
    # egg = my_heap.add(27, 'egg')
    # fox = my_heap.add(18, 'fox')
    # # my_heap.add(1, 'Karim')
    #
    # print(my_heap)
    #
    # # print('\n get parent')
    # # print(my_heap.getParent(dog))
    # #
    # # print('\n removing min')
    # # print(my_heap.remove_min())
    # print()
    #
    # # print(my_heap.get_key(fox), 'key')
    # # print(my_heap.getParent(fox), 'parent')
    #
    # # my_heap.update_key(egg, 12)
    # # print(my_heap)
    # #
    #
    # print('updating ant key to 13')
    # my_heap.update_key(ant, 13)
    # print(my_heap, '\n')
    #
    # print('updating fox key to 25')
    # my_heap.update_key(fox, 25)
    # print(my_heap, '\n')
    #
    # print('get parent of ant')
    # print(my_heap.getParent(ant))
    # print('\n')
    #
    # print('update eggs key to 12')
    # my_heap.update_key(egg, 12)
    # print(my_heap, '\n')
    #
    # print('remove egg')
    # my_heap.remove(bed)
    # print(my_heap, '\n')

    # my_heap.remove(bed)
    # print(my_heap)
    #
    # my_heap.remove(ant)
    # print(my_heap)
    #
    # my_heap.update_key(egg, 1)
    # print(my_heap)

    # ------------------------------tester---------------------------


# Test methods

# def test_graph():
#     """ Test on a simple 3-vertex, 2-edge graph. """
#     print('----------- Test on simple graph ----------')
#     graph = Graph()
#     a = graph.add_vertex('a')
#     b = graph.add_vertex('b')
#     c = graph.add_vertex('c')
#     d = graph.add_vertex_if_new('b')  # should not create a vertex
#     eab = graph.add_edge(a, b, 2)
#     ebc = graph.add_edge(b, c, 9)
#
#     vnone = Vertex('dummy')
#     evnone = graph.add_edge(vnone, c, 0)  # should not create an edge
#     if evnone is not None:
#         print('ERROR: attempted edges  should have been none')
#
#     edges = graph.get_edges(vnone)  # should be None: vnone not in graph
#     if edges != None:
#         print('ERROR: returned edges for non-existent vertex.')
#
#     print('number of vertices:', graph.num_vertices())
#     print('number of edges:', graph.num_edges())
#
#     print('Vertex list should be a,b,c in any order :')
#     vertices = graph.vertices()
#     for key in vertices:
#         print(key.element())
#
#     print('Edge list should be (a,b,2),(b,c,9) in any order :')
#     edges = graph.edges()
#     for edge in edges:
#         print(edge)
#
#     print('Graph display should repeat the above:')
#     print(graph)
#     print()
#
#     print(graph.dijkstra(a))
#
#     print()
#     print('----------- End of test ----------')
#
#
# test_graph()


# def graphreader(filename):
#     """ Read and return the route map in filename. """
#     graph = Graph()
#     file = open(filename, 'r')
#     entry = file.readline()  # either 'Node' or 'Edge'
#     num = 0
#     while entry == 'Node\n':
#         num += 1
#         nodeid = int(file.readline().split()[1])
#         vertex = graph.add_vertex(nodeid)
#         entry = file.readline()  # either 'Node' or 'Edge'
#     print('Read', num, 'vertices and added into the graph')
#     num = 0
#     while entry == 'Edge\n':
#         num += 1
#         source = int(file.readline().split()[1])
#         sv = graph.get_vertex_by_label(source)
#         target = int(file.readline().split()[1])
#         tv = graph.get_vertex_by_label(target)
#         length = float(file.readline().split()[1])
#         edge = graph.add_edge(sv, tv, length)
#         file.readline()  # read the one-way data
#         entry = file.readline()  # either 'Node' or 'Edge'
#     print('Read', num, 'edges and added into the graph')
#     print(graph)
#     return graph


print('\n')

print('----------- TEST ON SIMPLE GRAPH 1 ------------')

SIMPLE_GRAPH1 = graphreader('simplegraph1.txt')

print('\n', SIMPLE_GRAPH1)

print(SIMPLE_GRAPH1.get_vertex_by_label(1))

print(SIMPLE_GRAPH1.dijkstra(SIMPLE_GRAPH1.get_vertex_by_label(1)))

print('\n ---------------- DONE -------------------------')

print('\n')

print('----------- TEST ON SIMPLE GRAPH 2 ------------')

SIMPLE_GRAPH2 = graphreader('simplegraph2.txt')

print('\n', SIMPLE_GRAPH2)

print(SIMPLE_GRAPH2.get_vertex_by_label(14))

print(SIMPLE_GRAPH2.dijkstra(SIMPLE_GRAPH2.get_vertex_by_label(14)))

print('\n ---------------- DONE -------------------------')

#
# def test_graph2():
#     """ Test Graph with the standard 6-vertex graph from lectures. """
#
#     print('----------- Test on 6-vertex graph from lectures ----------')
#
#     graph = Graph()
#     a = graph.add_vertex('a')
#     b = graph.add_vertex('b')
#     c = graph.add_vertex('c')
#     d = graph.add_vertex('d')
#     e = graph.add_vertex('e')
#     f = graph.add_vertex('f')
#     graph.add_edge(a, b, 1)
#     graph.add_edge(a, c, 1)
#     graph.add_edge(b, c, 1)
#     graph.add_edge(b, d, 1)
#     graph.add_edge(b, e, 1)
#     graph.add_edge(c, f, 1)
#     graph.add_edge(e, f, 1)
#
#     # print('--look under here-----')
#     # print()
#     #
#     # print(graph._breadthFirstSearch(a,))
#     #
#     # print()
#     # print('--- look above ----')
#
#     hdv = graph.highestdegreevertex()
#     print(hdv.element(),
#           'has the highest degree =',
#           graph.degree(hdv))
#     print(graph)
#
#     print()
#     print('----------- End of test ----------')
#
#
#
# #
# #
# def test_graph3():
#     """ Test on the larger graph from lectures. """
#
#     print('----------- Test on 13-vertex graph from lectures ----------')
#
#     graph = Graph()
#     a = graph.add_vertex('a')
#     b = graph.add_vertex('b')
#     c = graph.add_vertex('c')
#     d = graph.add_vertex('d')
#     e = graph.add_vertex('e')
#     f = graph.add_vertex('f')
#     g = graph.add_vertex('g')
#     h = graph.add_vertex('h')
#     i = graph.add_vertex('i')
#     j = graph.add_vertex('j')
#     k = graph.add_vertex('k')
#     l = graph.add_vertex('l')
#     m = graph.add_vertex('m')
#     graph.add_edge(a, b, 1)
#     graph.add_edge(a, e, 1)
#     graph.add_edge(a, h, 1)
#     graph.add_edge(b, c, 1)
#     graph.add_edge(b, e, 1)
#     graph.add_edge(c, d, 1)
#     graph.add_edge(c, g, 1)
#     graph.add_edge(d, f, 1)
#     graph.add_edge(e, f, 1)
#     graph.add_edge(e, k, 1)
#     graph.add_edge(f, i, 1)
#     graph.add_edge(g, j, 1)
#     graph.add_edge(h, m, 1)
#     graph.add_edge(i, j, 1)
#     graph.add_edge(i, k, 1)
#     graph.add_edge(j, l, 1)
#     graph.add_edge(k, l, 1)
#     graph.add_edge(k, m, 1)
#
#     hdv = graph.highestdegreevertex()
#     print(hdv.element(),
#           'has the highest degree =',
#           graph.degree(hdv))
#     print(graph)
#
#     print('----------- End of test ----------')
