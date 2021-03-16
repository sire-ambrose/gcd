#Run the code

'''This Function finds the gcd of two numbers and prints the steps'''
def gcd(a,b):
    r=1
    m,n=max(a,b),min(a,b)
    a,b=max(a,b),min(a,b)
    while r != 0 :
        c, r=a//b , a%b
        print(a,' = ',b, '(',c,') +', r)
        a,b=b,r
    print('gcd(',m,',',n,')=',a)
'''This Function converts the steps to a list'''
def gcd_steps(a,b): 
    alg=[]
    r=1
    m,n=max(a,b),min(a,b)
    a,b=max(a,b),min(a,b)
    while r != 0 :
        c, r=a//b , a%b
        x=str(a)+'='+str(b)+'('+str(c)+')+'+str(r)
        alg.append(x)
        a,b=b,r
    return alg
'''substitutes the step before the gcd i.e a=b(c)+d into the step of the gcd i.e b=d(e) +gcd'''
def Simplify0(f1,f2):
    a=f1[:f1.find('-')]
    b=f2[:f2.find('-')]
    a_itg=str((int(f2[f2.find('(')+1:f2.find(')')])*int(f1[f1.find('(')+1:f1.find(')')]))+1)
    b_itg=f1[f1.rfind('(')+1:f1.rfind(')')]
    comb=a+'('+a_itg+')'+'-'+b+'('+b_itg+')'
    return comb

'''simplifies bracket subsequent substitutions that are toward the left i.e (a+b(c))(g)+h'''
def simplify1(f1,f2):
    f1_itg=f1[f1.find('(')+1:f1.find(')')]
    f1_itg_b=f1[f1.rfind('(')+1:f1.rfind(')')]
    f2_itg=f2[f2.find('(')+1:f2.find(')')]
    a1=f2[:f2.find('-')]
    b1=f1[1+f1.find('-'):f1.rfind('(')]
    b1_itg=str(int(f1_itg)*int(f2_itg)+int(f1_itg_b))
    comb=a1+'('+f1_itg+')'+'-'+b1+'('+b1_itg+')'
    return comb
    
'''simplifies bracket subsequent substitutions that are toward the right i.e h + (a+b(c))(g)'''
def simplify2(f1,f2):
    f1_itg=f1[f1.find('(')+1:f1.find(')')]
    f1_itg_b=f1[f1.rfind('(')+1:f1.rfind(')')]
    f2_itg=f2[f2.find('(')+1:f2.find(')')]
    a1=f1[:f1.find('(')]
    b1=f2[:f2.find('-')]
    a1_itg=str(int(f1_itg_b)*int(f2_itg)+int(f1_itg))
    comb=a1+'('+a1_itg+')'+'-'+b1+'('+f1_itg_b+')'
    return comb


'''Makes the remainder in each step the subject of formulae and retuns it as a list'''
def Remainder(steps):
    r_list=[]
    gcd=steps[-2][steps[-2].find('+')+1:]
    for i in range(-2,-len(steps)-1,-1):
        i_step=steps[i]
        a=i_step[:i_step.find('=')]
        b=i_step[i_step.find('=')+1:i_step.find('(')]
        itg=i_step[i_step.find('(')+1:i_step.find(')')]
        r=i_step[i_step.find('+')+1:]
        val=a+'-'+'('+itg+')'+b
        r_list.append(val)
    return r_list, gcd



def linear_comb():
    x=eval(input('Enter first number : '))
    y=eval(input('Enter second number : '))
    steps=gcd_steps(x,y)
    r_list,a=Remainder(steps)
    comb=Simplify0(r_list[0], r_list[1])
    
    try:
        for i in range(2,len(r_list),2):
            comb=simplify1(comb, r_list[i])
            comb=simplify2(comb, r_list[i+1])
    except:
        pass
    gcd(x,y)
    print(a,'=',comb)

linear_comb()
#Run the code
