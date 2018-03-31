import random


def numeral_to_str(n):
    # This function converts numeral to string for output it
    # Array numbers
    array_str_numbers = [[" # # ", "#   #", "#   #", "#   #", " # # "],  # 0
                         ["  #  ", "# #  ", "  #  ", "  #  ", "# # #"],  # 1
                         ["# # #", "    #", "# # #", "#    ", "# # #"],  # 2
                         ["# # #", "    #", "# # #", "    #", "# # #"],  # 3
                         ["#   #", "#   #", "# # #", "    #", "    #"],  # 4
                         ["# # #", "#    ", "# # #", "    #", "# # #"],  # 5
                         ["# # #", "#    ", "# # #", "#   #", "# # #"],  # 6
                         ["# # #", "    #", "  #  ", "  #  ", "  #  "],  # 7
                         ["# # #", "#   #", "# # #", "#   #", "# # #"],  # 8
                         ["# # #", "#   #", "# # #", "    #", "# # #"]]  # 9
    str_num = ""
    for i in range(0, 5):
        for j in n:
            str_num += array_str_numbers[j][i] + "    "
        str_num += "\n"
    return str_num


print("Hi!\nHow much dices would you roll?")
amount_of_dices = int(input())
print("Type ENTER when you will be ready to ROLL the dice.")

while True:
    input()
    temp = []
    for i in range(amount_of_dices):
        temp.append(random.randint(1, 6))
    print(numeral_to_str(temp))
    print("\nType ENTER when you will be ready to ROLL the dice again.")
