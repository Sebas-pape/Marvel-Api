from routes import create_marvel_app


app = create_marvel_app()

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True, port=5000)