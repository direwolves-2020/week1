###Duplication_1

new_string = []
# Global Variable. No use outside the function, should be declared within the function.

def remove_consecutive(string):
    # Good practice to add a comment as to what function should do
    """Removes occurances of consecutive duplicate characters in a string"""
    
    new_string = [string[0]]

    for i in range(len(string)):
        letter = (string[i])

        if letter != new_string[-1]:
        # The idea is correct here, but could be more efficient.
        # the check if its the first character need occur only once, but here it will be run on every iteration
        # More efficient to initialize new_string to the first character of string before starting the loop
            new_string.append(letter)

    # Good idea to use a list and append to it, rather than appending to a string variable

    return (''.join(new_string))
    # Returns a list, when instead what is needed is a string. ''.join(new_string)

# Always good to add an assert statement right at the end, so anyone reviewing your code can just run the file as is
# to first check whether the code works.
assert remove_consecutive('somessstringgg') == 'somestring', "Expected somestring back from the run"



def remove_cons(str):
    """Removes consecutive occurrances of duplicate characters in a string"""

    new_string = [str[0]]

    for i in range(1, len(str)):
        if str[i] != str[i-1]:
            new_string.append(str[i])

    return (''.join(new_string))

assert remove_cons('somessstringgg') == 'somestring'


def remove_consective_soln(str):
    """Removes consecutive occurrances of duplicate characters in a string"""

    str_list = [str[i] for i in range(1, len(str)) if str[i] != str[i-1]]

    return ''.join([str[0]] + str_list)

assert remove_consective_soln('someeesssos') == 'somesos', "Should remove duplicate characters in the input string"

