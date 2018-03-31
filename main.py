import random


def numeral_to_str(n):
    # This function converts numeral to string for output it
    if n == 0:
        str_num = " ### \n#   #\n#   #\n#   #\n ### "
    if n == 1:
        str_num = "  #  \n# #  \n  #  \n  #  \n# # #"
    if n == 2:
        str_num = "# # #\n    #\n# # #\n#    \n# # #"
    if n == 3:
        str_num = "# # #\n    #\n# # #\n    #\n# # #"
    if n == 4:
        str_num = "#   #\n#   #\n# # #\n    #\n    #"
    if n == 5:
        str_num = "# # #\n#    \n# # #\n    #\n# # #"
    if n == 6:
        str_num = "# # #\n#    \n# # #\n#   #\n# # #"
    if n == 7:
        str_num = "# # #\n    #\n  #  \n  #  \n  #  "
    if n == 8:
        str_num = "# # #\n#   #\n# # #\n#   #\n# # #"
    if n == 9:
        str_num = "# # #\n#   #\n# # #\n    #\n# # #"
    return str_num


print("Hi!\nType ENTER when you will be ready to ROLL the dice.")
while True:
    input()
    print(numeral_to_str(random.randint(1, 6)))
    print("\nType ENTER when you will be ready to ROLL the dice again.")
