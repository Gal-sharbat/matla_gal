def power(x,k):
    result=1.0
    for i in range(int(k)):
        result=result*x
    return result

def azeret(k):
    result1=1.0
    for i in range(1, int(k)+1):
        result1=result1*i
    return result1

def exponent(marih):
    result2=0.0
    for i in range (0,100):
        result2=result2+(power(marih,i))/(azeret(i))
    return result2

def Ln(x):
    try:
        if (x<=0):
            return (0.0)
        else:
            yn=0
            result3=x-1.0
            while ((yn-result3)>0.001 or (result3-yn)>0.001):
                yn=result3
                result3=result3+2*((x-exponent(result3))/(x+exponent(result3)))
            return result3
    except:
        return(0.0)
    
def XtimesY(x:float,y:float) -> float:
    try:
        if(x<=0):
            return (0.0)
        else:
           b=exponent(Ln(x)*y)
           return float('%0.6f' %b)
    except:
        return(0.0)

def sqrt(x:float,y:float) -> float:
    try:
        if(y<=0):
            return (0.0)
        elif (y>0 and x!=0):
            x=1/x
            b=(XtimesY(y,x))
            return float('%0.6f' %b)
        else:
            return(0.0)
    except:
        return (0.0)
        
def calculate(x):
    try:
        if(x<=0):
            return(0.0)
        result4=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
        b=float('%0.6f' %result4)
        return b
    except:
        return (0.0)
    
#try:
    #number1=input ('enter a num1: ')
    #number2=input ('enter a num2: ')
    #x=float(number1)
    #y=float(number2)
    #print(calculate(x))
    #print(XtimesY(x,y))
    #print(sqrt(x,y))
#except:
  #  print(0.0)