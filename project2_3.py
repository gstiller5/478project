import matplotlib.pyplot as plt
# input the file
file = open('routeviews-rv2-20171114-1800.txt', 'r')
# read the file line by line
data_lines = file.readlines()
data = []

# separating the lines by the '|' character
# and data_line_stringipping off the '\n' character
for x in data_lines:
    data_line_string = x.split()
    if ',' in data_line_string[-1]:
        data_line_string[-1] = data_line_string[-1].partition(",")[0]
    elif '_' in data_line_string[-1]:
        data_line_string[-1] = data_line_string[-1].partition("_")[0]
    data_line_string[-1] = data_line_string[-1].rstrip()
    data.append(data_line_string)

as_list = set()

for x in data:
    as_list.add(int(x[2]))

as_list = list(as_list)
as_list.sort()
# print(as_list)

as_list1 = []
for x in as_list:
    as_list1.append([x, 0])

# print(as_list1)
for x in data:
    # ++ on the second number for the number at the index in as_list
    as_list1[as_list.index(int(x[2]))][1] += 1

# print(as_list1)
bin1 = 0
bin2_5 = 0
bin5_100 = 0
bin100_200 = 0
bin200_1000 = 0
bin1000_plus = 0
as_list2 = []
for x in as_list1:
    as_list2.append(x[1])
    if x[1] == 1:
        bin1 += 1
    elif x[1] == 2:
        bin2_5 += 1
    elif x[1] < 5:
        bin5_100 += 1
    elif x[1] < 10:
        bin100_200 += 1
    elif x[1] < 20:
        bin200_1000 += 1
    else:
        bin1000_plus += 1

bin_list = [bin1, bin2_5, bin5_100, bin100_200, bin200_1000, bin1000_plus]
bin_list_strings = ['1', '2', '3-4', '5-9', '10-19', '20+']

# print(as_list2)
# print(bin_list)
# print(sum(bin_list))
total_bins_num = sum(bin_list)
for i in range(len(bin_list)):
    bin_list[i] = bin_list[i]/total_bins_num
# print(bin_list)
plt.bar(range(len(bin_list)), bin_list)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Graph 2 - AS Node Degree Distribution')
plt.xticks(range(len(bin_list)), bin_list_strings)
plt.show()
