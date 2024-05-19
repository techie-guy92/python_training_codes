from tkinter import *
from mysql.connector import connect,Error



#--------------------------------------Creating Database And Tabels-------------------------------------------------
# try:

#     with connect(host="localhost",user="root",password="Soheil0014",database="db_Tesla_Tech") as db:
#         myCursor=db.cursor()

        # myCursor.execute("create database db_Tesla_Tech")
        # db.commit()
       
        # myCursor.execute("create table T_Users(ID int primary key auto_increment, First_Name VarChar(50) not null, Last_Name VarChar(50) not null, Age int(50) not null, Gender VarChar(50) not null, Marrital_Status VarChar(50) not null, Date_Of_register datetime not null)")
        # db.commit()

          # myCursor.execute("Update T_Users set ID=1  where ID=2")
        # db.commit()

        # myCursor.execute("Delete from T_Users where id=1 ")
        # db.commit()

# except Error as error:
#     print(error)
#---------------------------------------------------------------------------------------------------------


def sign_in():
    

    try:
        
        fname=first_name_e.get().capitalize()
        lname=last_name_e.get().capitalize()
        agee=age_e.get()
        malee=male_status.get()
        femalee=female_status.get()
        singlee=single_status.get()
        marriedd=married_status.get()

        
        if len(fname) == 0 or len(lname) == 0 or len(agee) == 0:
            greeting.config(text="All fiels must be filled")
            
        elif  malee == 0  and femalee == 0:
            greeting.config(text="You must choose your gender")
            
        elif  malee == 1  and femalee == 1:
            greeting.config(text="You must not choose both genders")
              
        elif  singlee == 0  and marriedd == 0:
            greeting.config(text="You must choose your marital status")
                
        elif  singlee == 1  and marriedd == 1:
            greeting.config(text="You must not choose both marital status")
               
     
        else:
                
            if malee == 0 or femalee == 1:
                genderr="Female"
            elif malee == 1 or femalee == 0:
                genderr="Male"

            if singlee == 0 or marriedd == 1:
                m_status="Married"
            elif singlee == 1 or marriedd == 0:
                m_status="Single"
                
            greeting.config(text=f"""Welcome dear {fname} {lname}\nYour information has been saved up,\nnow you are able to follow your interests""")
            login_to_db(fname,lname,agee,genderr,m_status)



    except Error as error:
        greeting.config(text=error)
            
      


def login_to_db(fname,lname,agee,genderr,m_status):

    with connect(host="localhost",user="root",password="Soheil0014",database="db_Tesla_Tech") as db: 
        myCursor=db.cursor()
    
        try:

            myCursor.execute("SET time_zone = '+03:30'")
            
            new_commer1="Insert into T_Users(First_Name,Last_Name,Age,Gender,Marrital_Status,Date_Of_register) values(%s,%s,%s,%s,%s,now())"
            new_commer2=(fname,lname,agee,genderr,m_status)
            myCursor.execute(new_commer1,new_commer2)
            db.commit()

        except Error as error:
            greeting.config(text=error)
            print(error)
            db.rollback()
            db.close()

        

root=Tk()

root.title("Questionnaire")
root.iconbitmap("Files/Icons/questionnaire.ico")

w=300
h=300
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
root.resizable(width=False,height=False)



greeting=Label(root,text="")
first_name_l=Label(root,text="First Name",fg="Black",width=12)
last_name_l=Label(root,text="Last Name",fg="Black",width=12)
age_l=Label(root,text="Age",fg="Black",width=12)
matrial_status_l=Label(root,text="Marital Status",fg="Black",width=12)
gender=Label(root,text="Gender",width=12)
sign_in_b=Button(root,text="Sign up",fg="Black",width=15,command=sign_in)


first_name_e=Entry(root,width=12)
last_name_e=Entry(root,width=12)
age_e=Entry(root,width=12)
male_status=IntVar()
female_status=IntVar()
male=Checkbutton(root,text="Male",width=5,variable=male_status)
female=Checkbutton(root,text="Female",width=5,variable=female_status)
single_status=IntVar()
married_status=IntVar()
single=Checkbutton(root,text="Single",width=5,variable=single_status)
married=Checkbutton(root,text="Married",width=5,variable=married_status)

greeting.grid(row=0,column=0,columnspan=8)
first_name_l.grid(row=1,column=0,padx=2,pady=2)
last_name_l.grid(row=2,column=0,padx=2,pady=2)
age_l.grid(row=4,column=0,padx=2,pady=2)
gender.grid(row=5,column=0,padx=2,pady=2)
matrial_status_l.grid(row=6,column=0,padx=2,pady=2)

first_name_e.grid(row=1,column=1,padx=2,pady=2)
last_name_e.grid(row=2,column=1,padx=2,pady=2)
age_e.grid(row=4,column=1,padx=2,pady=2)
male.grid(row=5,column=1,padx=2,pady=2)
female.grid(row=5,column=2,padx=2,pady=2)
single.grid(row=6,column=1,padx=2,pady=2)
married.grid(row=6,column=2,padx=2,pady=2)
sign_in_b.grid(row=7,column=0,padx=2,pady=2,columnspan=3)


root.mainloop()