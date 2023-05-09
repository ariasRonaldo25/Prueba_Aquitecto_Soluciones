# Prueba_Aquitecto_Soluciones
Prueba tecnica aprendiz arquitecto de soluciones Zenware

<p align="center"><img src="https://github.com/ariasRonaldo25/Prueba_Aquitecto_Soluciones/blob/main/img/Arquitectura.png" height="450px"></p>

## Descripción.

En este diagrama, los dispositivos de medición (por ejemplo, medidores de agua) están conectados a AWS IoT Core, que es un servicio de administración de dispositivos de IoT en AWS. AWS IoT Core recibe los datos de medición de los dispositivos y los transmite a través de la nube de AWS.

Luego, los datos de medición se procesan utilizando AWS Lambda, que permite realizar operaciones de procesamiento adicional, como validación de datos o cálculos específicos.

Después del procesamiento, los datos se almacenan en servicios de almacenamiento de AWS, como Amazon S3 (Simple Storage Service) o Amazon DynamoDB, donde se pueden escalar y mantener de manera duradera.

Por último, los datos almacenados se pueden analizar y visualizar utilizando servicios de análisis de datos de AWS, como Amazon Redshift, Amazon QuickSight u otros servicios similares. Esto permite realizar análisis en profundidad y visualizar los resultados para obtener información valiosa.

Cabe destacar que este es solo un ejemplo de arquitectura y se puede adaptar según las necesidades y requisitos específicos de la empresa de servicios públicos.

Para una información más detallada de la arquitectura propuesta, mayor información sobre el script desarrollado y las demas tareas propuesas consultar el documento general de la solución de la prueba técnica.

## Documento General Desarrollo de la prueba.
[Doc](https://github.com/ariasRonaldo25/Prueba_Aquitecto_Soluciones/blob/main/documento/SOLUCI%C3%93N%20PRUEBA%20T%C3%89CNICA.pdf) Documento con la solución detallada.

## Instrucciones para configurar y ejecutar el script de Python.

1.Instalación de las dependencias:

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python (https://www.python.org).
Instala las bibliotecas necesarias ejecutando los siguientes comandos en tu terminal:

pip install psycopg2
pip install boto3

2.Configuración de la conexión a la base de datos on-premise:

Reemplaza los valores de db_host, db_name, db_user y db_password en el script con los correspondientes a tu base de datos on-premise.

3.Configuración de la conexión a la base de datos en AWS:

Reemplaza los valores de aws_region, aws_db_instance_identifier, aws_db_name, aws_db_user y aws_db_password en el script con los correspondientes a tu entorno en la nube AWS.

4.Ejecución del script:

Abre una terminal o línea de comandos y navega hasta el directorio donde guardaste el archivo del script.
Ejecuta el script usando el comando python db_promise.py.
