#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:10:24 2021

@author: nickbenelli
"""
import numpy as np
#import sympy
import matrix_formulas

#np.matmul(a, b)
i = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
    ])


a = np.array([
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
    ])

#at = a.transpose()
#b = np.array([0, 1, 0, 3]).transpose()

#np.matmul(at, a)
#np.matmul(a, at)
#np.matmul(at, b)
n = 2

a = np.array([
    [0.00, 0.50, 0.50],
    [0.25, 0.50, 0.25],
    [0.25, 0.25, 0.50]
    ])
u = np.array([1, 0, 0])
output = matrix_utils.transition_probability(u, a, n)

print(output)




