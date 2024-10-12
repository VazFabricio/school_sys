from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

DB_HOST = '127.0.0.1'
DB_PORT = 3307
DB_NAME = 'bhbus'
DB_USER =  'userbh'
DB_PASSWORD =  'pass_word_user'

def create_connection():
    return mysql.connector.connect(
        host=DB_HOST, 
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=3307
    )

@app.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    telefone = data.get('telefone')
    endereco = data.get('endereco')
    
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)", 
                       (nome, email, telefone, endereco))
        connection.commit()
        return jsonify({"message": "Cliente adicionado com sucesso"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        connection.close()

@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.json
    nome_produto = data.get('nome_produto')
    preco = data.get('preco')
    estoque = data.get('estoque')
    
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO produto (nome_produto, preco, estoque) VALUES (%s, %s, %s)", 
                       (nome_produto, preco, estoque))
        connection.commit()
        return jsonify({"message": "Produto adicionado com sucesso"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        connection.close()

@app.route('/pedidos', methods=['POST'])
def add_pedido():
    data = request.json
    id_cliente = data.get('id_cliente')
    id_produto = data.get('id_produto')
    data_pedido = data.get('data_pedido')
    quantidade = data.get('quantidade')
    
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT preco FROM produto WHERE id_produto = %s", (id_produto,))
    produto = cursor.fetchone()
    
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    
    preco = produto[0]
    valor_total = preco * quantidade
    
    try:
        cursor.execute("INSERT INTO pedido (id_cliente, id_produto, data_pedido, quantidade, valor_total) VALUES (%s, %s, %s, %s, %s)", 
                       (id_cliente, id_produto, data_pedido, quantidade, valor_total))
        connection.commit()
        return jsonify({"message": "Pedido registrado com sucesso"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
