my_list = ['1', '12', '123', '1234', '12345', 'aa', 'bbbbb', 'c', '123123123', 'asfbwdbw', 'gwethwfvw', 'adfgwe', 'qr']

lenght_of_my_list = len(my_list)
filtered_list = []
for i in range(lenght_of_my_list):
    if len(my_list[i]) <= 3:
        filtered_list.append(my_list[i])

print(my_list)
print(filtered_list)



