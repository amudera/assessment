from pprint import pprint

def jsondata():
    arr = {'data': [[1,2,3],[4,5,6],[7,8,9]]}
    arr2 = arr["data"]
    vals = sum(map(sum,arr2)) 
    print(vals)

jsondata()