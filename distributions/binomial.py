# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 11:39:52 2016

@author: Nikhil
"""
import matplotlib.pyplot as plt
from math import factorial

def ncr(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)

def binomial(n, p):
    px = []
    for i in xrange(n+1):
        px.append(ncr(n,i) * p ** i * (1-p)**(n-i))
    
    return px

def graph(x, y):
    plt.bar(x, y)
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Binomial Distribution')
    plt.show()

def run(N, p):
    x = list(range(0, N+1))
    y = binomial(N, p)
    graph(x, y)

def main():
    N = 10
    p = 0.8
    run(N, p)

if __name__ == '__main__':
    main()