
def reverse(bit):
            actualBinary=[]
            actualBinaryNum=""
            
            for i in range(len(bit)-1,-1,-1):
                actualBinary.append(bit[1])
                actualBinaryNum=actualBinaryNum+str(bit[i])
               
            return actualBinaryNum
