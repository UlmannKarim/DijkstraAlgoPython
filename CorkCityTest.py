# KARIM ABDUL ULMANN 119329701

from RouteMap import *

# simpleRoute = RouteMap('simpleroute.txt')

# simpleGraph = graphreader('simplegraph1.txt')
# simpleGraph.dijkstra(simpleGraph.get_vertex_by_label(1))
#
# simpleGraph2 = graphreader('simplegraph2.txt')
# simpleGraph2.dijkstra(simpleGraph2.get_vertex_by_label(14))


routemap = RouteMap('corkCityData.txt')

ids = {}

ids['wgb'] = 1669466540

ids['turnerscross'] = 348809726

ids['neptune'] = 1147697924

ids['cuh'] = 860206013

ids['oldoak'] = 358357

ids['gaol'] = 3777201945

ids['mahonpoint'] = 330068634

sourcestr = 'wgb'

deststr = 'neptune'

source = routemap.get_vertex_by_label(ids[sourcestr])

dest = routemap.get_vertex_by_label(ids[deststr])

tree = routemap.sp(source, dest)

routemap.printvlist(tree)

# ---------------logs------------------------------


# Western Gateway to Neptune Stadium
# 195.49595012020677

# The Old Oak to Cork University Hospital
# 265.9720774815984

# Cork City Gaol to Mahon Point
# 968.400395864096

# ---------------------------------------------------------

# final cost from wgb to neptune is 327.1926431486171
# improved cost from wgb to neptune is 195.49595012020677


# final cost from wgb to CUH is 130.33195885418456
# improved cost from wgb to CUH is 130.33195885418456


# final cost from wgb to MP is 1042.1959312896654
# improved cost from wgb to MP is 895.8406177155017


# final cost from wgb to oldoak is 196.6362254679223
# improved cost from wgb to oldoak is 177.00499487834833


# final cost from wgb to gaol is 100.3057736841561
# improved cost from wgb to gaol is 100.3057736841561


# final cost from wgb to tCross is 248.93772501090962
# improved cost from wgb to tCross is 236.40183495063545
