with open("brother_list.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    if "The Pennsylvania State University - Epsilon" in data[i]:
        data[i] = data[i].replace(
            "The Pennsylvania State University - Epsilon", "")
    if "Alumnus" in data[i]:
        data[i] = data[i].replace(
            "Alumnus", "")
    if "  Active Member" in data[i]:
        data[i] = data[i].replace(
            "  Active Member", ",,,Active Member")
    if " --" in data[i]:
        data[i] = data[i].replace(
            " -- ", ",")

with open("brother_list.txt", "w") as f:
    f.writelines(data)
