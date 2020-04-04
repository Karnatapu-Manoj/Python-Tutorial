print("\n\n\t~~~~~~~~~~~~~~Welcome to Student Marks Registration Portal~~~~~~~~~~~~~~")
print("\n\n \t\t\tEnter the Student Details\n")



a = str(input("Enter student Name : ")) ; print("\n")
b = str(input("Enter Student's Father Name : ")) ; print("\n")
c = int(input("Enter the D.O.B : ")); print("\n")
d = input("Do u want to do calculation for student {} (Y/N): ".format(a))
if d == 'Y' or 'y':
    #print("\nWelcome to student marks registration Portal")
    print("\n")
    s1 = int(input("Enter marks for Telugu : "))
    s2 = int(input("Enter marks for hindi : "))
    s3 = int(input("Enter marks for English : "))
    s4 = int(input("Enter marks for Maths : "))
    s5 = int(input("Enter marks for Science : "))
    s6 = int(input("Enter marks for Social : "))
    
    if s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100 and s6<=100 :
        if s1>=0 and s2>=0 and s3>=0 and s4>=0 and s5>=0 and s6>=0 :
            
            total = s1+s2+s3+s4+s5+s6
            
            avg = total/6
            
            percentage = (total/600)*100
        
            print("\n=========The Progess Report of Student '{}'========".format(a))
            print("\nThe Student Name is :",a);print("\nThe Student's father Name is :",b)
            print("\nThe student's D.O.B is :",c)
            print("\n=========The Overall Status of Student '{}'========".format(a))
            print("\n The Total Marks Obtained for student Named {} is : ".format(a),total)
            print("\n The Aaverage score Obtained for Student Named {} is : ".format(a),avg)
            print("\n The Percentage of Student Named {} is : ".format(a),percentage)
            if percentage>=90 and percentage<=100:
                    print("\n Students Grade is : A+ Grade\n")
            elif percentage>=80 and percentage<90:
                    print("\n Students Grade is : A Grade\n")
            elif percentage>=70 and percentage<80:
                    print("\n Students Grade is : B Grade\n")
            elif percentage>=60 and percentage<70:
                print("\n Students Grade is : C Grade\n")
            elif percentage>=50 and percentage<60:
                    print("\n Students Grade is : D Grade\n")
            elif percentage>=40 and percentage<50:
                print("\n Students Grade is : E Grade\n")
            else:
                print("\nThe student is failed In the Graduation\n")
        else:
            print("You have Entered the -ve Marks, Plz do Check once")
    else:
        print("Please do enter marks below 100")
    
else:
    print("Thank Q visit again")    





