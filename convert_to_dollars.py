
quarters = int(input())
dimes = int(input())
nickles = int(input())
pennies = int(input())

final_value = (quarters * 25 / 100) + (dimes * 10 / 100) + (nickles * 5 / 100) + (pennies / 100)

print(f'Balance Amount: ${final_value:.2f}')