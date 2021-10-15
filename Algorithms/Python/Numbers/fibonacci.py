"""Fibonacci series with a twist!
    It will return the list of all Fibonacci numbers leading up to the Fibonacci number that is bigger 
    (or equal) than the number passed in as argument.
    Ex : fibonacci(10) return [0,1,1,2,3,5,8,13]
    Ex : fibonacci(5) return [0,1,1,2,3,5]
    """


def fibonacci(number):
    fibo_list = [0, 1]
    if number == 0:
        fibo_list = [0]
    while fibo_list[-1] < number:
        next_num = fibo_list[-2] + fibo_list[-1]
        fibo_list.append(next_num)
    return fibo_list


num = int(input("Enter the number until where fibonacci series is to be printed : "))
print(fibonacci(num))
