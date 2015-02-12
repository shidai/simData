#!/bin/bash

rm -f obs*
sh makeProf.sh $1 > prof.pt
./make.py $3 $2 > input

i=0
while read line;do
	mjd=`echo $line | awk '{print $1}'`
#	dm=10
	dm=`echo $line | awk '{print $2}'`
	noise=`echo $line | awk '{print $3}'`
#	echo $mjd $dm $noise
	sed "s/DM 0.0/DM $dm/g" J1713+0747.tmp > obs$i.par
	echo START_OBS
	echo PHEAD P456_header
	echo SRC J1713+0747
	echo "FILE obs$i.rf" 
	echo TYPE PSR
	echo "STT_IMJD $mjd"
	echo STT_SMJD 990
	echo STT_OFFS 0.0034883
	echo TSUB 3840   
	echo NSUB 1    
	echo NCHAN $1
	echo NBIN 1024 
	echo NPOL 1
	echo EXACT_EPHEMERIS obs$i.par 
	echo TEMPLATE prof.pt
	echo CFREQ 1369.0
	echo BW -1024
	echo SEGLENGTH 1800
	echo NFREQ_COEFF 32
#	echo WHITE_LEVEL 5
	echo "#WHITE_LEVEL $noise"
	echo "#SCINT_FREQBW 24"
	echo "#SCINT_TS 2855"
	echo TSYS 21
	echo TSKY 1
	echo GAIN 0.8
	echo CFLUX 900.1
	echo SI 0.0
#	echo SI -1.06
	echo END_OBS
	echo ------------
	i=$(($i+1))
done<input

