import sys
import random
import numpy as np
import time

#some of the code is from open source project and tutorial
#The referenced code should be less than 10 lines
MAX = sys.maxsize

@profile
def Dijkstra_2D(W,src):
    nodes=[]
    for i in range(len(W)):
      nodes.append(i)
    visited = []
    visited.append(src)
    results = {src:0}
    for i in nodes:
        # print(W[src][i])
        results[i] = W[src][i]
    #recording
    path={src:{src:[]}}  
    new_node=pre=src
    while nodes: # iterate all nodes
        temp = new_node
        initial_distance=MAX # regarding all link weight are infinite
        for v in visited:
            for d in nodes:
                if W[src][v] != MAX and W[v][d] != MAX:
                  #compare the new nodes
                    new_distance = W[src][v]+W[v][d]
                    if new_distance <= initial_distance:
                        initial_distance=new_distance
                        W[src][d]=new_distance  
                        new_node=d
                        pre=v
        if new_node!=src and temp==new_node:
            break
        results[new_node]=initial_distance  
        path[src][new_node]=[i for i in path[src][pre]]
        path[src][new_node].append(new_node)

        visited.append(new_node)
        nodes.remove(new_node)
    return results,path



@profile
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
# print(Dijkstra_2D(W, 0))

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
# print(Dijkstra_2D(W, 0))




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

print("Dijkstra_2D Algorithm veriy case 1")
print("path between V1~V8 is 0~7 in my design")
results,path = Dijkstra_2D(W1, 0)
result={}
print("shortest distance from V0 to V7 is:")
result["0"]=results
print(result)
print("shortest path from V0 to V7 is:")
print(path[0][7])

print("path between V7~V8 is 6~7 in my design")
results,path = Dijkstra_2D(W1, 6)
result={}
print("shortest distance from V6 to V7 is:")
result["6"]=results
print(result)
print("shortest path from V6 to V7 is:")
print(path[6][7], "\n")

print("Dijkstra_2D Algorithm veriy case 2")
print("path between V2~V8 is 1~7 in my design")
results,path = Dijkstra_2D(W2, 1)
result={}
print("shortest distance from V1 to V7 is:")
result["1"]=results
print(result)
print("shortest path from V1 to V7 is:")
print(path[1][7])

print("path between V12~V10 is 11~9 in my design")
results,path = Dijkstra_2D(W2, 11)
result={}
print("shortest distance from V11 to V9 is:")
result["11"]=results
print(result)
print("shortest path from V11 to V9 is:")
print(path[11][9])



print("---------------Dijkstra Algorithm complete graph----------------")
W_total=[20,40,60,80,100,120,140,160,180,200]

for j in range(10):
    print("Start calculating  ", W_total[j] )
    start = time.time()
    W=rng_2_arry_complete(W_total[j])
    for i in range(len(W)):
        # print(i)
    # print("this is node", i)
    # print(Dijkstra_2D(W, i))
        Dijkstra_2D(W, i)
    end = time.time()
    print("This is the time to get  ", W_total[j], "  calculated" )
    print(str(end-start))

print("---------------Dijkstra Algorithm sparse graph----------------")
W_total=[20,40,60,80,100,120,140,160,180,200]

for j in range(10):
    print("Start calculating  ", W_total[j] )
    start = time.time()
    W=rng_2_arry_sparse(W_total[j])
    for i in range(len(W)):
    # print("this is node", i)
    # print(Dijkstra_2D(W, i))
        Dijkstra_2D(W, i)
    end = time.time()
    print("This is the time to get  ", W_total[j], "  calculated" )
    print(str(end-start))


# print("---------------Dijkstra Algorithm complete graph memory analysis----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for j in range(10):
#     if j==4:
#         print("Start calculating  ", W_total[j])
#         W=rng_2_arry_sparse(W_total[j])
#         Dijkstra_2D(W, 0)
#         end = time.time()
#         print(  W_total[j], "nodes  calculated" )


