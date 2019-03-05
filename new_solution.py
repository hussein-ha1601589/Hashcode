import numpy as np
import codecs
with codecs.open('data/c_memorable_moments.txt', encoding='utf-8-sig') as f:
    set = np.array([[x for x in line.split()] for line in f])

n = int(set[0][0])
set = np.delete(set,0)
orient = np.array([])
tag_size = np.array([])
tags = []
for col in set:
    orient = np.append(orient,col[0])
    tag_size = np.append(tag_size,col[1])
    tags.append(col[2:len(col)])

tags = np.array(tags)
set = np.stack((orient,tag_size,tags))
set = set.transpose()
set[:,1] = set[:,1].astype(np.int)
set = set[set[:,1].argsort()]
