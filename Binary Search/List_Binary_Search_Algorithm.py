import math
import sys
n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m=[1,5,7,9,15,30,33,37,41,42,43,65,69]

target=69
# count=0
global nul_count
# nul_count=0
count=0
global counter
counter=0


def chunks(arr, m):
    n = int(math.ceil(len(arr) / float(m)))
    return [arr[i:i + n] for i in range(0, len(arr), n)]
def main(n,target,counter):
    global count
    # count=0
    sub=chunks(n,3)
    print(sub)
    xxx=0
    for i in range (len(sub)):
        sub_=sub[i]
        if len(sub_)==1:     
            if target == sub_[0]:
                counter=counter+i
                print("this is the index")
                print(counter)
                sys.exit(0)
            else:
                xxx=xxx+1
                if xxx==len(sub):
                    print("There is no such number")
                    sys.exit(0)

                



        else:
            if isinstance(sub_,list):
                if target < sub_[0] or target > sub_[-1]:
                    counter=counter+len(sub_)
                    print(counter)
                if target >= sub_[0] and target <= sub_[-1]:
                    print(counter)
                    main(sub_,target,counter)
                
main(m,target,counter)

