from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    name = 'Саша'
    return render_template('index.html',
                           name=name)
@app.route('/<name>/')
def naming(name):
    my_name = f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Моё имя {name}</title>
</head>
<body>
    <p>Моё имя {name}</p>
</body>
</html>
'''
    with open(f'templates/name_{name}.html', 'w', encoding='UTF-8') as f:
        f.write(my_name)
    return my_name
if __name__ == '__main__':
    app.run(debug=True)