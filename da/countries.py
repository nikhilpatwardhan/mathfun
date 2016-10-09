# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 12:42:43 2016

Ref:
http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html
http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt

@author: Nikhil
"""

from numpy import genfromtxt
import matplotlib.pyplot as plt

def read():
    return genfromtxt('countries.csv', delimiter=',', skip_header=1, filling_values=0.0, usecols=(1,2), unpack=True)

def graph(y):
    plt.bar(list(range(len(y))), y)
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.title('Populations of countries')
    plt.show()

def run():
    pop, areas = read()
    graph(pop)

def main():
    run()

if __name__ == '__main__':
    main()