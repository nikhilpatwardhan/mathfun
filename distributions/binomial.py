# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 11:39:52 2016

@author: Nikhil
"""
import timeit
import matplotlib.pyplot as plt
from math import factorial

fact_n = 0

def ncr(n, r):
    global fact_n
    if not fact_n:
        fact_n = factorial(n)
    return fact_n / factorial(r) / factorial(n-r)

def binomial(n, p):
    for i in xrange(n+1):
        yield (ncr(n,i) * p ** i * (1-p)**(n-i))

def graph(x, y):
    plt.bar(x, y)
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Binomial Distribution')
    plt.show()

def run(N, p):
    x = list(range(0, N+1))
    y = list(binomial(N, p))
    # graph(x, y)

def main():
    timing_x = range(10,90,5)
    timing_y = []
    for i in timing_x:
        timing_y.append(timeit.timeit('run(%d, 0.8)' % i, setup='from __main__ import run', number=10000))
    
    plt.plot(timing_x, timing_y)
    plt.xlabel('N')
    plt.ylabel('Runtime')
    plt.title('Runtimes for increasing N')
    plt.show()

if __name__ == '__main__':
    main()