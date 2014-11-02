#!/bin/bash
arch="$1"    # archivo a modificar
rm processing/log >> processing/log
rm processing/out.arff >> processing/log
rm processing/inp.arff >> processing/log
SMILExtract -C Configs/IS10_paraling.conf -I "$arch" -O processing/out.arff -instname replaceHere -noconsoleoutput 1 -logfile processing/log -appendLogfile 1 >> processing/log
java -cp /usr/share/java/weka.jar weka.filters.unsupervised.attribute.Remove -V -R 1,685,684,676,1441,1432,1442,678,686,1440,691,713,712,1446,1434,1522,256,266,265,264,707,327,1437,258,271,319,1436,277,1330,321,328,329,279,285,270,286 -i processing/out.arff -o processing/inp.arff >> processing/log
sed -i 's/@attribute name string/@attribute sexo {m,f}/g' processing/inp.arff
sed -i 's/replaceHere/?/g' processing/inp.arff
sed -i "s/@relation 'SMILEfeatures-weka.filters.unsupervised.attribute.Remove-V-R1,685,684,676,1441,1432,1442,678,686,1440,691,713,712,1446,1434,1522,256,266,265,264,707,327,1437,258,271,319,1436,277,1330,321,328,329,279,285,270,286'/@relation SMILEfeatures/g" processing/inp.arff >> processing/log
java -cp /usr/share/java/weka.jar weka.classifiers.lazy.IB1 -l Configs/lazyIB1.model -T processing/inp.arff -p 0 -c 1 > processing/resultado.txt
if grep -q "m" processing/resultado.txt; then
   echo "m"
else
	if grep -q "f" processing/resultado.txt; then
   		echo "f"
	else
		echo "ERROR!"
	fi
fi