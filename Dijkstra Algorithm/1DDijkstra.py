import sys
import random
import numpy as np
import time
import copy

#some of the code is from open source project and tutorial
#The referenced code should be less than 10 lines

##N is the total row/col number minus 1 !!!!!


def RNG(n):
    return random.randint(1,n)
@profile  
def rng_2_arry_complete(N):  # complete graph, we just need to generate weight for each link
    temp1=0                  #the input N here, will lead to N+1 node
    W=[]
    for i in range (N+1):  ##generating N+1 nodes' links, lower half
        temp1=temp1+i
    for i in range(temp1):
        W.append(RNG(N))
    return W
# print(rng_2_arry_complete(5))

# W=rng_2_arry_complete(100)
# print(Dijkstra_1D(W, 0))

@profile  
def rng_2_arry_sparse(n):  ##generating N+1 nodes' links, lower half
    W=[]
    MAX=sys.maxsize
    x=np.zeros((n+1,n+1))   
    node_list=[]
    temp1=RNG(n+1)
    node_list.append(temp1)
    while (len(node_list) <n+1):
        next_node=RNG(n+1)
        if next_node not in node_list:
            node_list.append(next_node)
    for i in range (n+1):
        if i<n+1-1:
            temp1=node_list[i]
            temp2=node_list[i+1]
            xx=RNG(n+1) # to compensate the array is 0~99 RNG is 1~100
            x[temp1-1,temp2-1]=xx
            x[temp2-1,temp1-1]=xx
    for i in range (n+1): ## set the un-connected nodes distance to be 0
        for j in range (n+1):
            if j>i and x[i,j]==0:
                x[i,j]=MAX
    for i in range (n+1):
        for j in range (n+1):
            if j<i and x[i,j]==0:
                x[i,j]=MAX
    x_list=x.tolist()
##convert it to a one-dimension array
    for i in range(n+1):
        for j in range(len(x_list[i])):
            if i!=0 and j<i:
                W.append(x_list[i][j])
    return W

# print(rng_2_arry_sparse(5))
@profile 
def parse_array(WW,n,N): # the real row is N+1, minor mismatch, fixed and compensated in main algorithm function and RNG
    W=[]
    if n !=0:
        temp1=0
        for i in range (n):
            temp1=temp1+i
        temp2=temp1+n-1
        W=WW[temp1:temp2+1] #get the each row of the lower matrix
        W.append(0) #add 0 to diagonal line
        idx=0
        for i in range (0,N-n):
            temp1=len(W)+i-idx
            temp2=0
            temp3=0
            for j in range(temp1):
                temp2=temp2+j
            temp3=temp2+n
            a=WW[temp3]
            W.append(a)
            temp1=0
            temp2=0
            temp3=0
            idx=idx+1
    if n == N:
        temp1=0
        for i in range (n):
            temp1=temp1+i
        temp2=temp1+n-1
        W=WW[temp1:temp2+1] 
        W.append(0) 
    if n == 0:
        W.append(0)
        for i in range (N):
            temp1=0
            for j in range (i):
                temp1=temp1+j+1
            # print(temp1)
            W.append(WW[temp1]) 
    # print (W)          
    return W

# print(parse_array(WW,n,N))

#the input is a one dimension array!
@profile  
def Dijkstra_1D(W,src,N):
    nodes=[]
    for i in range(N+1):
        nodes.append(i)
    visited = []
    visited.append(src)
    results = {src:0}
    W_src=parse_array(W,src,N)
    for i in nodes:
        results[i] = W_src[i]
    #recording
    path={src:{src:[]}}  
    new_node=pre=src
    
    while nodes: # iterate all nodes
        temp = new_node
        initial_distance=MAX # regarding all link weight are infinite
        for v in visited:
            W_v=parse_array(W,v,N)
            for d in nodes:
                if W_src[v] != MAX and W_v[d] != MAX:
                  #compare the new nodes
                    new_distance = W_src[v]+W_v[d]
                    if new_distance <= initial_distance:
                        initial_distance=new_distance
                        W_src[d]=new_distance  
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


# N=7
# n=0
MAX = sys.maxsize
##the one-dimension array only store the lower half matrix, the diagonal is not included
case1=[MAX,MAX,MAX,29,MAX,12,MAX,MAX,MAX,5,MAX,11,5,MAX,MAX,MAX,11,5,13,7,MAX,MAX,MAX,MAX,MAX,11,17,MAX]
case2=[11,
    14,12,
    MAX,MAX,18,
    8,6,13,MAX,
    MAX,MAX,13,MAX,MAX,
    29,MAX,MAX,27,MAX,MAX,
    28,MAX,MAX,17,MAX,15,MAX,
    MAX,MAX,25,9,MAX,5,MAX,5,
    MAX,MAX,MAX,25,MAX,MAX,MAX,9,MAX,
    14,MAX,MAX,MAX,MAX,MAX,MAX,MAX,25,MAX,
    MAX,MAX,16,MAX,22,MAX,MAX,MAX,MAX,MAX,MAX]

# cases=[case1,case2]
# print("in case 1, path between V1~V8 is 0~7 in my design")
# print("in case 1, path between V7~V8 is 6~7 in my design")
# print("in case 2, path between V2~V8 is 1~7 in my design")
# print("in case 2, path between V12~V10 is 11~9 in my design")
# for i in range(2):
#     case=cases[i]
#     if i==0:
#         print("This is test case1.txt")
#         results,path=Dijkstra_1D(case, 0, 7)
#         temp={}
#         temp[str(0)]=results
#         print("shortest distance from V0 to V7 is:")
#         print(temp)
#         print("shortest path from V0 to V7 is:")
#         print(path[0][7])

#         results,path=Dijkstra_1D(case, 6, 7)
#         temp={}
#         temp[str(6)]=results
#         print("shortest distance from V6 to V7 is:")
#         print(temp)
#         print("shortest path from V6 to V7 is:")
#         print(path[6][7], "\n")
#     if i==1:
#         print("This is test case2.txt")
#         results,path=Dijkstra_1D(case, 1, 11)
#         temp={}
#         temp[str(1)]=results
#         print("shortest distance from V1 to V7 is:")
#         print(temp)
#         print("shortest path from V1 to V7 is:")
#         print(path[1][7])
#         results,path=Dijkstra_1D(case, 11, 11)
#         temp={}
#         temp[str(11)]=results
#         print("shortest distance from V11 to V9 is:")
#         print(temp)
#         print("shortest path from V11 to V9 is:")
#         print(path[11][9])
        

# print("---------------Dijkstra Algorithm complete graph----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for j in range(7):
#     print("Start calculating  ", W_total[j] )
#     start = time.time()
#     W=rng_2_arry_complete(W_total[j]-1)
#     for i in range((W_total[j])):
#         Dijkstra_1D(W, i, W_total[j]-1)
#     end = time.time()
#     print("This is the time to get  ", W_total[j], "  calculated" )
#     print(str(end-start))

# print("---------------Dijkstra Algorithm sparse graph----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for j in range(7):
#     print("Start calculating  ", W_total[j] )
#     start = time.time()
#     W=rng_2_arry_sparse(W_total[j]-1)
#     for i in range((W_total[j])):
#         Dijkstra_1D(W, i, W_total[j]-1)
#     end = time.time()
#     print("This is the time to get  ", W_total[j], "  calculated" )
#     print(str(end-start))


print("---------------Dijkstra Algorithm sparse graph----------------")
W_total=[20,40,60,80,100,120,140,160,180,200]

for j in range(7):
    if j==4:
        print("Start calculating  ", W_total[j] )
        start = time.time()
        W=rng_2_arry_sparse(W_total[j]-1)
        for i in range((W_total[j])):
            Dijkstra_1D(W, 0, W_total[j]-1)
        end = time.time()
        print("This is the time to get  ", W_total[j], "  calculated" )
        print(str(end-start))

