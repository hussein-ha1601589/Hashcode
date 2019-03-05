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


print(graph.get(y))
for i in data :
    max = [0,None,None]
    for inf in data:
        ret = graph.get(i)[inf]['cost']
        if ret > max[0]:
            max[0] = ret
            max[1] = inf.id
            max[2] = i.id
    graph.pop(i)
    np.delete(data,i.id)
    print(max)


