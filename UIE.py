import numpy as np
import matplotlib.pyplot as plt
import math

class NPoints:
    ''' This class is an example code of the paper
    UNIFIED INTERPOLATION AND EXTRAPOLATION FUNCTION BY DIRECT TAYLOR EXPANSION.
    This package predicts the poitns which within the given range of give data and outside the range of same data set with presize points.
    Using very small give data set in very small range this algorthm can predict the point which is extremely far away from given range.

    '''

    def __init__(self,x_domain,y_domain):
        ''' Check len of data'''
        if (len(x_domain)%2==0 and len(y_domain)%2==0 ):
            x_domain=x_domain[:-1]
            y_domain=y_domain[:-1] #drop the last element to get odd number..
            self.x_domain = x_domain  # Store x domain
            self.y_domain = y_domain  # Store y domain
            self.n = int((len(self.y_domain) - 1) / 2) #middle point index
            self.del_x = self.x_domain[1] - self.x_domain[0]
            self.taylor_coef=NPoints.taylor_coef_matrix(self)
            self.taylor_coefficent_matrix = np.matmul(np.linalg.inv(NPoints.taylor_coef_matrix(self)), self.y_domain)
        else:
            self.x_domain=x_domain # Store x domain
            self.y_domain=y_domain # Store y domain
            self.n = int((len(self.y_domain) - 1) / 2)  # middle point index
            self.del_x=self.x_domain[1]-self.x_domain[0]
            self.taylor_coef = NPoints.taylor_coef_matrix(self)
            self.taylor_coefficent_matrix=np.matmul(np.linalg.inv(NPoints.taylor_coef_matrix(self)),self.y_domain)

    @staticmethod
    def fact(num):
        ''' Static function which caluclates the factorial of feeded number'''
        factorial = 1
        if num == 0:
            return factorial
        else:
            for i in range(1, num + 1):
                factorial = factorial * i
            return factorial

    def taylor_coefficients(self,n, delta_x, m):
        coef_array = []
        for i in range(m):
            coef_array.append((n * delta_x) ** (i) / (NPoints.fact(i)))
        return coef_array

    def taylor_coef_matrix(self):
        n = int((len(self.y_domain) - 1) / 2)
        taylor_coef_matr = np.zeros((len(self.y_domain), len(self.y_domain)), dtype=float)
        mirror_array = []
        for i in range(-n, n + 1):
            mirror_array.append(i)

        for i in range(len(taylor_coef_matr)):
            taylor_coef_matr[i] =self.taylor_coefficients(mirror_array[i], self.del_x, len(mirror_array))
        return taylor_coef_matr

    def UIE_function(self,betta):
        alfa = betta - self.x_domain[self.n]
        #f_x = self.y_domain[n]
        f_x=0
        for i in range( len(self.taylor_coefficent_matrix)):
            #f_x += (((alfa ** (i)) / (NPoints.fact(i))) * (self.taylor_coefficent_matrix[i]))
            #f_x += (((alfa ** (i)) / math.factorial(i)) * (self.taylor_coefficent_matrix[i]))
            f_x += (alfa ** (i))* ((self.taylor_coefficent_matrix[i])/ math.factorial(i))
        return f_x

    def analytical_function(self):
        string ="f(x)="
        x_0=self.x_domain[self.n]
        string=string+str(self.y_domain[self.n])
        for i in range(1,len(self.taylor_coefficent_matrix)):
            string+="+(x-"+str(x_0)+")^("+str(i)+")*"+str((float(self.taylor_coefficent_matrix[i]))/(NPoints.fact(i)))


        return string




