import numpy as np
import pdb
import pickle
with open('all_movie_modify.csv', "r") as lst:
#with open('filmtv_movies - ENG.csv', "r") as lst:
    file = lst.readlines()
cast = []
for i in range(len(file)-1):
    dem =0
    for k in range(6):
        dem =k
        if((file[i+1].split(','))[k] == 'Cast Not Available'):
            break
    cast.append(np.array(file[i+1].split(','))[:dem])
cast = np.asarray(cast)
edges = []
for i in range(len(cast)-1):
    print(i)
    for j in range(i+1,len(cast)):
        for m in range(len(cast[i])):
            for n in range(len(cast[j])):
                if(cast[i][m]==cast[j][n]):
                    edges.append(np.array([i+2,j+2]))
edges = np.asarray(edges)
output = open('edges_all_movie_modify.pkl', 'wb')
pickle.dump(edges, output)
output.close()