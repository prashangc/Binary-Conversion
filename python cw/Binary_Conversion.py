def conversion(Input1):
            bit=[]
            
            counter1=0
            while counter1!=8:
                remainder=Input1%2
                bit.append(remainder)
                Input1=Input1//2
                counter1+=1
            return bit

