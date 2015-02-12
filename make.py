#!/usr/bin/python

import math
import numpy as np
import sys

def calDM(array,mjd):
	(nd,md) = array.shape
	for i in np.arange(0,nd-1):
		if (array[i,0]<mjd and array[i+1,0]>mjd):
			dm = mjd*(array[i,1]-array[i+1,1])/(array[i,0]-array[i+1,0])+array[i+1,1]-array[i+1,0]*(array[i,1]-array[i+1,1])/(array[i,0]-array[i+1,0])
#			dm = 10.0*(mjd*(array[i,1]-array[i+1,1])/(array[i,0]-array[i+1,0])+array[i+1,1]-array[i+1,0]*(array[i,1]-array[i+1,1])/(array[i,0]-array[i+1,0]))
	return dm

n = int(sys.argv[1])
dm0 = float(sys.argv[2])

dmV = np.loadtxt('J1713.txt')
gap = (dmV[-1,0]-dmV[0,0])/(n)

mu, sigma = 0, 30
i = 1 + abs(np.random.normal(mu, sigma, n))
#i = np.ones(n)*0.1

for j in np.arange(0,n):
	#	mjd = 53453.011458 + (int)(n*20.0)
	mjd = dmV[0,0] + (int)(gap) + (int)(j*gap)
	dmt = dm0
#	dmt = dm0 + calDM(dmV,mjd)
	print mjd,dmt,i[j]
