# Enter the clues
clue1_input = input("Enter Clue 1: ").strip()
clue2_input = input("Enter Clue 2: ").strip()
clue3_input = int(input("Enter Clue 3: ").strip())

decoded_message = chr(int("0x" + clue1_input, 16)) + chr(int(clue2_input, 2)) + chr(clue3_input)
print("decoded message:", decoded_message)
