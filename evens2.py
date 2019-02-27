def even_number_of_evens(numbers):

    # Check to see if the list is empty
    if numbers == []:
        return False
    else:
        # Set a `number_of_evens` variable that will be incremented each time
        # an even number is found
        evens = 0
        
    # Iterate of over each item and if it's an even number, increment the
    # `evens` variable
    for number in numbers:
        if number % 2 == 0:
            evens += 1
    
    if evens == 0:
        return False
    else:
        return evens % 2 == 0

# Our set of test cases

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"


print("All tests passed!")