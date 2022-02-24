with open("data.csv", "r") as file:
    data = file.readlines()


for item in data[1:]:
    split_item = item.split(",")
    print(split_item[0])
    
