import numpy as np
import pdb
with open('tmdb-movies.csv', "r") as lst:
#with open('filmtv_movies - ENG.csv', "r") as lst:
    file = lst.readlines()
print(len(file))
cast = []
for i in range(len(file)-1):
    cast.append(np.array(file[i+1].split(','))[6].split('|'))
print(cast[46][1]==cast[44][3])
edges = []
for i in range(len(cast)-1):
    print(i)
    for j in range(i+1,len(cast)):
        for m in range(len(cast[i])):
            for n in range(len(cast[j])):
                if((cast[i][m]==cast[j][n])):
                    edges.append(np.array([i+2,j+2]))
edges = np.asarray(edges)
print(edges)
np.save('edgesTMDB.npy',edges)


