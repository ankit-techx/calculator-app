from cal_func import do_addition,do_subtraction

select_option = input("""
CALCULTOR
1. to add
2. to subtract
""")

a = int(input('enter 1st no. '))
b = int(input('enter 2nd no. '))

if select_option == '1':
    print(f'The result is {do_addition(a,b)}')
elif select_option == '2':
    print(f'The result is {do_subtraction(a,b)}')

