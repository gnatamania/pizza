import json
from collections import Counter

json_filename = 'pizza_request_dataset/pizza_request_dataset.json'
json_data=open(json_filename)
data = json.load(json_data)
json_data.close()

pizza_w = []
pizza_l = []

for x in range(len(data)):
  if data[x]["requester_received_pizza"]:
    pizza_w.append(data[x]["request_text"].split())
  else:
    pizza_l.append(data[x]["request_text"].split())

pizza_l = sum(pizza_l, [])
pizza_w = sum(pizza_w, [])

pizza_l_u = list(set(pizza_l))
pizza_w_u = list(set(pizza_w))

# Transform words to lower-case. 
pizza_l_lower =  map(lambda s: s.lower(), pizza_l)
pizza_w_lower =  map(lambda s: s.lower(), pizza_w)

# Calculate the N most common words with their frequencies.
pizza_l_freqlst = Counter(pizza_l_lower)
pizza_w_freqlst = Counter(pizza_w_lower)

# Top 500 words.
top_words = 500
pizza_l_mcommon = pizza_l_freqlst.most_common()[:top_words]
pizza_w_mcommon = pizza_w_freqlst.most_common()[:top_words]

# P(pizza) och P(~pizza)

p_pizza = 0;
p_not_pizza = 0;

for x in range(len(data)):
  if data[x]["requester_received_pizza"]:
    p_pizza = p_pizza + 1

p_not_pizza = len(data) - p_pizza;

p_pizza = p_pizza/float(len(data))
p_not_pizza = 1.0 - p_pizza


# P(w_i | pizza) = pizza_w_lower.count(w_i)

# P(pizza | w1, w2, w3, ..., w_n) = P(pizza)*P(w1|pizza)*P(w2|pizza)*...*P(w_n|pizza)/Z

all_words = pizza_l_lower + pizza_w_lower
