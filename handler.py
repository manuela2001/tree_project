import json

def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response

def arbolito_navidad(event, context):
    pisos = 10  # Número de pisos del árbol
    arbol = ""  # Variable para guardar el árbol en formato string

    # Dibujar el árbol
    for piso in range(1, pisos + 1):
        arbol += ' ' * (pisos - piso) + '*' * (2 * piso - 1) + "\n"

    # Dibujar el tronco
    for _ in range(2):  # Tronco con 2 líneas
        arbol += ' ' * (pisos - 1) + '***\n'

    # Devolver el árbol como respuesta HTTP
    return {'statusCode': 200, 'body': json.dumps(arbol)}

