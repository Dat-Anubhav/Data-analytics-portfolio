'''Q16:- Define a decorator function that prints 'Executing function...' before executing a function 
and 'Function executed.' after executing it. Apply this decorator to a function that takes a 
list of integers and returns their sum. Test the decorated function with different lists.'''

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Executing function...')
        result = func(*args, **kwargs)
        print('Function executed.')
        return result
    return wrapper

@my_decorator
def sum_list(lst):
    return sum(lst)

# Test
print(sum_list([1, 2, 3, 4, 5]))  # 15