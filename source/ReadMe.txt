Ahora el archivo .py no solo extrae los atributos sino que borra el ultimo de los atributos (que no era nada) y lo reemplaza por el atributo gender que indica si es f o m.

Usando weka, creo que ahora que tenemos la clase que queremos distinguir weka funcióna como corresponde.

Si se vuelve a correr el .py hay que reemplazar el atributo que dice "numeric_class numeric" por uno que diga: "gender {m,f}"
(traté de hacerlo con el script, pero python no me dio bola)

Probando el weka, hay que borrar el atributo "name" para que ande, sinó te tira cosas raras cuando los queres rankear.