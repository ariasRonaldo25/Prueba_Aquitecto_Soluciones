
import psycopg2  # Módulo para conectarse a la base de datos on-premise
import boto3  # Módulo para interactuar con los servicios de AWS

# Configuración de la conexión a la base de datos on-premise
db_host = 'localhost'
db_name = 'nombre_basedatos'
db_user = 'usuario'
db_password = 'contraseña'

# Configuración de la conexión a la base de datos en AWS
aws_region = 'us-east-1'
aws_db_instance_identifier = 'nombre_instancia'
aws_db_name = 'nombre_basedatos'
aws_db_user = 'usuario'
aws_db_password = 'contraseña'

# Conexión a la base de datos on-premise
on_premise_conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
on_premise_cursor = on_premise_conn.cursor()

# Consulta de los datos en la base de datos on-premise
on_premise_cursor.execute('SELECT * FROM tabla_datos')
data = on_premise_cursor.fetchall()

# Cierre de la conexión a la base de datos on-premise
on_premise_cursor.close()
on_premise_conn.close()

# Conexión a la base de datos en AWS
aws_rds_client = boto3.client('rds', region_name=aws_region)

# Inserción de los datos en la base de datos en AWS
for row in data:
    aws_rds_client.execute_statement(
        resourceArn='arn:aws:rds:{}:123456789012:cluster:{}'.format(aws_region, aws_db_instance_identifier),
        secretArn='arn:aws:secretsmanager:{}:123456789012:secret:{}'.format(aws_region, aws_db_instance_identifier),
        database=aws_db_name,
        sql='INSERT INTO tabla_datos VALUES (%s, %s, %s)',
        parameters=[
            {'name': 'param1', 'value': {'stringValue': row[0]}},
            {'name': 'param2', 'value': {'stringValue': row[1]}},
            {'name': 'param3', 'value': {'stringValue': row[2]}}
        ]
    )

print("Datos almacenados en la base de datos en AWS.")

