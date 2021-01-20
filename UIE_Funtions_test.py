import numpy as np
import math
import matplotlib.pyplot as plt
from basic_units import radians

plt.style.use('seaborn-whitegrid')

def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)

from UIE import NPoints


def linear(x,a):
    return a*x

#Cubic function
def cubic(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

#Quadratic function
def quadratic(x,a,b,c,d,f):
    return a*x**4+b*x**3+c*x**2+d*x+f

#Sin function
def sinus(x):
    return math.sin(x)

#Tangent function
def tangent(x):
    return math.tan(x)


''' Test for tan'''
def tan_test_pi():
    #Give set
    x_domain=np.linspace(-math.pi,math.pi,30)
    y_domain=[]
    for i in x_domain:
        y_domain.append(tangent(i))

    #set to predict
    x_domain_predict=np.linspace(-math.pi,math.pi,50)
    y_domain_anal=[]

    for i in x_domain_predict:
        y_domain_anal.append(tangent(i))

    UIE=NPoints(x_domain,y_domain)

    y_domain_UIE=UIE.UIE_function(x_domain_predict)

    test_int=math.pi/2
    n=UIE.UIE_function(test_int)
    a=tangent(test_int)
    print("a=",a,"\nn=",n,"\nError=a-n=",a-n)
    print(UIE.taylor_coefficent_matrix)
    print(UIE.analytical_function())


    plt.scatter(x_domain_predict,y_domain_anal, color='green', linewidth=3)
    # predicted value plot and scatter
    #plt.plot(x_domain_predict[8:-9],y_domain_UIE[8:-9], color='red', alpha=0.5, linewidth=5)
    plt.scatter(x_domain_predict[8:-9],y_domain_UIE[8:-9], color='red', alpha=0.7, linewidth=6)
    plt.scatter(x_domain, y_domain, color='blue', linewidth=3)
    plt.show()

def tan_test_pi_2():
    #Give set
    x_domain=np.linspace(-math.pi/2,math.pi/2,30)
    y_domain=[]
    x_domain=x_domain[1:-1]
    for i in x_domain:
        y_domain.append(tangent(i))

    #set to predict
    x_domain_predict=np.linspace(-math.pi/2,math.pi/2,50)
    y_domain_anal=[]
    x_domain_predict=x_domain_predict[1:-1]
    for i in x_domain_predict:
        y_domain_anal.append(tangent(i))

    UIE=NPoints(x_domain,y_domain)
    y_domain_UIE=UIE.UIE_function(x_domain_predict)

    #test_int=5*math.pi
    #n=UIE.UIE_function(test_int)
    #a=tangent(test_int)
    #print("a=",a,"\nn=",n,"\nError=a-n=",a-n)
    print(UIE.taylor_coefficent_matrix)
    print(UIE.analytical_function())

    plt.scatter(x_domain_predict,y_domain_anal)
    plt.scatter(x_domain_predict,y_domain_UIE)
    plt.scatter(x_domain, y_domain)
    plt.show()




''' Test for sin'''
def sin_test():
    #Give set
    x_domain=np.linspace(-math.pi,math.pi,5)
    y_domain=[]
    for i in x_domain:
        y_domain.append(sinus(i))

    #set to predict
    x_domain_predict=np.arange(-5*math.pi/4,5*math.pi/4,math.pi/8)
    y_domain_anal=[]

    for i in x_domain_predict:
        y_domain_anal.append(sinus(i))

    UIE=NPoints(x_domain,y_domain)
    y_domain_UIE=UIE.UIE_function(x_domain_predict)

    test_int=5*math.pi
    n=UIE.UIE_function(test_int)
    a=sinus(test_int)
    print("a=",a,"\nn=",n,"\nError=a-n=",a-n)
    print(UIE.taylor_coefficent_matrix)
    print(UIE.analytical_function())

    plt.title(" [x vs. y=sin(x)] Graph for Extrapolation Experiment")
    plt.xlabel("x domain [Radian's]")
    plt.ylabel('y=f(x) domain')

    plt.xticks(x_domain_predict,
               [
                 "","", "$\pi$", "","" 
                "","",
                "$-\pi / 2$", "", "","", "0",  "", "", "",
                "$ \pi / 2 $",
                "", "", "", "$\pi$", "", ""])

    #plt.plot(x_domain, y_domain,color='dodgerblue')


    plt.scatter(x_domain_predict, y_domain_anal, color='darkorange',marker='s',label='Test Data')
    plt.plot(x_domain_predict, y_domain_anal, color='darkorange')

    plt.scatter(x_domain_predict, y_domain_UIE, color='limegreen',marker='^',label='Proposed Model Data')
    plt.plot(x_domain_predict, y_domain_UIE, color='limegreen')
    plt.scatter(x_domain, y_domain, color='dodgerblue',  marker='o', label='Feed Data')

    plt.savefig('sin_extrapolation_test_5points.png')
    plt.show()

def sin_test_intra():
    #Give set
    x_domain=np.linspace(-math.pi,math.pi,5)
    print(x_domain[1]-x_domain[0])
    y_domain=[]
    for i in x_domain:
        y_domain.append(sinus(i))

    #set to predict
    x_domain_predict=np.linspace(-math.pi,math.pi,20)
    y_domain_anal=[]

    for i in x_domain_predict:
        y_domain_anal.append(sinus(i))

    UIE=NPoints(x_domain,y_domain)
    y_domain_UIE=UIE.UIE_function(x_domain_predict)

    test_int=2*math.pi/3
    n=UIE.UIE_function(test_int)
    a=sinus(test_int)
    print("a=",a,"\nn=",n,"\nError=a-n=",a-n)
    print(UIE.taylor_coefficent_matrix)
    print(UIE.analytical_function())

    plt.title(" [x vs. y=sin(x)] Graph for Interpolation  Experiment")
    plt.xlabel("x domain [Radian's]")
    plt.ylabel('y=f(x) domain')

    plt.xticks(x_domain_predict,["-$\pi$","","","","","$-\pi / 2$","","","","0","","","","","$ \pi / 2 $","","","","","$\pi$"])

    plt.title(" [x vs. y=sin(x)] Graph for Interpolation  Experiment")
    plt.xlabel("x domain [Radian's]")
    plt.ylabel('y=f(x) domain')

    #plt.plot(x_domain, y_domain,color='dodgerblue')


    plt.scatter(x_domain_predict, y_domain_anal, color='darkorange',marker='s',label='Test Data')
    plt.plot(x_domain_predict, y_domain_anal, color='darkorange')

    plt.scatter(x_domain_predict, y_domain_UIE, color='limegreen', marker='^',label='Proposed Model Data')
    plt.plot(x_domain_predict, y_domain_UIE, color='limegreen')

    plt.scatter(x_domain, y_domain, color='dodgerblue', marker='o', label='Feed Data')
    plt.legend()

    plt.savefig('sin_interpolation_5points.png')
    plt.show()

''' Test for linear'''
def linear_test():
    #Give set
    x_domain=np.linspace(0,1,5)
    y_domain=linear(x_domain,3)

    #set to predict
    x_domain_predict=np.linspace(-3,3,10)
    y_domain_anal=linear(x_domain_predict,3)

    UIE=NPoints(x_domain,y_domain)
    y_domain_UIE=UIE.UIE_function(x_domain_predict)

    test_int = 100000
    n = UIE.UIE_function(test_int)
    a = linear(test_int, 3)

    print("a=", a, "\nn=", n, "\nError=a-n=", a - n)

    print(UIE.taylor_coefficent_matrix)
    print(UIE.analytical_function())

    plt.plot(x_domain,y_domain)
    plt.scatter(x_domain, y_domain)

    plt.scatter(x_domain_predict,y_domain_anal)
    plt.plot(x_domain_predict,y_domain_anal)

    plt.scatter(x_domain_predict,y_domain_UIE)
    plt.show()

''' Test for quadratic'''
def quadratic_test():
    #Give set
    x_domain=np.linspace(3,4,5)
    y_domain=quadratic(x_domain,5,3,1,4,2)

    print(x_domain)
    print(y_domain)

    #set to predict
    x_domain_predict=np.linspace(-5,5,13)
    y_domain_anal=quadratic(x_domain_predict,5,3,1,4,2)

    UIE=NPoints(x_domain,y_domain)
    y_domain_UIE=UIE.UIE_function(x_domain_predict)

    print(UIE.taylor_coef)
    print(UIE.taylor_coefficent_matrix)

    test_int=999
    n=UIE.UIE_function(test_int)
    a=quadratic(test_int, 5,3,1,4,2)

    print("a=",a,"\nn=",n,"\nError=a-n=",a-n)
    print(UIE.taylor_coefficent_matrix)
    print(UIE.analytical_function())

    plt.title(" [x vs. y=f(x)] Graph for Extrapolation Experiment")
    plt.xlabel("x domain")
    plt.ylabel('y=f(x) domain')

    plt.plot(x_domain, y_domain, color='dodgerblue')

    plt.scatter(x_domain_predict, y_domain_anal, color='darkorange', marker='s', label='Test Data')
    plt.plot(x_domain_predict, y_domain_anal, color='darkorange')

    plt.scatter(x_domain_predict, y_domain_UIE, color='limegreen', marker='^', label='Proposed Model Data')

    plt.scatter(x_domain, y_domain, color='dodgerblue', marker='o', label='Feed Data')

    plt.legend()
    #plt.savefig('quadratic_test.png')
    plt.show()


''' Test for cubic'''
def cubic_test():
    #Give set
    x_domain=np.linspace(-3,-2,5)
    y_domain=cubic(x_domain,3, 2, 1, 4)


    print(x_domain)
    print(y_domain)

    #set to predict
    x_domain_predict=np.linspace(-5,5,13)
    y_domain_anal=cubic(x_domain_predict,3, 2, 1, 4)

    UIE=NPoints(x_domain,y_domain)

    y_domain_UIE=UIE.UIE_function(x_domain_predict)

    print(UIE.taylor_coef)
    print(UIE.taylor_coefficent_matrix)


    test_int=999
    n=UIE.UIE_function(test_int)
    a=cubic(test_int, 3, 2, 1, 4)
    print("a=",a,"\nn=",n,"\nError=a-n=",a-n)
    print(UIE.taylor_coefficent_matrix)
    print(UIE.analytical_function())

    plt.title(" [x vs. y=f(x)] Graph for Extrapolation Experiment")
    plt.xlabel("x domain")
    plt.ylabel('y=f(x) domain')

    plt.plot(x_domain, y_domain, color='dodgerblue')

    plt.scatter(x_domain_predict, y_domain_anal, color='darkorange',marker='s',label='Test Data')
    plt.plot(x_domain_predict, y_domain_anal, color='darkorange')

    plt.scatter(x_domain_predict, y_domain_UIE, color='limegreen', marker='^',label='Proposed Model Data')

    plt.scatter(x_domain, y_domain, color='dodgerblue', marker='o', label='Feed Data')

    plt.legend()
    #plt.savefig('cubic_test.png')
    plt.show()

sin_test_intra()


'''TEST 
#x_domain=np.linspace(0,0.01,5)
x_domain=np.linspace(-math.pi,math.pi,11)
del_x=x_domain[1]-x_domain[0]
#print(x_domain)

def f(x):
    #return 10*x**3+5*x**2+6*x
    return math.sin(x)

y_domain=[]
for i in x_domain:
    y_domain.append(f(i))

test=NPoints(x_domain,y_domain)


taylor_x=np.linspace(-2*math.pi,2*math.pi,100)

anal_y=[]
for i in taylor_x:
    anal_y.append(f(i))

UIE_y=test.UIE_function(taylor_x)


plt.plot(taylor_x,anal_y)
plt.plot(taylor_x,UIE_y)
plt.show()
'''