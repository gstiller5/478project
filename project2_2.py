import matplotlib.pyplot as plt
# input the file
file = open('20170901.as-rel2.txt', 'r')
# read the file line by line
data_lines = file.readlines()
data_lines = data_lines#[646:]
data = []

# separating the lines by the '|' character
# and stripping off the '\n' character
for x in data_lines:
    str = x.split('|')
    str[-1] = str[-1].rstrip()
    data.append(str)

for x in data[625:655]:
    if x[0][0] != '#':
        print(x)
        print(data.index(x))
print(len(data))
print(data[651])
print(data[652])

