// frontend/src/services/api.js

const API_URL = 'http://127.0.0.1:5000/api';

// Función para obtener la lista de clientes desde Flask
export async function obtenerClientesService() {
  try {
    const response = await fetch(`${API_URL}/clientes`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error al conectar con la API:', error);
    return { success: false, message: 'Error de conexión con el servidor' };
  }
}

