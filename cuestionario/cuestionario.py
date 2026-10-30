cuestionario.html

#Configuracion de conexion para la base de datos en phpmyadmin
def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='cuestionario',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    edad = request.form['edad']
    semestre = request.form['semestre']
    carrera = request.form['carrera']

    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO registros (nombre, correo, edad, semestre, carrera) VALUES (%s, %s,%s,%s,%s)”
            cursor.execute(sql, (nombre,correo, edad, semestre, carrera))
            conexion.commit()
        conexion.close()
        mensaje = "Datos registrados"
    except Exception as e:
        mensaje = f"Hubo un error: {e}"

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
