"""create a function skip_two, that given a list, returns a list that:

Skips every two elements of the input.
Starts with the second element of the input list."""

def skip_two(a_list):
        return a_list[1:11:3]
        
        
        
print(skip_two(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']))


#create a function skip_one, that given a list, returns a list that skips every other element and includes the first one

def skip_one(a_list):
    return a_list[0::2]

print(skip_one(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))