from cal_func import do_addition,do_subtraction
from multiply import do_multiplication
from area import area_for_rectangle

select_option = input("""
CALCULTOR
1. to add
2. to subtract
3. to multiply
4. to area
                      
""")

a = int(input('enter 1st no. '))
b = int(input('enter 2nd no. '))

if select_option == '1':
    print(f'The result is {do_addition(a,b)}')
elif select_option == '2':
    print(f'The result is {do_subtraction(a,b)}')
elif select_option == '3':
    print(f'The result is {do_multiplication(a,b)}')
elif select_option == '4':
    print(f'The result is {area_for_rectangle(a,b)}')

