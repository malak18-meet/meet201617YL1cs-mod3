from student import Student
shira=Student("shira","Kfar Tavor","15","1.68","Cookies and Cream")
malak=Student("malak","nazareth","15","1.75","chocolate")
avigail=Student("avigail","manof","15","1.73","chocolate")
shira.print_summary()
malak.print_summary()
avigail.print_summary()
s=shira.get_giraffe_gap()
m=malak.get_giraffe_gap()
a=avigail.get_giraffe_gap()
print(s , m , a)
