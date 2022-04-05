given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_of_input_element = int(input("Enter The Number of element in the list = "))
input_list = []
for x in range(0, number_of_input_element):
    number = int(input("Enter the number = "))
    input_list.append(number)

my_dict = {}

# input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]


def multiple_calculator(in_li):
    for gl in given_list:
        count = 0
        for il in in_li:
            if il % gl == 0:
                count += 1
            else:
                pass
        my_dict.update({gl: count})
    return my_dict


print(multiple_calculator(input_list))
