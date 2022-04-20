from datetime import date

present_year = date.today()
 
try:
   
    input_age_year = input("Enter your Present age/Birth year : ")
    detect_age_year = len(input_age_year)

    if input_age_year >= 'a' and input_age_year <= 'z' or  input_age_year >= 'A' and input_age_year <= 'Z':
        print("Invalid input !!!")
    
    elif(int(input_age_year) == 0):
        print("Were you born today ?")
     
    elif detect_age_year > 4 or int(input_age_year) < 0 or detect_age_year == 3:
        if detect_age_year > 4 or int(input_age_year) < 0:
            print("Are you even a human being ?")
        elif(detect_age_year == 3):
            print("You are the most oldest person in this world !!!")

    if detect_age_year == 4:
        if(int(input_age_year) < 1900):
            print("You are the most oldest person in the world !!")

    elif detect_age_year == 4 : #year
     
        if int(input_age_year) > present_year.year:
            print("You are not even born, how are you even writing this ?")
            
        elif(int(input_age_year) <= present_year.year):

            year = int(input_age_year)
            age = present_year.year - year
            if age == 100:
                print("You have it a century !!")
            elif age > 100:
                print("Your age is above 100, so our System is incapable to detect !!!")
         
            elif age < 100:
                count = 0
                for i in range(age,100):
                    count +=1             
                
                print(f"This will be the year where you will be turning 100 years of age : {present_year.year + count}")   

    elif detect_age_year == 2 or detect_age_year == 1: #age
        age = int(input_age_year)
        count = 0 
        for i in range(age,100):
            count +=1
        print(f"This will be the year where you will be turning 100 years of age : {present_year.year + count}")

    else:
        print("Please enter valid inputs !!")
except ValueError:
    print("Try to enter valid inputs !!")





