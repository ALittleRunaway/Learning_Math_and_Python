with open("file.txt", "r") as f:
    strings = f.readlines()
for i in range(len(strings)):
    strings[i] = strings[i].strip()
file_take = strings[0]
file_give = strings[1]
row_number = int(strings[2])

with open(file_take, "r") as f:
    i = 0
    for line in f:
        i += 1
        if i == row_number + 1:
            gived_string = line.strip().lower()

with open(file_give, "a") as f:
    f.write("\n" + gived_string)


# Содержимое students.txt
# FFFFFFFFFFF 5 5 5
# ZZZZZZZZZZZ 5 5 5
# hklhkhlkaaaaaa cbb a b c dfa b12312
