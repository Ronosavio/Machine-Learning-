import numpy as np

def gradient_decent(x, y):
    m_curr = b_curr = 0
    itirations = 10000
    n = len(x)
    learning_rate = 0.0001
    for i in range(itirations):
        Y_predicted = m_curr*x + b_curr
        #m derivative 
        md = -(2/n)*sum(x*(y-Y_predicted))
        #b derivative
        bd  = -(2/n)*sum(y-Y_predicted)
        m_curr = m_curr - md * learning_rate
        b_curr = b_curr - bd * learning_rate
        print(f"m:{m_curr},b:{b_curr}, iterations:{i}")
        
X = np.array([1,2,3,4,5])
Y = np.array([5, 7, 9, 11, 13])

gradient_decent(X, Y)