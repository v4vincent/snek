

# letter1 = 'a'
# letter2 = ''

# while letter1 != 'z':
#     letter2 = 'a'
#     while letter2 != 'z':
#         print(f"{letter1}{letter2}.com")
#         letter2 = chr(ord(letter2) + 1)
#     letter1 = chr(ord(letter1) + 1)

# 1A 1B 1C 2A 2B 2C 
num_rows = 2
num_cols = 3

counter = 1
counter2 = 1
letter = 65

# for i in range(num_rows):
#     for i in range(num_cols):


#         print(f'{counter}{chr(letter)}', end = ' ')
#         # counter+=1
#         letter+=1
#     # print()

# # end = " "

# while num_cols > 0:
#     counter = 1
#     while num_rows > 0:
#         print(f'{counter}{chr(letter)}', end = ' ')
#         letter += 1
#         num_rows -= 1
#     num_cols -= 1
    
# print()

for i in range(num_rows):
    for i in range(num_cols):
        print(f'{counter}{chr(counter2 + 64)}', end = ' ')
        counter2 += 1        
    counter += 1
    counter2 = 1
    
print()