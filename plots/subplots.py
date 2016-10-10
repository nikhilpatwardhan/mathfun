# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:29:48 2016

@author: Nikhil
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
    
def test1():
    f, axes = plt.subplots(2, 2, sharex=True, sharey=True)
    
    axes[0,0].plot(np.sin(x))
    axes[0,1].plot(np.sin(2*x))
    axes[1,0].plot(np.sin(3*x))
    axes[1,1].plot(np.sin(4*x))
    
    plt.show()

def test2():
    f, axes = plt.subplots(2, 1, sharex=True, sharey=True)
    
    axes[0].plot(np.sin(x), label='sin')
    axes[1].plot(np.cos(x), label='cos')
    plt.legend()
    plt.show()

def test3():
    plt.hold(True)
    plt.plot(x, np.sin(x), label='sin')
    plt.plot(x, np.cos(x), label='cos')
    plt.legend(loc='best') # Figure out a non-overlapping region
    plt.xlabel('angle in Radians')
    plt.grid()
    plt.show()

def test4():
    plt.hold(True)
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.sin(2*x), label='sin(2x)')
    plt.plot(x, np.sin(3*x), label='sin(3x)')
    plt.legend(loc='best') # Figure out a non-overlapping region
    plt.xlabel('angle in Radians')
    plt.grid()
    plt.show()

def main():
    test4()

if __name__ == '__main__':
    main()