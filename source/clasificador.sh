#!/bin/bash
arch=$1    # archivo a modificar
SMILExtract -C config/IS10_paraling.conf -I $arch -O out.arff -instname "?"
sed -i 's/@attribute name string/@attribute sexo {m,f}/g' out.arff
java -cp /usr/share/java/weka.jar weka.filters.unsupervised.attribute.Remove -V -R 1, 685, 684, 676, 1441, 1432, 1442, 678, 686, 1440, 691, 713, 712, 1446, 1434, 1522, 256, 266, 265, 264, 707, 327, 1437, 258, 271, 319, 1436, 277, 1330, 321, 328, 329, 279, 285, 270, 286 -i inp.arff -o out.arff
java -cp /usr/share/java/weka.jar weka.classifiers.lazy.IB1 -l lazyIB1.model -T inp.arff