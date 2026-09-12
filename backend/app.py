from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir peticiones del frontend

# Función para conectar a tu base de datos MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="practica_servicios_tecnicos"
    )

# Ruta para el inicio de sesión (Login)
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data:
        return jsonify({"success": False, "message": "Faltan datos en formato JSON"}), 400
        
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"success": False, "message": "El usuario y la contraseña son obligatorios"}), 400
        
    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        
        # Consulta segura para verificar el usuario
        query = "SELECT * FROM usuario WHERE nombre = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if user:
            return jsonify({
                "success": True, 
                "message": "Inicio de sesión exitoso",
                "usuario": {"nombre": user.get('nombre'), "correo": user.get('correo')}
            }), 200
        else:
            return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"}), 401
            
    except Exception as e:
        return jsonify({"success": False, "message": f"Error en el servidor: {str(e)}"}), 500

# Ruta para ver la lista de usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

