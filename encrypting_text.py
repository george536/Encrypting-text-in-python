class Encryption:
    def __init__(self, option,text):
        self.option=option
        self.text=text
        self.scripted=""
        chars=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','?',',','!',' ','1','2','3','4','5','6','7','8','9','0','(',')']
        self.chars=chars



    def generate(self):
        import random
        scripted=[]
        while True:
            num=random.randint(0,67)
            if num not in scripted:
                scripted.append(num)
                if len(scripted)==68:
                    break;
        new_list=[]
        for i in scripted:
            temp=self.chars[i]+str(random.randint(0,1000))
            new_list.append(temp)
        scripted=new_list

        file=open('testfile.txt','w')
        for i in scripted:
            file.write(str(i))
            file.write("\n")
        file.close()
        self.scripted=scripted





    def convert(self):
        file=open('testfile.txt','r')
        scripted=[]
        for line in file:
            scripted.append(line)

        new_text=[]
        for letter in self.text:
            num=self.chars.index(letter)
            new_text.append(scripted[num])

        self.new_text=new_text




    def convert_back(self):
        file=open('testfile.txt','r')
        scripted=[]
        for line in file:
            scripted.append(line.strip("\n"))

        text=[]
        self.text=self.text[:-5]
        no_space_text=self.text.split("03021")
        for var in no_space_text:
            index_number=scripted.index(var)
            text.append(self.chars[int(index_number)])
        
        self.translated_text=text





    def print_output(self):
        if self.option==1:
            for i in self.scripted:
                print(i,end="")
            print("\nnew scripts have been updated")
        elif self.option==2:
            for i in self.new_text:
                print(i.strip("\n"),end="03021")
            print("\nPlease copy your code along with the scripts!")
        elif self.option==3:
            print("The translated text is:\n")
            for i in self.translated_text:
                print(i,end="")
            print("\n")





while True:
    option=input("\nselect an option \n\n(1) To change the script \n\n(2)To convert text to special script  \n\n(3)To translate a script to text \n\n(4)To close\t")
    if option=="1":
        run=Encryption(1,"")
        run.generate()
        run.print_output()
    elif option=="2":
        text=input("Enter the text, containing normal letters, and/or (?),(,),(!)\t")
        run=Encryption(2,text)
        run.convert()
        run.print_output()
    elif option=="3":
        text=input("Enter the script you want to be translated, with spcaes as is\t")
        run=Encryption(3,text)
        run.convert_back()
        run.print_output()
    elif option=="4":
        break;
    else:
        print("Invalid input")
