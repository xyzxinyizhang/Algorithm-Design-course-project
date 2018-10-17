from collections import defaultdict, deque
import sys
import random
import time

#some of the code is from open source project and tutorial
#The referenced code should be less than 10 lines

MAX=sys.maxsize
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.graph_dict = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

@profile
def Floyd(graph):
    dist = {}
    pred = {}
    for node in graph:
        dist[node] = {}
        pred[node] = {}
        for dst in graph:
            dist[node][dst] = MAX
            pred[node][dst] = 0
        dist[node][node] = 0
        for node_ in graph[node]:
            dist[node][node_] = graph[node][node_]
            pred[node][node_] = node
    for node_next in graph:
        for node in graph:
            for dst in graph:
                newdist = dist[node][node_next] + dist[node_next][dst]
                if newdist < dist[node][dst]:
                    dist[node][dst] = newdist
                    pred[node][dst] = pred[node_next][dst] 
 
    return dist,pred
 
#######################################################################################case_verify############################################
graph=Graph()
def read_case(case):
    case_matrix=[]
    file = open(case)
    while 1:
        line = file.readline()
        if not line:
            break
        line=line.split()   
        for i in range (len(line)):
            if line[i]== "99999":
                line[i]=MAX
        for i in range (len(line)):
            if line[i] != MAX:
                line[i]=int(line[i])
        case_matrix.append(line)
    for i in range (len(case_matrix)):
        temp1=case_matrix[i]
        for j in range(len(temp1)):
            if i==j:
                temp1[j]=0
    # print (case_matrix)
    return case_matrix
def make_case_lined_list_verify(case):
    graph = Graph()
    case_input=read_case(case)

    for i in range (len(case_input)):
        graph.add_node(i)

    for i in range (len(case_input)):
        temp1=case_input[i]
        for j in range (len(temp1)):
            if j>i:
                graph.add_edge(i, j, temp1[j])
            if j==i:
                graph.add_edge(i,j,0)
    return graph



#######################################################################################end case_verify############################################


#######################################################################################sparse and complete############################################
@profile
def RNG(n):
    return random.randint(1,n)
@profile
def make_case_lined_list_complte(n):
    graph = Graph()
    node_list=[]
    for i in range(n):
        node_list.append(i)
    for i in range (n):
        graph.add_node(i)
    for i in range (n):
        for j in range (n):
            if j>i:
                graph.add_edge(i, j, RNG(n))
            if j==i:
                graph.add_edge(i,j,0)
    return graph,node_list

# graph=make_case_lined_list_complte(5)
# print(graph.edges)
@profile
def make_case_lined_list_sparse(n):
    MAX=sys.maxsize
    graph = Graph() 
    node_list=[]
    temp1=RNG(n)
    node_list.append(temp1)

    # determinme the n-1 links first
    while (len(node_list) <n):
        next_node=RNG(n)
        if next_node not in node_list:
            node_list.append(next_node)
    for i in range(n):
        node_list[i]=node_list[i]-1
# add the determined node (all nodes) to the node graph
    for i in range (n):
        graph.add_node(node_list[i])
#initial the entire linked list to be max distance
    for i in range (n):
        for j in range (n):
            if j>i:
                graph.add_edge(i, j, MAX)
#change the determened links value to RNG number
    for i in range(n):
        graph.add_edge(node_list[i], node_list[i],0) 
        if i<n-1:
            xx=RNG(n)
            graph.add_edge(node_list[i], node_list[i+1], RNG(n))
    return graph, node_list


#######################################################################################sparse and complete end############################################

# graph,node = make_case_lined_list_complte(5)
# @profile
def get_linked_list(graph, node):
    graph_dict={}
    # for i in range(len(graph.edges)):
    for i in range(len(node)):   
        node_temp=node[i] # get a node in graph
        node_linked_temp=graph.edges[node[i]]  # get its ;inked nodes
        # print("new node")
        node_dict={}
        for j in range(len(node_linked_temp)):
            pair=()
            pair=node_temp, node_linked_temp[j] #check in the dictionary the distance to each linked node
            pair_dist=graph.distances[pair]        
            node_dict[node_linked_temp[j]]=pair_dist # add it into node_dic
            # print(pair_dist)
        graph_dict[node_temp]=node_dict #add node_dic to the graph dict
    return graph_dict

# graph=get_linked_list(graph, node)


case_node2 = [0,1,2,3,4,5,6,7,8,9,10,11]
case_node1= [0,1,2,3,4,5,6,7]

# cases=["case1.txt", "case2.txt"]
# print("in case 1, path between V1~V8 is 0~7 in my design")
# print("in case 1, path between V7~V8 is 6~7 in my design")
# print("in case 2, path between V2~V8 is 1~7 in my design")
# print("in case 2, path between V12~V10 is 11~9 in my design")
# for i in range(2):
#     case=cases[i]
#     if i==0:
#         node=case_node1
#         print("This is case", case)
#         graph=make_case_lined_list_verify(case) 
#         graph=get_linked_list(graph, node)
#         results,pred=Floyd(graph)
#         # print(pred,"\n")
#         temp={}
#         result=results[0]
#         temp[0]=result
#         print("The shortest distance from V0~V7 is")
#         print(temp)
#         pred_=pred[0]
#         temp1=pred_[7]
#         temp2=pred_[temp1]
#         temp3=pred_[temp2]
#         print("The shortest path from V0~V7 is")
#         print(7,temp1,temp2,temp3)


#         temp={}
#         result=results[6]
#         temp[6]=result
#         print("The shortest distance from V6~V7 is")
#         print(temp)
#         pred_=pred[6]
#         temp1=pred_[7]
#         temp2=pred_[temp1]
#         print("The shortest path from V0~V7 is")
#         print(7,temp1,temp2,"\n")

#     if i==1:
#         node=case_node2
#         print("This is case", case)
#         graph=make_case_lined_list_verify(case) 
#         graph=get_linked_list(graph, node)
#         results,pred=Floyd(graph)
#         temp={}
#         result=results[1]
#         temp[1]=result
#         print("The shortest distance from V1~V7 is")
#         print(temp)
#         # print()
#         pred_=pred[1]
#         temp1=pred_[7]
#         temp2=pred_[temp1]
#         temp3=pred_[temp2]
#         temp4=pred_[temp3]
#         print("The shortest path from V0~V7 is")
#         print(7,temp1,temp2,temp3,temp4)
#         temp={}
#         result=results[11]
#         temp[11]=result
#         print(temp)
#         # print(pred)
#         pred_=pred[9]
#         temp1=pred_[11]
#         temp2=pred_[temp1]
#         temp3=pred_[temp2]
#         temp4=pred_[temp3]
#         temp5=pred_[temp4]
#         print("The shortest path from V0~V7 is")
#         print(11,temp1,temp2,temp3,temp4,temp5)
      

# print("---------------Floyd Algorithm complete graph----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for i in range(len(W_total)):
#     print("Start calculating  ", W_total[i],"node" )
#     start = time.time()
#     graph,node = make_case_lined_list_complte(W_total[i])
#     graph=get_linked_list(graph,node)
#     Floyd(graph)
#     end = time.time()
#     print("This is the time to get  ", W_total[i], "node  calculated" )
#     print(str(end-start))


# print("---------------Floyd Algorithm complete graph----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for i in range(len(W_total)):
#     print("Start calculating  ", W_total[i],"node" )
#     start = time.time()
#     graph,node = make_case_lined_list_sparse(W_total[i])
#     graph=get_linked_list(graph,node)
#     Floyd(graph)
#     end = time.time()
#     print("This is the time to get  ", W_total[i], "node  calculated" )
#     print(str(end-start))


print("---------------Floyd Algorithm complete graph memory analysis----------------")

node=100

print("Start calculating  ", node)
graph,node = make_case_lined_list_sparse(node)
graph=get_linked_list(graph,node)
Floyd(graph)
end = time.time()
print( "Analysis completeed" )

# print("---------------Floyd Algorithm sparse graph memory analysis----------------")

# node=100

# print("Start calculating  ", node)
# graph,node = make_case_lined_list_sparse(node)
# graph=get_linked_list(graph,node)
# Floyd(graph)
# end = time.time()
# print( "Analysis completeed" )