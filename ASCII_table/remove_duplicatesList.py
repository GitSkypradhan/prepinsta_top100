# how to remove duplicates from list
l = [10,20,20,10,10,30,20,40]
temp_l = set(l)
l = list(temp_l)
sorted_list = sorted(l)
print(sorted_list)
