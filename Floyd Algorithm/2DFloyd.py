import sys
import random
import numpy as np
import time
import copy


#some of the code is from open source project and tutorial
#The referenced code should be less than 10 lines
MAX = sys.maxsize

def RNG(n):
    return random.randint(1,n)
@profile
def rng_2_arry_complete(n):  #initial as all zero
    x=np.zeros((n,n))
    for i in range (n):      # set random number except diagonal
        for j in range(n):
            if j>i:
                xx=RNG(n)
                x[i,j]=xx
                x[j,i]=xx
    x_list=x.tolist()
    return x_list

# W=rng_2_arry_complete(100)
# print(Dijkstra_1(W, 0))
@profile
def rng_2_arry_sparse(n):
    MAX=sys.maxsize
    x=np.zeros((n,n))   
    # generate a graph with n-1 nodes
    node_list=[]
    temp1=RNG(n)
    node_list.append(temp1)
    while (len(node_list) <n):
        next_node=RNG(n)
        if next_node not in node_list:
            node_list.append(next_node)
    for i in range (n):
        if i<n-1:
            temp1=node_list[i]
            temp2=node_list[i+1]
            xx=RNG(n) # to compensate the array is 0~99 RNG is 1~100
            x[temp1-1,temp2-1]=xx
            x[temp2-1,temp1-1]=xx
    for i in range (n): ## set the un-connected nodes distance to be MAX
        for j in range (n):
            if j>i and x[i,j]==0:
                x[i,j]=MAX
    for i in range (n):
        for j in range (n):
            if j<i and x[i,j]==0:
                x[i,j]=MAX
    x_list=x.tolist()
    return (x_list)

# W=rng_2_arry_sparse(10)
# print(Dijkstra_1(W, 0))
@profile
def Floyd_2D(W):    
    results=copy.deepcopy(W)
    n=len(W)    
    path = [([0] * n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if results[i][j]:
                path[i][j] = str(i + 1) + " " + str(j + 1)
                path[i][j] = str(i) + " " + str(j)   
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if results[i][j] > results[i][k] + results[k][j]:
                    results[i][j] = results[i][k] + results[k][j]
                    path[i][j] = path[i][k] + " " + path[k][j][2:]
    return results, path

W1 = [[0,MAX,MAX,29,MAX,MAX,MAX,MAX],
 [MAX,0,MAX,MAX,MAX,11,11,MAX],
 [MAX,MAX,0,12,MAX,5,5,MAX],
 [29,MAX,12,0,5,MAX,13,MAX],
 [MAX,MAX,MAX,5,0,MAX,7,11],
 [MAX,11,5,MAX,MAX,0,MAX,17],
 [MAX,11,5,13,7,MAX,0,MAX],
 [MAX,MAX,MAX,MAX,11,7,MAX,0]]


W2 = [[0,11,14,MAX,8,MAX,29,28,MAX,MAX,14,MAX],
[11,0,12,MAX,6,MAX,MAX,MAX,MAX,MAX,MAX,MAX],
[14,12,0,18,13,13,MAX,MAX,25,MAX,MAX,16],
[MAX,MAX,18,0,MAX,MAX,27,17,9,25,MAX,MAX],
[8,6,13,MAX,0,MAX,MAX,MAX,MAX,MAX,MAX,22],
[MAX,MAX,13,MAX,MAX,0,MAX,15,5,MAX,MAX,MAX],
[29,MAX,MAX,27,MAX,MAX,0,MAX,MAX,MAX,MAX,MAX],
[28,MAX,MAX,17,MAX,15,MAX,0,5,9,MAX,MAX],
[MAX,MAX,25,9,MAX,5,MAX,5,0,MAX,25,MAX],
[MAX,MAX,MAX,25,MAX,MAX,MAX,9,MAX,0,MAX,MAX],
[14,MAX,MAX,MAX,MAX,MAX,MAX,MAX,25,MAX,0,MAX],
[MAX,MAX,16,MAX,22,MAX,MAX,MAX,MAX,MAX,MAX,0]]


print("Floyd_2D Algorithm veriy case 1")
print("path between V1~V8 is 0~7 in my design")
results,path = Floyd_2D(W1)
# print("This is the overall results", results)  #un comment this line to check my complete results
result=results[0]
result_show={}
result_show_={}
for i in range(len(results)):
  result_show_[str(i)]=str(result[i])
result_show[str(0)]=result_show_
print("shortest distance from V0 to V7 is:")
print(result_show)
print("shortest path from V0 to V7 is:")
print(path[0][7])


print("path between V7~V8 is 6~7 in my design")
result=results[6]
result_show={}
result_show_={}
for i in range(len(results)):
  result_show_[str(i)]=str(result[i])
result_show[str(6)]=result_show_
print("shortest distance from V6 to V7 is:")
print(result_show)
print("shortest path from V6 to V7 is:")
print(path[6][7])



print("Floyd_2D Algorithm veriy case 2")
print("path between V2~V8 is 1~7 in my design")
results,path = Floyd_2D(W2)
# print("This is the overall results", results)  #un comment this line to check my complete results
result=results[1]
result_show={}
result_show_={}
for i in range(len(results)):
  result_show_[str(i)]=str(result[i])
result_show[str(1)]=result_show_
print("shortest distance from V1 to V7 is:")
print(result_show)
print("shortest path from V1 to V7 is:")
print(path[1][7])


print("path between V12~V10 is 11~9 in my design")
result=results[11]
result_show={}
result_show_={}
for i in range(len(results)):
  result_show_[str(i)]=str(result[i])
result_show[str(11)]=result_show_
print("shortest distance from V11 to V9 is:")
print(result_show)
print("shortest path from V11 to V9 is:")
print(path[11][9])


print("---------------Floyd_2D Algorithm complete graph----------------")
W_total=[20,40,60,80,100,120,140,160,180,200]

for j in range(10):
    # print(j)
    print("Start calculating  ", W_total[j] )
    start = time.time()
    W=rng_2_arry_complete(W_total[j])
    Floyd_2D(W)
    end = time.time()
    print("This is the time to get  ", W_total[j], "  calculated" )
    print(str(end-start))

print("---------------Floyd_2D Algorithm sparse graph----------------")
W_total=[20,40,60,80,100,120,140,160,180,200]

for j in range(10):
    # print(j)
    print("Start calculating  ", W_total[j] )
    start = time.time()
    W=rng_2_arry_sparse(W_total[j])
    Floyd_2D(W)
    end = time.time()
    print("This is the time to get  ", W_total[j], "  calculated" )
    print(str(end-start))


# print("---------------Floyd_2D Algorithm complete graph memory analysis----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for j in range(10):
#     if j==4:
#         print("Start calculating  ", W_total[j] )
#         start = time.time()
#         W=rng_2_arry_sparse(W_total[j])
#         Floyd_2D(W)
#         end = time.time()
#         print("This is the time to get  ", W_total[j], "  calculated" )
#         print(str(end-start))




