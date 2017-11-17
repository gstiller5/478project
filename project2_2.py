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
    as_list1.append([x, 0])

print(as_list1)
print(len(as_list1))
for x in data:
    # ++ on the second number for the number at the index in as_list
    as_list1[as_list.index(int(x[0]))][1] += 1
    as_list1[as_list.index(int(x[1]))][1] += 1 # added

print(as_list1)

bin1 = 0
bin2_5 = 0
bin5_100 = 0
bin100_200 = 0
bin200_1000 = 0
bin1000_plus = 0
for x in as_list1:
    if x[1] == 1:
        bin1 += 1
    elif x[1] < 5:
        bin2_5 += 1
    elif x[1] < 100:
        bin5_100 += 1
    elif x[1] < 200:
        bin100_200 += 1
    elif x[1] < 1000:
        bin200_1000 += 1
    else:
        bin1000_plus += 1

bin_list = [bin1, bin2_5, bin5_100, bin100_200, bin200_1000, bin1000_plus]
bin_list_strings = ['1', '2-5', '5-100', '100-200', '200-1000', '1000+']


print(bin_list)
print(sum(bin_list))
total_bins_num = sum(bin_list)
for i in range(len(bin_list)):
    bin_list[i] = bin_list[i]/total_bins_num
print(bin_list)
plt.bar(range(len(bin_list)), bin_list)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Graph 2 - AS Node Degree Distribution')
plt.xticks(range(len(bin_list)), bin_list_strings)
plt.show()

