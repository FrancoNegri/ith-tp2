#!/usr/bin/python
#coding: utf8

import sys
import os
import subprocess 

path = "~/Repos/ith-tp2/opensmile-2.0-rc1/opensmile/config/IS10_paraling.conf"
for i in os.listdir("../tp2-dev/"):
    if i.endswith(".wav"): 
        print "Extrayendo attr de: ", i
        # $DIR/SMILExtract -C $DIR/config/IS10_paraling.conf -I in.wav -O out.arff
        cmd = "SMILExtract -C " + path + " -I ../tp2-dev/"+ i + " -O output.arff"
        p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()
        # output = process.communicate()[0]
        continue
    else:
        continue

