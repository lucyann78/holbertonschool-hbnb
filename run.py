from flask import Flask

# Definición de la función create_app
def create_app():
    app = Flask(__name__)

    # Rutas y lógica de la aplicación
    @app.route('/')
    def home():
        return "¡Hola Mundo!"

    return app

# Crear la instancia de la aplicación
app = create_app()

# Ejecutar la aplicación con el modo de depuración habilitado
if __name__ == '__main__':
    app.run(debug=True)  # Esto habilita el modo de depuración
