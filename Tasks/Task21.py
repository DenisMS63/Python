# Программа для печати всех уникальных значений в словаре.

# Input: [{"V":"S001"},{"V":"S002"}, {"VI":"S001"}, {"VI":"S005"},
#         {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# Output: {"S005", "S002", "S007", "S001", "S009"}

list_dict = [{"V":"S001"},{"V":"S002"}, {"VI":"S001"}, {"VI":"S005"},
             {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

unique_value = set()

for cur_dict in list_dict:
    for key in cur_dict:
        unique_value.add(cur_dict[key])
    
print(unique_value)