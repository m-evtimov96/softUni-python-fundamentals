factor = int(input())
count = int(input())
num_list = []

for counter in range(1,count+1):
    num_list.append(int(counter*factor))

print(num_list)
