import reverse
def and_gate(x,y):
    if x==y and y==1:
        return 1
    else:
        return 0

def or_gate(x,y):
    if x==0 and y==0:
        return 0
    else:
        return 1



def xor_gate(x,y):
    if x==0 and y==0 or x==1 and y==1:
        return 0
    else:
        return 1


