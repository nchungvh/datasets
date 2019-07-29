import numpy as np
import pdb
import pickle
with open('all_movie.csv', "r") as lst:
#with open('filmtv_movies - ENG.csv', "r") as lst:
    file = lst.readlines()
cast = []
for i in range(len(file)-1):
    cast.append(np.array(file[i+1].split(','))[:6])
cast = np.asarray(cast)
print(cast[1][5])
edges = []
for i in range(len(cast)-1):
    print(i)
    for j in range(i+1,len(cast)):
        for m in range(6):
            for n in range(6):
                if((cast[i][m]==cast[j][n])&(str(cast[i][m])!='Cast Not Available')):
                    edges.append(np.array([i+2,j+2]))
edges = np.asarray(edges)
output = open('edges_all_movie.pkl', 'wb')
pickle.dump(edges, output)
output.close()