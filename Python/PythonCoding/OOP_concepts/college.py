

class College:
    def __init__(self, ccode, cname, ccity):
        self._collcode = ccode
        self._collname = cname
        self._collcity = ccity

    def welcome_message(self):
        print('Hello There !!!')

    def display_college_details(self):
        print(f'College code: {self._collcode} \nCollege Name: {self._collname} \nCity: {self._collcity}')



