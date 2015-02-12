#!/bin/bash

rm obs* temp* 
cp ../obs*.rf .

pat -s paas.std -f tempo2 obs*.rf > rf.tim
tempo2 -nobs 300000 -output general2 -s "{file} {ism} {ipm} {freqSSB}\n" -f J1713+0747.tmp rf.tim > temp

for f in `ls obs*.rf`; do
	grep $f temp | awk '{print $2, $3, $4}' > $f.tdis 
	echo $f
done

