from OOP_concepts.agecalc import AgeCalculation
from OOP_concepts.myexception import AgeException

age = int(input('Age: '))

aobj = AgeCalculation()


try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)

except AgeException as ae:
    print(ae)
else:
    print('Eligible. Contact next step...')

finally:
    print('Done, thank you')







