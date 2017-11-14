import matplotlib.pyplot as plt
# input the file
file = open('20150801.as2types.txt', 'r')
# read the file line by line
data_lines = file.readlines()
data_lines = data_lines[6:]
data = []

# separating the lines by the '|' character
# and stripping off the '\n' character
for x in data_lines:
    str = x.split('|')
    str[-1] = str[-1].rstrip()
    data.append(str)

# now we have an array of arrays of the data
# in the format ['1', 'peerDB_class', 'Transit/Access']

# part 2.1 - graph 1
tran_acc_count = 0
content_count = 0
enterprise_count = 0
for x in data:
    if x[2] == 'Transit/Access':
        tran_acc_count += 1
    elif x[2] == 'Content':
        content_count += 1
    elif x[2] == 'Enterpise':
        enterprise_count += 1

pie_data = [tran_acc_count, content_count, enterprise_count]
labels = ['Transit/Access', 'Content', 'Enterprise']
plt.pie(pie_data, labels=labels)
# plt.legend()
plt.title('Graph 1')
plt.show()

