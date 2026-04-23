
#for_list

numbers = [11,22,98,54,63,45,20,45]

for number in numbers:
    print(number%10, end='\t')

#for_tuple

numbers = (11,22,98,54,63,45,20,45)

for number in numbers:
    print(number%10, end='\t')

#for_ set

numbers = {11,22,98,54,63,45,20,45}

for number in numbers:
    print(number%10, end='\t')

#for_dict

stud = {'rno':'101', 'name':'AAA', 'city':'Mumbai'}

for k,v in stud.items():
    print(k , '--', v)