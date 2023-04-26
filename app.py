from flask import Flask, render_template, request, redirect, url_for, flash

# Crea la instancia de la aplicación
app=Flask(__name__)

# Crea la vista index, URL principal
@app.route('/')
def index():
	return "<h1> ¡¡¡ Bienvenido a Flask !!! <h1>"

# Ejecutamos la aplicación. 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
