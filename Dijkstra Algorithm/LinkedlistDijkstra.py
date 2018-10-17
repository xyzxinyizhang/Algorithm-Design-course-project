from collections import defaultdict, deque
import sys
import random
import time

#some of the code is from open source project and tutorial
#The referenced code should be less than 10 lines


# This class is obtained from a Python package, which can help users to build linked list. 
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
# @profile
def dijkstra(graph, initial):
    results = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in results:
                if min_node is None:
                    min_node = node
                elif results[node] < results[min_node]:
                    min_node = node
        nodes.remove(min_node)
        current_weight = results[min_node]
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in results or weight < results[edge]:
                results[edge] = weight
                path[edge] = min_node
    return results, path
    # return results
###################################################################################end dickstra####################################################

############################################################verify the test case################################################################
graph = Graph()
MAX=sys.maxsize
def read_case(case):
    case_matrix=[]
    file = open(case)
    while 1:
        line = file.readline()
        if not line:
            break
        line=line.split()   
        for i in range (len(line)):
            if line[i]== "99999": # i changed the  "." in test case to "99999" to easy read
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




cases=["case1.txt", "case2.txt"]
case1_node=[0, 6]
case2_node=[1, 9]
print("in case 1, path between V1~V8 is 0~7 in my design")
print("in case 1, path between V7~V8 is 6~7 in my design")
print("in case 2, path between V2~V8 is 1~7 in my design")
print("in case 2, path between V12~V10 is 11~9 in my design")
for i in range(2):
    case=cases[i]
    print("This is case", case)
    graph=make_case_lined_list_verify(case) 
    if i==0:
        case_node=case1_node
        for j in range(2):
          if j==0:
              results, path=dijkstra(graph, case_node[j])
              temp={}
              temp[case_node[j]]=results
              print("The shortest distance from V0~V7 is")
              print(temp) 
              # print(path)           
              temp1=path[7]
              temp2=path[temp1]
              temp3=path[temp2]
              print("The shortest path from V0~V7 is")
              print(7,temp1,temp2,temp3)
          if j==1:
              results, path=dijkstra(graph, case_node[j])
              temp={}
              temp[case_node[j]]=results
              print("The shortest distance from V6~V7 is")
              print(temp)
              # print(path)            
              temp1=path[7]
              temp2=path[temp1]
              print("The shortest path from V6~V7 is")
              print(7,temp1,temp2, "\n")
    if i==1:
        case_node=case2_node
        for j in range(2):
          if j==0:
              results, path=dijkstra(graph, case_node[j])
              temp={}
              temp[case_node[j]]=results
              print("The shortest distance from V1~V7 is")
              print(temp) 
              # print(path)           
              temp1=path[7]
              temp2=path[temp1]
              temp3=path[temp2]
              temp4=path[temp3]
              print("The shortest path from V1~V7 is")
              print(7,temp1,temp2,temp3,temp4)
          if j==1:
              results, path=dijkstra(graph, case_node[j])
              temp={}
              temp[case_node[j]]=results
              print("The shortest distance from V11~V9 is")
              print(temp)
              # print(path)            
              temp1=path[11]
              temp2=path[temp1]
              temp3=path[temp2]
              temp4=path[temp3]
              temp5=path[temp4]
              print("The shortest path from V11~V9 is")
              print(11,temp1,temp2,temp3,temp4,temp5)
# a very straid forward way to interpret path


############################################################end verify the test case################################################################

def RNG(n):
    return random.randint(1,n)
# @profile
def make_case_lined_list_complte(n):
    graph = Graph()
    for i in range (n):
        graph.add_node(i)
    for i in range (n):
        for j in range (n):
            if j>i:
                graph.add_edge(i, j, RNG(n))
            if j==i:
                graph.add_edge(i,j,0)
    return graph

# graph=make_case_lined_list_complte(5)
# print(graph.edges)
# @profile
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
    return graph



# graph=make_case_lined_list_sparse(6)
# print(dijkstra(graph, 0)) 

# print("---------------Dijkstra Algorithm complete graph----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for j in range(len(W_total)):
#     print("Start calculating  ", W_total[j] )
#     start = time.time()
#     W=make_case_lined_list_complte(W_total[j])
#     for i in range(W_total[j]):
#         dijkstra(W, i)
#     end = time.time()
#     print("This is the time to get  ", W_total[j], "  calculated" )
#     print(str(end-start))

# print("---------------Dijkstra Algorithm sparse graph----------------")
# W_total=[20,40,60,80,100,120,140,160,180,200]

# for j in range(len(W_total)):
#     print("Start calculating  ", W_total[j] )
#     start = time.time()
#     W=make_case_lined_list_sparse(W_total[j])
#     for i in range(W_total[j]):
#         dijkstra(W, i)
#     end = time.time()
#     print("This is the time to get  ", W_total[j], "  calculated" )
#     print(str(end-start))


print("---------------Dijkstra Algorithm complete graph----------------")
W_total=[20,40,60,80,100,120,140,160,180,200]

for j in range(len(W_total)):
  if j==4:
      print("Start calculating  ", W_total[j] )
      start = time.time()
      W=make_case_lined_list_sparse(W_total[j])
      for i in range(W_total[j]):
          dijkstra(W, i)

      end = time.time()
      print("This is the time to get  ", W_total[j], "  calculated" )
      print(str(end-start))



