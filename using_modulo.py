# days = int(input("How many days? "))
# years = days // 365
# days_remaining = days % 365
#
# print(days, "days is", years, "year(s) with", days_remaining, "remaining days")

user_val = 927

ones_digit = user_val % 10  # Ex: 927 % 10 is 7.
tmp_val = user_val // 10

print(ones_digit)
# print(tmp_val, end="\n\n")

tens_digit = tmp_val % 10
tmp_val = tmp_val // 10

print(tens_digit)
# print(tmp_val, end="\n\n")

hundreds_digit = tmp_val % 10
print(hundreds_digit)


amount_to_change = int(input())

num_fives = amount_to_change // 5

''' Your solution goes here '''

num_ones = (amount_to_change - (num_fives * 5)) % 10

print('Change for $', amount_to_change)
print(num_fives, '$5 bill(s) and', num_ones, '$1 bill(s)')