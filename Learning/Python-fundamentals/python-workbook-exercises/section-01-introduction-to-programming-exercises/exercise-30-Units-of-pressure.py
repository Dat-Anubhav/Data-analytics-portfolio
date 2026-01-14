'''Q30:- In this exercise you will create a program that reads a pressure from the user in kilopascals. 
Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.'''

p=float(input("\nEnter the pressure in Kilopascals :- \n"))

n=int(input("\n You have entered the pressure in kilo pascals \
\n Press 1 to convert this into equivalent pounds per square inch \
\n Press 2 to convert this into equivalent milimeters of mercury \
\n Press 3 to convert this into equivalent standard atmospheric :-\n "))

if(n==1):
    
    # 1 psi(pounds per square inches) = 6894.76 pascals ; 1 kilo pascals = 1000/6894.76 = 0.145038 psi 
    P=p*0.145038
    print(f"\n{p} kilo pascals pressure when converted to equivalent pounds per square inches(psi) will be = {P} psi\n")

elif(n==2):
    
    # 1 milimeters per square inches(mmhg) = 133.322 Pascals ; 1 kilo pascals = 1000/133.322 = 7.5006 mmhg
    P=p*7.5006
    print(f"\n{p} kilo pascals pressure when converted to equivalent milimeters of mercury (mmhg) will be = {P} mmhg\n")

elif(n==3):
    
    #1 atm(atmospheric) = 101,325 pascals ; 1 kilo pascals = 1000/101,325 = 0.00986923 atm
    P=p*0.00986923
    print(f"\n{p} kilo pascals pressure when converted to equivalent standard atmospheric (atm) will be = {P} atm\n")

else:
    print("\nINVALID INPUT\n") 