import numpy as np
import pdb
import pickle
import csv
with open('all_movie.csv', "r") as lst:
#with open('filmtv_movies - ENG.csv', "r") as lst:
    file = lst.readlines()
print(len(file), type(file))
i = 0
while(i<len(file)-10):
    print(i)
    for j in range(i+1,len(file)-9):
        if(file[i].split(',')[:10]==file[j].split(',')[:10]):
            del file[j]
    i+=1
print(len(file))
with open('all_movie_modify.csv', 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerows([c.strip() for c in r.split(',')] for r in file)
