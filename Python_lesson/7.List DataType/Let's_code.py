person1=["David Doe",20,1,180.0,100.0]
person2=["John Smith",25,1,170.0,70.0]
person3=["Jane Carter",22,0,169.0,60.0]
person4=["Peter Kelly",40,1,150.0,50.0]
person_list = person1+person2+person3+person4
n_person = int(len(person_list)/4)
age=person_list[1::5]

print(person_list[1::3])
print(person_list[1::5])
print(age)
age_sum=sum(age)
avg_age =float(age_sum/n_person)

print("Average age is " + str(avg_age) + ".")
