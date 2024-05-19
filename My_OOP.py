class STR:
    def __init__(self,content) :
        self.content=content
        self.lencontent=len(self.content)
        self.isdigitcontent=self.content.isdigit()

    def __str__(self):
        return f"content of str: {self.content}\nlenght of str: {self.lencontent}\ncontent is digit: {self.isdigitcontent}"


    def adding_sth(self,beginning,endding):
        self.content=beginning + self.content + endding
        self.lencontent=len(self.content)
        self.isdigitcontent=self.content.isdigit()
        return self.content

    def removing_nums(self):
        x=""
        for i in self.content:
            if not i.isdigit():
                x+=i
        self.content=x
        self.lencontent=len(self.content)
        self.isdigitcontent=self.content.isdigit()
        return self.content


    def removing_str(self):
        x=""
        for i in self.content:
            if i.isdigit():
                x+=i
        self.content=x
        self.lencontent=len(self.content)
        self.isdigitcontent=self.content.isdigit()
        return self.content

    def removing_spaces(self):
        self.content=self.content.replace(" ","")
        self.lencontent=len(self.content)
        self.isdigitcontent=self.content.isdigit()
        return self.content

    
    def adding_nums(self):
        x=0
        
        for i in self.content:
           if i.isdigit():
              x+=ord(i)-48
        
        return x 



#-----------------------------------------------------------------------------------------------------------
# Making instence: 
#-----------------------------------------------------------------------------------------------------------

str1=STR("soheil92")
str2=STR(input("Enter your strings: "))


print(str2)
