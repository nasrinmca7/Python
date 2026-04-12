class multipleFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        arrList = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        for item in arrList:
            print(item)

    def OddEven():
        num = int(input("Enter a number"))
        if(num % 2 == 0):
           print(num, "is Even number")
        else:
           print(num, "is Odd number")

    def Elegible():
        gender = input("Enter Gender")
        age = int(input("Enter Age"))
        
        print("Your Gender:", gender)
        print("Your Age:", age)
       
        if((gender.lower() == "female") and (age>=18)):
            print("ELIGIBLE")
        elif((gender.lower() == "male") and (age>=21)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        Sub1 = int(input("Enter Subject 1 Marks:"))
        Sub2 = int(input("Enter Subject 2 Marks:"))
        Sub3 = int(input("Enter Subject 3 Marks:"))
        Sub4 = int(input("Enter Subject 4 Marks:"))
        Sub5 = int(input("Enter Subject 5 Marks:"))

        obtained = Sub1+Sub2+Sub3+Sub4+Sub5
        total = 500
        percentage = (obtained/total)*100
        
        print("Subject1=", Sub1)
        print("Subject2=", Sub2)
        print("Subject3=", Sub3)
        print("Subject4=", Sub4)
        print("Subject5=", Sub5)
        print("Total:", obtained)
        print("Percentage:", percentage)

    def area():
        height = 32
        breadth = 34
        areaOfTriangle = (height*breadth)/2
        return areaOfTriangle
        
    def perimeter():
        height1 = 2
        height2 = 4
        breadth = 4
        perimeterOfTriangle = height1+height2+breadth
        return perimeterOfTriangle