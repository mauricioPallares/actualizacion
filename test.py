from updating.updating.connection import Conexion

HOST = "db-bawconexion.c3cy223njycx.us-east-1.rds.amazonaws.com"
USER = "admin"
PASSWORD = "#125899+*"
DB_BAW = "bawcommerce"
DB_HER = "heroku_28eae3090e8e8ef"

connBaw = Conexion(HOST, USER, PASSWORD, DB_BAW)
connHer = Conexion(HOST, USER, PASSWORD, DB_HER)

sql = "SELECT sku, titulo, precio, marca, modelo, peso, caracteristicas, descripcion, imagenes, isPrime, inStock FROM producto WHERE titulo != '' AND editado = 0 AND infraccion = 0 AND deleted_at = 0 LIMIT 20000, 10000 "
connBaw.cursor.execute(sql)

productos = connBaw.cursor.fetchall()

print(len(productos))

for producto in productos:
    print(f"insertando {producto['sku']}")
    sql = "INSERT IGNORE INTO producto_paula (sku, titulo, precio, marca, modelo, peso, caracteristicas, descripcion, imagenes, isPrime, inStock) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s)"
    val = (
    producto['sku'], 
    producto['titulo'], 
    producto['precio'],
    producto['marca'], 
    producto['modelo'], 
    producto['peso'], 
    producto['caracteristicas'], 
    producto['descripcion'], 
    producto['imagenes'],
    producto['isPrime'],
    producto['inStock']
    )

    connHer.cursor.execute(sql, val)
    connHer.connection.commit()