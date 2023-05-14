def capitalize(String):
    return String.title()
capitalize("snow") # [Snow] берем из обоих веток
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]

def merge(dic1,dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1={1:"start", 2:"end"} # берем из master
dic2={3:"Python", 4:"Programming"}
merge(dic1,dic2) # {1: 'start', 2: 'end', 3: 'Python', 4: 'Programming'} # берем из master

import time
start_time= time.time()
def fun():
    a=2
    b=3
    c=a+b # берем из feature
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken)