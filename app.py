from flask import Flask, request, render_template_string

# Asegúrate de que main.py esté en el mismo directorio que este archivo, o ajusta la ruta de importación según sea necesario.
from main import generate_password

app = Flask(__name__)


# Define una página simple para generar contraseñas
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Obtiene los parámetros del formulario web
        length = int(request.form.get("length", 8))
        include_numbers = "include_numbers" in request.form
        include_special_chars = "include_special_chars" in request.form
        include_uppercase = "include_uppercase" in request.form

        # Genera la contraseña
        password = generate_password(
            length, include_numbers, include_special_chars, include_uppercase
        )

        # Pasa la contraseña generada de vuelta al template
        return render_template_string(PAGE_TEMPLATE, password=password)
    else:
        # No se ha enviado el formulario, muestra la página por defecto
        return render_template_string(
            PAGE_TEMPLATE, password="Tu contraseña aparecerá aquí."
        )


# HTML del template en forma de string
# HTML del template en forma de string, ahora con CSS responsivo
# HTML del template en forma de string, utilizando Bootstrap
PAGE_TEMPLATE = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Generador de Contraseñas</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
</head>
<body>
    <nav class="container-fluid">
        <ul>
            <li><strong>Generador de Contraseñas</strong></li>
        </ul>
        <ul>
            <li><a href="https://www.configuroweb.com/" role="button">Para más desarrollos configuroweb</a></li>
        </ul>
    </nav>
    <main class="container">
        <div class="grid">
            <section>
                <hgroup>
                    <h2>Genera una contraseña segura</h2>
                    <h3>Completa los siguientes campos</h3>
                </hgroup>
                <form method="post" class="needs-validation" novalidate>
                    <div class="form-group">
                        <label for="length">Longitud:</label>
                        <input type="number" class="form-control" name="length" value="8" required>
                    </div>
                    <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" name="include_numbers" id="include_numbers" checked>
                        <label class="form-check-label" for="include_numbers">Incluir números</label>
                    </div>
                    <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" name="include_special_chars" id="include_special_chars" checked>
                        <label class="form-check-label" for="include_special_chars">Incluir caracteres especiales</label>
                    </div>
                    <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" name="include_uppercase" id="include_uppercase" checked>
                        <label class="form-check-label" for="include_uppercase">Incluir mayúsculas</label>
                    </div>
                    <button type="submit" class="btn btn-primary btn-block">Generar Contraseña</button>
                </form>
                <p class="mt-4 text-center">{{ password }}</p>
            </section>
        </div>
    </main>
    <footer class="container">
        <small>
            <a href="#">Política de privacidad</a> • <a href="#">Términos de servicio</a>
        </small>
    </footer>
</body>
</html>

"""


if __name__ == "__main__":
    app.run(debug=True)
