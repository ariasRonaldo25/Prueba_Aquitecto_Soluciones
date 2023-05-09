# Prueba_Aquitecto_Soluciones
Prueba tecnica aprendiz arquitecto de soluciones Zenware

<p align="center"><img src="https://github.com/ariasRonaldo25/Prueba_Aquitecto_Soluciones/blob/main/img/Arquitectura.png" height="450px"></p>

## Descripción.

En este diagrama, los dispositivos de medición (por ejemplo, medidores de agua) están conectados a AWS IoT Core, que es un servicio de administración de dispositivos de IoT en AWS. AWS IoT Core recibe los datos de medición de los dispositivos y los transmite a través de la nube de AWS.

Luego, los datos de medición se procesan utilizando AWS Lambda, que permite realizar operaciones de procesamiento adicional, como validación de datos o cálculos específicos.

Después del procesamiento, los datos se almacenan en servicios de almacenamiento de AWS, como Amazon S3 (Simple Storage Service) o Amazon DynamoDB, donde se pueden escalar y mantener de manera duradera.

Por último, los datos almacenados se pueden analizar y visualizar utilizando servicios de análisis de datos de AWS, como Amazon Redshift, Amazon QuickSight u otros servicios similares. Esto permite realizar análisis en profundidad y visualizar los resultados para obtener información valiosa.

Cabe destacar que este es solo un ejemplo de arquitectura y se puede adaptar según las necesidades y requisitos específicos de la empresa de servicios públicos.
