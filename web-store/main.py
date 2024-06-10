from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


@app.route("/clothes/")
def clothes():
    _clothes = [
        {
            'title': 'Свитшот',
            'price': '150',
            'image': '/static/image/***.jpg'
        }
    ]
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route("/footwear/")
def footwear():
    _footwear = [
        {
            'title': 'Кроссовки',
            'price': '540',
            'image': '/static/image/footwear.jpg'
        }
    ]
    context = {'title': 'Обувь'}
    return render_template('footwear.html', **context)


@app.route("/backpacks/")
def backpacks():
    _backpacks = [
        {
            'title': 'Рюкзак 15 л.',
            'price': '430',
            'image': '/static/image/***.jpg'
        }
    ]
    context = {'title': 'Рюкзаки'}
    return render_template('backpacks.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
