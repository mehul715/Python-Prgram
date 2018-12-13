#!/bin/bash


while true;
do
	fname=$(date +%Y-%m-%d-%H-%M-%S)
	wget -O ${fname}.html http://wsj.com/mdc/public/page/2_3021-activnyse-actives.html
	java -jar tagsoup-1.2.1.jar --files ${fname}.html
	python3 phy.py ${fname}.xhtml
	
sleep 60

done


