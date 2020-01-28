def palindrome(string):

   if len(string) == 0 or len(string) == 1:
       return True

   if string[0] != string[-1]:
       return False

   return palindrome(string[1:-1])


a = palindrome('matam')
print("Return value {}".format(a))

assert a == True, "Should detect it as a palindrome"