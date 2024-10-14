from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar testimonios
testimonios = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        # Añadir el testimonio a la lista de testimonios
        testimonios.append({'name': name, 'message': message})
        
        # Redirigir a la página de inicio para mostrar el testimonio recién añadido
        return redirect(url_for('index'))
    
    return render_template('index.html', testimonios=testimonios)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        # Añadir el testimonio a la lista de testimonios
        testimonios.append({'name': name, 'message': message})
        
        # Redirigir a la página de inicio
        return redirect(url_for('index'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)