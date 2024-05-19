#-------------------------------------------------------------------------------------------------------
# It is a company (class) which has some male and female employees: 
# Total number of employees are shown and numbers of employees in each group.
# Total salary of employees are shown and avrage salary of employees in each group.
# Also avrage age of employess are shown and avrage age of employess in each group. 
#-------------------------------------------------------------------------------------------------------
from abc import ABC,abstractclassmethod

class Person(ABC):

    def __init__(self,fname,lname,age,gender,birthPlace):
         self._fname=fname.capitalize()
         self._lname=lname.capitalize()
         self._gender=gender.capitalize()
         self._age=age
         self._birthPlace=birthPlace.capitalize()

    @abstractclassmethod
    def show_info(self):
        pass 

#Child---------------------------------------------------------------------------------------------------

class Employee(Person):

    # counter=0

    def __init__(self, fname, lname, age, gender, birthPlace, Id, salary, position):
        Person.__init__(self, fname, lname, age, gender, birthPlace)
        self.ID=Id
        self.salary=salary
        self.position=position
        self.menlist=[]
        self.womenlist=[]
        # Employee.counter+=1
    
    def show_info(self):
        print(f"""Full Name: {self._fname} {self._lname} 
Age: {self._age}
Birth Place: {self._birthPlace} 
ID: {self.ID} 
Salary: {self.salary} 
Position: {self.position}\n""")

    def show_men_info(self):
        age=0
        salary=0
        for em in self.menlist:
            em.show_info()
            age+=em._age
            salary+=em.salary
            print(f"Number of men employees: {len(self.menlist)}")
            print(f"Avrage age of men employees: {age / len(self.menlist)}")
            print(f"Avrage salary of men employees: {salary / len(self.menlist)}")
            print(f"Total salary of men employees: {salary}\n")
    
    def show_women_info(self):
        age=0
        salary=0
        for em in self.womenlist:
            em.show_info()
            age+=em._age
            salary+=em.salary
            print(f"Number of women employees: {len(self.womenlist)}")
            print(f"Avrage age of women employees: {age / len(self.womenlist)}")
            print(f"Avrage salary of women employees: {salary / len(self.womenlist)}")
            print(f"Total salary of women employees: {salary}\n")

    def addToMenList(self,man):
        self.menlist.append(man)
    
    def addToWomenList(self,woman):
        self.womenlist.append(woman)

    def show_employees(self):
        bothGroupSalary=[] 
        bothGroupAge=[] 
    
        for em in self.menlist:
            bothGroupSalary.append(em.salary)
            bothGroupAge.append(em._age)
            print(em._fname,em._lname)
        for em in self.womenlist:
            bothGroupSalary.append(em.salary)
            bothGroupAge.append(em._age)
            print(em._fname,em._lname)

        print(f"\nNumber of employees: {len(self.menlist)+len(self.womenlist)}")
        print(f"Total salary of employees: {sum(bothGroupSalary)}")
        print(f"Avrage age of employees: {sum(bothGroupAge)/len(bothGroupAge)}")
        print(f"Avrage salary of employees: {sum(bothGroupSalary)/len(bothGroupSalary)}\n")


#----------------------------------------------------------------------------------------------------
# Making instances: 
#----------------------------------------------------------------------------------------------------

em1=Employee("soheil","daliri",31,"male","tehran",7321,23000000,"programmer")
em2=Employee("omid","hashemi",32,"male","tehran",9107,13000000,"graphist")
em3=Employee("negin","sarlak",26,"female","tehran",3456,18000000,"lawyer")
em4=Employee("najmeh","golestan",34,"female","tehran",4276,10000000,"psychologist")
em5=Employee("mohammad","veskati",36,"male","varamin",6342,8000000,"accountant")
em6=Employee("ali","hallaj",38,"male","tehran",1391,10000000,"electrician")
em7=Employee("mansoureh","afshar",34,"female","tehran",1398,7000000,"coach")
em8=Employee("hamid","nasirzadeh",39,"male","tehran",1397,12000000,"versatile")
em9=Employee("tara","ochizi",37,"female","tehran",1400,10000000,"architect")
em10=Employee("mona","rezaei",30,"female","shiraz",2698,6000000,"secretary")

#----------------------------------------------------------------------------------------------------
# Running code: 
#----------------------------------------------------------------------------------------------------

em1.addToMenList(em1)
em1.addToMenList(em2)
em1.addToMenList(em5)
em1.addToMenList(em6)
em1.addToMenList(em8)
em1.addToWomenList(em3)
em1.addToWomenList(em4)
em1.addToWomenList(em7)
em1.addToWomenList(em9)
em1.addToWomenList(em10)


em1.show_employees()
# em1.show_men_info()
# em1.show_women_info()
# em1.show_info()