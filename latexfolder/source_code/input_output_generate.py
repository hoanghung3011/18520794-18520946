import random as random
def rand_list(list_to,sotien,list_tien):
  foo =[500000,200000,100000,50000,20000]
  #random.seed(0)  # don't use seed function, if you want different results in each run
  for i in range(10):
    list_tien += random.sample(foo,4)
  list_to += random.sample(list_tien,10)
  for i in list_to:
    sotien = sotien + i
  return list_tien,sotien,list_to
n = 0 
list_tien = []
list_totien = []
list_sotien = []
while n < 1000 :
  sotien = 0
  list_to = []
  list_tien2 = []
  list_tien2,sotien,list_to = rand_list(list_to,sotien,list_tien2)
  list_tien.append(list_tien2)
  n += 1
  list_totien.append(list_to)
  list_sotien.append(sotien)
  list_tien2.clear
  list_to.clear

import pandas as pd
data = {
    'List tien':list_tien,
    'So tien can rut':list_sotien,
    'To tien tra ra' : list_totien
}
data = pd.DataFrame(data)
print(data)
data.to_csv("data_test.csv",index=False)