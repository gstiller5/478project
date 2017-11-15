import matplotlib.pyplot as plt
# input the file
file = open('20170901.as-rel2.txt', 'r')
# read the file line by line
data_lines = file.readlines()
data_lines = data_lines[652:] # takes out all the lines beginning with #
data = []

# separating the lines by the '|' character
# and stripping off the '\n' character
for x in data_lines:
    str = x.split('|')
    str[-1] = str[-1].rstrip()
    data.append(str)

as_list = set()
for x in data:
    # print(x)
    as_list.add(int(x[0]))
as_list = list(as_list)
as_list.sort()
# print(as_list)

as_list1 = []
for x in as_list:
    as_list1.append([x, 0])

print(as_list1)
for x in data:
    # ++ on the second number for the number at the index in as_list
    as_list1[as_list.index(int(x[0]))][1] += 1

print(as_list1)

