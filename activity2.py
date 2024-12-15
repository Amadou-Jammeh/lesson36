height=int(input("enter your height"))
weight=int(input("enter your weight"))
bmi=weight/(height/100)**2
if bmi<=18.4:
    print("you are underweight",bmi)
elif bmi<=24.9:
    print("you are healthy",bmi)
elif bmi<=29.9:
    print("you are overweight",bmi) 
elif bmi<=34.9:
    print("you are severely overweight",bmi) 
elif bmi<=39.9:
    print("you are obase",bmi)   
else:
    print("you are severely obase",bmi)           