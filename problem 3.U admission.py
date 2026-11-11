#Problem 3

print ("This program checks your eligibility, Please Enter your Correct Scores: \n")

math = float(input("Mathematics: "))
eng = float(input("English: "))
sci = float(input("Science: ")) 
interv = float(input ("Interview: "))

if math < 0 or math > 100 or eng < 0 or eng > 100 or sci < 0 or sci > 100 or interv  < 0 or interv > 100:
    print ("\nInvalid Score.")
else:
    
    total = math + eng +sci + interv

    total_ava = math + eng + sci

    ava = total_ava / 3
    
    if math < 60:
        print ("\nAdmission Rejected!, Your Mathematics Score is less than 60.")
    else:
        if eng <50:
            print ("\nAdmission Rejected!, Your English Score is less than 50.")
        else:
            if sci <55:
                print ("\nAdmission Rejected!, Your Science Score is less than 55.")
            else:
                if interv < 70:
                    print ("\nAdmission Rejected!, Your Interview Score is less than 70.")
                else:
                    if ava < 65:
                        print ("\nAdmission Rejected!, Your Avarage Score is less than 65.")
                    else:
                        print (f"\nAverage: {ava}.")
                        print ("Admission Approved! ")
                        
                        
