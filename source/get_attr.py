#!/usr/bin/python
#coding: utf8

import sys
import os
import subprocess 

offset_output_arf = 1590


path = "~/Repos/ith-tp2/opensmile-2.0-rc1/opensmile/config/IS10_paraling.conf"
for i in os.listdir("../tp2-dev/"):
    if i.endswith(".wav"): 
        print "Extrayendo attr de: ", i
        # $DIR/SMILExtract -C $DIR/config/IS10_paraling.conf -I in.wav -O out.arff
        cmd = "SMILExtract -C " + path + " -I ../tp2-dev/"+ i + " -O output.arff"
        p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()


        #aca cambio el atributo numeric class que no sirve de nada por el nuestro de si es femenino o masculino


        print "Cambiando attr numeric_class de: ", i

        num_lines = sum(1 for line in open('output.arff'))
        lol = open("2output.arff", "w")
        with open("output.arff", "r+") as f:
            texto = f.readlines()
            f.seek(0)
            contador = 1
            for line in texto:
                if contador == num_lines:
                    if "m" in i:
                        lol.write(line[:-4] + "m\n");
                    else:
                        lol.write(line[:-4] + "f\n");
                else:
                    lol.write(line)
                contador = contador +1
            f.close()
        lol.close()
        cmd = "rm output.arff"
        p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()

        cmd = "mv 2output.arff output.arff"
        p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()



        # output = process.communicate()[0]
        continue
    else:
        continue

lol = open("2output.arff", "w")
with open("output.arff", "r+") as f:
    texto = f.readlines()
    for line in texto:
        if "numeric_class numeric" in i:
            lol.write("@attribute gender {m,f}")
        else:
            lol.write(line)
    f.close()
lol.close()
cmd = "rm output.arff"
p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()

cmd = "mv 2output.arff output.arff"
p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
