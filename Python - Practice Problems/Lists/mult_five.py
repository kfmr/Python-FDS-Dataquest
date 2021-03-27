"""create a function named mult_five, that given an order list of integers (without repetitions) ranging and including all numbers from 0 to n (for some positive integer n) returns a list consisting of the multiples of 
5""

def mult_five(a_list):
    return a_list[0::5] 


print(mult_five([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))