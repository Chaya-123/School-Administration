import csv
def writetocsv(stud_info):
    with open("filehandler1.csv","a",newline="") as f:
        writer=csv.writer(f)
        if f.tell()==0:
            writer.writerow(["usn","name","age","phone_no","email-id","address"])
            
        
        writer.writerow(stud_info)
if __name__=="__main__":
    count=True
    student_no=1
    while count:
        student_info=input("enter student details for student {} in the given format(usn name age contact_no e-mail_id address)".format(student_no))
        student_details=student_info.split()
        print("\nthe entered details are-\n usn:{}\n name:{}\n age:{}\n contact_no:{}\n e_mail_id:{}\n address:{}\n"
          .format(student_details[0],student_details[1],student_details[2],student_details[3],student_details[4],student_details[5]))
        choice=input("Is the entered info correct(yes/no)")
        if choice=="yes":
            writetocsv(student_details)
            
    
    
            counter_condition=input("enter yes or no to enter another student details")
            if counter_condition=="yes":
                count=True
                student_no=student_no+1
            elif counter_condition=='no':
                count=False
        elif choice=="no":
            print("\nplease re-enter the values")
