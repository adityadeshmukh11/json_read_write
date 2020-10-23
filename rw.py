import json
with open("/home/aditya/Desktop/json_fetch/abc.json") as f:
    data=json.load(f)

ad_ip=input("enter ad ip ")
data['AD']=ad_ip


obj=json.dumps(data,indent=4)

with open("/home/aditya/Desktop/json_fetch/abc.json",'w') as f:
    f.write(obj)

