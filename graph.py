import numpy as np
from dijkstar import Graph, find_path
from algorithm import  single_source_shortest_paths
from interest import interest
from  adapter import Adapter
graph = Graph()

x = Adapter(np.array(['t1','t2','t3','t4','t5','t6']),0)
y= Adapter(np.array(['t4','t5','t6','t7','t8','t9','t10']),1)
z= Adapter(np.array(['t4','t5','t6','t7','t8','t9','t10']),2)
data = np.array([x,y,z])
for f in data :
    for inf in data :
        graph.add_edge(f,inf,{'cost':interest(f,inf,0,0)})

# print(str(graph))
# print(find_path(graph,y,z,cost_func= interest))
print(single_source_shortest_paths(graph,y,cost_func= interest))


#

# graph = Graph()
# graph.add_edge(1, 2, {'cost': 1})
# graph.add_edge(2, 3, {'cost': 2})
# cost_func = lambda u, v, e, prev_e: e['cost']
# print(find_path(graph, 1, 2, cost_func=cost_func))
