













































































































print"""                                 WELCOME TO QUIZZARD
Developed by HARSH DALAI,ANKUSH SONI,VIVEK BADANI,ANKIT DHADSE
GENERAL INSTRUCTIONS
1.Quiz contains 10 questions.     
2.Every questions are compulsory.
3.Each question is of 4 marks and one forth marks is deducted for wrong answers.
4.You can quit any time by typing "Quit".
5.No marks is being deducted for no response
6.Minimum marks to qualify for next level is 25"""
import random
class quiz:
    def __init__(self,pt=0,ca=0,wa=0):
        print
        self.sname=raw_input("Enter your name")
        self.sclass=raw_input("Enter  your class")        
        self.pt=pt
        self.ca=ca
        self.wa=wa
        qfl=open("C:\Quiz\p1.txt",'r')
        qfl1=qfl.read()
        qfl2=qfl1.split("?")
        qfl.close()
        afl=open("C:\Quiz\p2.txt",'r')
        afl1=afl.read()
        afl2=afl1.split("?")
        afl.close()               
        for i in range(len(qfl2)):
            l=1
            dl=[]
            ob1=open(qfl2[i])
            q=ob1.read()
            que=q.split('?')
            ob1.close()
            ob=open(afl2[i])
            a=ob.read()
            an=a.split("\n")
            ob.close()
            print"""

                """
            print "Welcome to Level",i+1,"Quiz"
            print
            for i in range(len(que)-1):
                dl.append([que[i],an[i]])
            
            random.shuffle(dl)
            
            
            for i in range(10):               
                print "Question ",i+1,dl[i][0]
                while 1:
                    print
                    x=raw_input("Choose correct option:")
                    if x not in["a","b","c","d","A","B","C","D","quit","Quit"]:
                        print
                        print "Incorrect Option"
                    else:
                        break
                if x=="QUIT" or x=="quit":
                    break
                if x==dl[i][1]:
                    print
                    print 'Answer Is Correct'
                    print
                    self.pt+=4
                    self.ca+=1
                else:
                    print
                    print 'Answer is Wrong, Correct Answer is', dl[i][1]
                    print
                    self.pt-=1
                    self.wa+=1
            if self.pt>=25:                
                    print"""

                """
                    print "             Congratulations! You are qualified for the next level."
                    print
                    print"Result is:"
                    print 'Total points',self.pt
                    print 'Total Correct Answers',self.ca
                    print 'Total Wrong Answers',self.wa
                    dlf=open("C:\Quiz\Student Details.txt",'a')
                    l='Student name:'+self.sname+'\n'+'Student class:'+self.sclass+'\n'+'Total points:'+str(self.pt)+'\n'+'Total Correct Answers:'+str(self.ca)+'\n'+'Total Wrong Answers:'+str(self.wa)+'\n'+'\n'
                    dlf.write(l)
                
                
            else :
                break
            self.pt=0
            self.ca=0
            self.wa=0            
        if self.pt<25 and l<=len(qfl2):
            print"""
            You are unable to qualify for next level.
                """
            print"Result is;"
            print 'Total points',self.pt
            print 'Total Correct Answers',self.ca
            print 'Total Wrong Answers',self.wa   
            dlf=open("C:\Quiz\Student Details.txt",'a')
            l='Student name:'+self.sname+'\n'+'Student class:'+self.sclass+'\n'+'Total points:'+str(self.pt)+'\n'+'Total Correct Answers:'+str(self.ca)+'\n'+'Total Wrong Answers:'+str(self.wa)+'\n'
            dlf.write(l)
class edit:
    def __init__(self):
        print
        print """GENERAL INSTRUCTIONS
1) Please don't put question mark at the end of the question
2)Follow the given formats correctly"""
        print
        en=int(input("Enter no. of questions to enter in quiz:"))
        for i in range(en):
            eq=raw_input("Enter question to enter in quiz(Questions will be entered randomly):")
            eo=raw_input('Enter all four options(Format:a)------ b)----- c)----- d)------):')
            ea=raw_input("Enter correct option(Format: a/b/c/d):")
            print
            efq=open("C:\Quiz\Question level 1.txt",'a')
            elq=eq+"\n"+eo+"?"+"\n"
            efq.write(elq)
            efa=open("C:\Quiz\Answer level 1.txt",'a')
            ela=ea+"\n"
            efa.write(ela)
sun=raw_input("Enter username:")
spass=raw_input("Enter password:")
if sun=="admin" and spass=="aja":
    aq=raw_input("Do you want to play or edit the quiz?")
    if aq=="play":
        a=quiz()
    else:
        a=edit()
else:
    a=quiz()
    



