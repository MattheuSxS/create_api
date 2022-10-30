# API - É um lugar para disponibilizar recursos e/ou funcionalidades

# 1. Objetivo - Criar uma api de disponiliza a consulta, criacao, edicao e exclusao de livros
# 2. URL base
# 3. Endpoints
    # - localhost/livros (GET)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)
# 4. Quais recursos

from crypt import methods
from distutils.log import debug
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1, 'titulo': 'É Assim que Acaba: 1', 'autor': 'Priscila Catão'
    },
    {
        'id': 2, 'titulo': 'Novembro, 9', 'autor': 'Ryta Vinagre'
    },
    {
        'id': 3, 'titulo': 'Os sete maridos de Evelyn Hugo', 'autor': 'Alexandre Boide '
    },
]

# consultar(todos)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Consultar (id)
@app.route('/books/<int:id>', methods=['GET'])
def get_books_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# Editar
@app.route('/books/<int:id>', methods=['PUT'])
def book_edit(id):
    alter_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(alter_book)
            break

    return jsonify(books[index])

# Criar
@app.route('/books', methods=['POST'])
def get_new_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books[-1])

# Excluir
@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]

    return jsonify(books)


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)