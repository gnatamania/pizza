import json
from pprint import pprint

file_directory = "~/pizza/train.json"
json_data=open('json_data')

data = json.load(json_data)
json_data.close()  

pizza_w = []
pizza_l = []

for x in range(0, len(data)):
   
  if data[x]["requester_received_pizza"]:
    
    pizza_w.append(data[x]["request_text"].split())
  else:
    pizza_l.append(data[x]["request_text"].split())
                
pizza_l = sum(pizza_l, [])
pizza_w = sum(pizza_w, [])

pizza_l_u = list(set(pizza_l))
pizza_w_u = list(set(pizza_w))