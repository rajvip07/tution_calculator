print("2021 Undergraduate Tuition Calculator.\n")


while True:
    jamesMad = '0'
    
    #inputs level
    level = input("Enter Level as freshman, sophomore, junior, senior: ")
    level = level.lower()
    
    #prints the error message if not the input is not desired
    while not (level == 'freshman' or level == 'sophomore' or \
               level == 'junior' or level == 'senior'):
        print("Invalid input. Try again.")
        level = input("Enter Level as freshman, sophomore, junior, senior: ")
        level = level.lower() 
        break
        continue
    
    #inputs college
    if level == 'junior' or level == 'senior':
        college = input("Enter college as business, engineering, health, sciences, or none: ")
        college = college.lower()   
        
        if not (college == 'business' or college == 'engineering' or \
                college == 'health' or college == 'sciences'):
            jamesMad = input("Are you in the James Madison College (yes/no): ")
            jamesMad = jamesMad.lower() 
          
    #iput if college of engineering or not 
    elif level == 'freshman' or level == 'sophomore':
        coe = input("Are you admitted to the College of Engineering (yes/no): ")
        coe = coe.lower()
        
        if coe != 'yes': 
            jamesMad = input("Are you in the James Madison College (yes/no): ")
            jamesMad = jamesMad.lower()
    
    #asks the user to input only an integer for credits, if not an integer \
        # an error is printed and asks for credits again
    while True:
        credit = input("Credits: ")
        credit = credit.lower()
        if credit == '0' or not credit.isdigit():
            print("Invalid input. Try again.")
        else:
            break
    #converts the str credits to integer 
    credit = int(credit)
        
    
    #per credit variables 
    freshmanPc = 482
    sophomorePc = 494
    juniorPc = 555
    juniorPcBe = 573 #percredit cost of junior in business and engineering clg
    seniorPc = 555 
    seniorPcBe = 573 #percredit cost of senior in business and engineering clg
    
    #taxes variables 
    asmsu = 21
    fmradio = 3
    statenews = 5
    
    #taxes added to the tuition 
    if credit >= 6:
        tuition = asmsu + fmradio + statenews
    else: 
        tuition = asmsu + fmradio 
    
    #calculates the tuition for all levels if credit is between 1-11
    if 1 <= credit <= 11: 
        if level == 'freshman':
            if credit <= 4 and coe == 'yes':
                tuition = tuition + freshmanPc + 402
                print("Tuition is ${:,.2f}.". format(tuition))
            if credit > 4 and coe == 'yes':
                tuition = tuition + freshmanPc + 670
                print("Tuition is ${:,.2f}.". format(tuition))
        elif level == 'sophomore':
            if credit <= 4 and coe == 'yes':
                tuition = tuition + sophomorePc + 402
                print("Tuition is ${:,.2f}.". format(tuition))
            if credit > 4 and coe == 'yes':
                tuition = tuition + sophomorePc + 670
                print("Tuition is ${:,.2f}.". format(tuition))
                
        elif level == 'junior':
            if not (college == 'business' or college == 'engineering'):
                if credit <= 4 and college == 'health':
                    tuition = tuition + juniorPc + 50
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif credit > 4 and college == 'health':
                    tuition = tuition + juniorPc + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
                if credit <= 4 and college == 'sciences':
                    tuition = tuition + juniorPc + 50
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif credit > 4 and college == 'sciences':
                    tuition = tuition + juniorPc + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
            else:
                if credit <= 4 and college == 'business':
                    tuition = juniorPcBe + 133
                    print("Tuition is ${:,.2f}.". format(tuition))
                if credit > 4 and college == 'business':
                   tuition = juniorPcBe + 226
                   print("Tuition is ${:,.2f}.". format(tuition))
            if college == 'engineering':
                tution = tuition + (juniorPcBe * credit) + 670
                print("Tuition is ${:,.2f}.". format(tuition))
            if jamesMad == 'yes':
                tuition =  (juniorPc * credit) + tuition + 7.50
                print("Tuition is ${:,.2f}.". format(tuition))
    
        elif level == 'senior':
            if not (college == 'business' or college == 'engineering'):
                if credit <= 4 and college == 'health':
                    tuition = tuition + seniorPc + 50
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif credit > 4 and college == 'health':
                    tuition = tuition + seniorPc + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
                if credit <= 4 and college == 'sciences':
                    tuition = seniorPc + 50
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif credit > 4 and college == 'sciences':
                    tuition = tuition + seniorPc + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
            else:
                if credit <= 4 and college == 'business':
                    tuition = tuition + seniorPcBe + 133
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif credit > 4 and college == 'business':
                    tuition = tuition + seniorPcBe + 226
                    print("Tuition is ${:,.2f}.". format(tuition))
            if college == 'engineering':
                tuition = tuition + (seniorPcBe * credit) + 670
                print("Tuition is ${:,.2f}.". format(tuition))
            if jamesMad == 'yes':
                tuition =  (seniorPc * credit) + tuition + 7.50
                print("Tuition is ${:,.2f}.". format(tuition))
    
    #flat rate variables
    freshmanFr = 7230
    sophomoreFr = 7410
    juniorFr = 8325
    juniorFrBe = 8595 #flat rate for junior in business and engineering clg
    seniorFr = 8325
    seniorFrBe = 8595 #flat rate for senior in business and engineering clg
    
    #calculates the tuition for all levels with credits between 12-18
    if 12 <= credit <= 18: 
        if level == 'freshman':
            if coe == 'yes':
                tuition = tuition + freshmanPc + 670
                print("Tuition is ${:,.2f}.". format(tuition))
            else:
                tuition = tuition + freshmanFr
                print("Tuition is ${:,.2f}.". format(tuition))
        elif level == 'sophomore':
            if coe == 'yes':
                tuition = tuition + sophomorePc + 670
                print("Tuition is ${:,.2f}". format(tuition))
            else:
                tuition = tuition + sophomorePc
                print("Tuition is ${:,.2f}.". format(tuition))
        elif level == 'junior':
            if not (college == 'business' or college == 'engineering'):
                if college == 'health':
                    tuition = tuition + juniorFr + 100
                    print("Tuition is ${:,.2f}". format(tuition))
                elif college == 'sciences':
                    tuition = tuition + juniorFr + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
            else:
                if college == 'business':
                    tuition = tuition + juniorFrBe + 226
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif college == 'engineering':
                    tuition = tuition + juniorFrBe
                    print("Tuition is ${:,.2f}.". format(tuition))
        elif level == 'senior':
            if not (college == 'business' or college == 'engineering'):
                if college == 'health':
                    tuition = tuition + seniorFr + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif college == 'sciences':
                    tuition = tuition + seniorFr + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
            else:
                if college == 'business':
                    tuition = tuition + seniorFrBe + 226
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif college == 'engineering':
                    tuition = tuition + seniorFrBe + 670
                    print("Tuition is ${:,.2f}.". format(tuition))

    #calculates tuition for all levels with credits more than 18
    if credit > 18:
        if level == 'freshman':
            if coe == 'yes':
                tuition = tuition + freshmanFr + \
                    ((credit - 18) * freshmanPc) + 670
                print("Tuition is ${:,.2f}.". format(tuition))
            else:
                tuition = tuition + freshmanFr + ((credit - 18) * freshmanPc)
                print("Tuition is ${:,.2f}.". format(tuition))
        elif level == 'sophomore':
            if coe == 'yes':
                tuition = tuition + sophomoreFr + \
                    ((credit - 18) * sophomorePc) + 670
                print("Tuition is ${:,.2f}.". format(tuition))
            else:
                tuition = tuition + sophomoreFr + ((credit - 18) * sophomorePc)
                print("Tuition is ${:,.2f}.". format(tuition))
        elif level == 'junior':
            if not (college == 'business' or college == 'engineering'):
                if college == 'health':
                    tuition = tuition + juniorFr + \
                        ((credit - 18) * juniorPc) + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif college == 'sciences':
                    tuition = tuition + juniorFr + \
                        ((credit - 18) * juniorPc) + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
            else:
                if college == 'business':
                    tuition = tuition + juniorFrBe + \
                        ((credit - 18) * juniorPcBe) + 226
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif college == 'engineering':
                    tution = tuition = tuition + juniorFrBe + \
                        ((credit - 18) * juniorPcBe)
                    print("Tuition is ${:,.2f}.". format(tuition))
                                                              
        elif level == 'senior':
             if not (college == 'business' or college == 'engineering'):
                if college == 'health':
                    tuition = tuition + seniorFr + \
                        ((credit - 18) * seniorPc) + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif college == 'sciences':
                    tuition = tuition + seniorFr + \
                        ((credit - 18) * seniorPc) + 100
                    print("Tuition is ${:,.2f}.". format(tuition))
             else:
                if college == 'business':
                    tuition = tuition + seniorFrBe + \
                        ((credit - 18) * seniorPcBe) + 226
                    print("Tuition is ${:,.2f}.". format(tuition))
                elif college == 'engineering':
                    tution = tuition + seniorFrBe + \
                        ((credit - 18) * seniorPcBe) + 670
                    print("Tuition is ${:,.2f}.". format(tuition))
                    
    askuser = input("Do you want to do another calculation (yes/no): ")
    if askuser == 'no':
        break
