class Validator:
    """ check self.card length, type, and run Luhn validation """


    def __init__(self, card):
        # self.card type requirements for left-most digits
        self.mc_digits = [51, 52, 53, 54, 55]
        self.amex_digits = [34, 37]
        self.visa_digits = [4]
        self.discover_digits = [6011]


        self.card = card

        self.length = len(card) # number of digits
        self.type = self.get_card_type() # amex, discovery, mc, visa, or null

        self.rules_registry = [self.check_length, self.is_card_type_valid, self.blank_check]
        


    def get_card_type(self):
        """Determines the card type"""
        ## otherwise return false
        if self.length == 16:
            if int(self.card[0]) in self.visa_digits:
                return 'visa'
            elif int(self.card[:2]) in self.mc_digits:
                return 'mc'
            elif int(self.card[:4]) in self.discover_digits:
                return 'discover' 
            else:
                return "Invalid"
        elif self.length == 15:
            if int(self.card[:2]) in self.amex_digits:
                return 'amex'
            else:
                return "Invalid"            
        else:
            return  "Invalid"



    def check_length(self):
        """ if self.card length 15 or 16 return True, otherwise False """

        # if self.card length is valid change self.length value
        ## otherwise return false
        return (self.length == 15 or self.length == 16)



    def is_card_type_valid(self):
        """ check length-digit matches for self.card types """

        # if length/digit requirements match then assign self.card type, return True
        return self.type != "Invalid"



    def valid(self):
        """ test Luhn validation """

        # reverse self.card numbers in list form
        reversed_card_list = [int(x) for x in self.card[::-1]]

        # double every even digit in reversed list
        doubled_digits = [x * 2 for x in reversed_card_list[::2]]

        # extract the not-doubled (odd) digits from reversed list
        notdoubled_digits = [x for x in reversed_card_list[1::2]]

        # iterate through each digit in doubled and notdoubled lists

        total = 0
        for l in str(doubled_digits + notdoubled_digits):
            ## sum each of the digits
            if l.isdigit():
                total += int(l)

        # if modulo of total is zero, then number is valid
        return (total % 10 == 0)


    def blank_check(self):
        return False


    def perform_validation(self):
        """ Run tests length, type, luhn. Valid if all three True """
        # return (self.check_length() and self.is_card_type_valid() and self.valid())

        result = True
        for rule in self.rules_registry:
            result = result and rule()

        return result



myCard = '347650202246884'
test = Validator(myCard)

## Asserts to verify initialization
assert test.card == '347650202246884'
assert test.length == 15
assert test.type == "amex"


assert test.check_length() == True
assert test.is_card_type_valid() == True

assert test.valid() == False

assert test.perform_validation() == False
