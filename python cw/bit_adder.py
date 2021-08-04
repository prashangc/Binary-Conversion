import reverse
import gates as g

def binary_addition(num1,num2):
    cin=0
    List=[]
    for i in range (len(num1)-1, -1, -1):
        a=int(num1[i])
        b=int(num2[i])
        #for sum value
        fs =g.xor_gate(a,b)
        sum_val=g.xor_gate(fs,cin)

        #for carry over

        fco=g.and_gate(a,b)
        fco2=g.and_gate(fs,cin)
        co=g.or_gate(fco,fco2)
        cin = co
        List.append(sum_val)
    List2=reverse.reverse(List)
    return List2
            
