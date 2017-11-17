import matplotlib.pyplot as plt
# input the file
file = open('20170901.as-rel2.txt', 'r')
# read the file line by line
data_lines = file.readlines()
data_lines = data_lines[652:] # takes out all the lines beginning with #
data = []

# separating the lines by the '|' character
# and data_line_stringipping off the '\n' character
for x in data_lines:
    data_line_string = x.split('|')
    data_line_string[-1] = data_line_string[-1].rstrip()
    data.append(data_line_string)

as_list = set()
for x in data:
    # print(x)
    as_list.add(int(x[0]))
    as_list.add(int(x[1])) # added
as_list = list(as_list)
as_list.sort()
# print(as_list)

as_list1 = []
for x in as_list:
    # [num, peers, customers, connections(total)]
    as_list1.append([x, 0, 0, 0])

print(as_list1[:100])
print('as_list1: ' + str(len(as_list1)))
print('data: ' + str(len(data)))
for x in data:
    if int(x[2]) == 0: # peer | peer
        # add to peer count
        as_list1[as_list.index(int(x[0]))][1] += 1
        as_list1[as_list.index(int(x[1]))][1] += 1
        # add to connections(total)
        as_list1[as_list.index(int(x[0]))][3] += 1
        as_list1[as_list.index(int(x[1]))][3] += 1  # added
    elif int(x[2]) == -1: # provider | customer
        # add to the customer count of the provider
        as_list1[as_list.index(int(x[0]))][2] += 1
        # add to connections(total)
        as_list1[as_list.index(int(x[0]))][3] += 1
        as_list1[as_list.index(int(x[1]))][3] += 1


print(as_list1[:100])

tran_acc_count = 0
content_count = 0
enterprise_count = 0
for x in as_list1:
    # need logic for sorting out the pie chart data
    if x[3] >= 2 and x[1] == 0 and x[2] == 0: # enterprise
        enterprise_count += 1
    elif x[2] == 0 and x[1] > 0:
        content_count += 1
    elif x[2] != 0:
        tran_acc_count += 1

pie_data = [tran_acc_count, content_count, enterprise_count]
print(pie_data)
labels = ['Transit/Access', 'Content', 'Enterprise']
plt.pie(pie_data, labels=labels)
# plt.legend()
plt.title('Graph 4')
plt.show()


