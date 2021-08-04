import greeting
import Binary_Conversion
import reverse
import bit_adder


greeting.Greeting()

continueLoop=True
while continueLoop==True:
            continueNumber1=False
            while continueNumber1==False:
                        try:
                                    Input1=int(input("Enter the first decimal number: "))
                                    if(Input1<0 or Input1>255):
                                        print("Invalid!!! Please enter the number between 0 to 255.")
                                        continue
                                    else:
                                        continueNumber1=True
                        except:
                                    print("\n")
                                    print("Please enter valid number.")

            continueNumber2=False
            while continueNumber2==False:
                        try:
                                    Input2=int(input("Enter the second decimal number: "))
                                    if(Input2<0 or Input2>255):
                                        print("Invalid!!! Please enter the number between 0 to 255.")
                                        continue
                                    else:
                                        continueNumber2=True
                        except:
                                    print("\n")
                                    print("Please enter valid number.")

            conversion1=Binary_Conversion.conversion(Input1)
            conversion2=Binary_Conversion.conversion(Input2)

            binaryNumber1=reverse.reverse(conversion1)
            binaryNumber2=reverse.reverse(conversion2)
            
            binary_addition=bit_adder.binary_addition(binaryNumber1,binaryNumber2)

            print("\n")
            #print ("Binary conversion of",Input1,"is",binaryNumber1)
            #print("\n")
            #print ("Binary conversion of",Input2,"is",binaryNumber2)
            #print("\n")
            
            print("Binary addition of",Input1,"and",Input2,"is: ",binary_addition)
            print("\n")
            continuous=input("Do you wish to continue? Type 'No' to exit: ").lower()
            if continuous=="no":
                        break


print("\n")
greeting.GreetingAtEnd()

            
            

