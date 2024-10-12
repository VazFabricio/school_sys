from flask import Blueprint, request, jsonify, current_app
from .controller import ClienteController, ProdutoController, PedidoController

clientes_bp = Blueprint('clientes', __name__)
produtos_bp = Blueprint('produtos', __name__)
pedidos_bp = Blueprint('pedidos', __name__)

@clientes_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    dados = request.json
    try:
        db = current_app.db  # Acessando a instância do banco
        cliente_id = ClienteController.criar_cliente(dados, db)
        return jsonify({"mensagem": "Cliente criado com sucesso!", "id_cliente": cliente_id}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@produtos_bp.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.json
    try:
        db = current_app.db  # Acessando a instância do banco
        produto_id = ProdutoController.criar_produto(dados, db)
        return jsonify({"mensagem": "Produto criado com sucesso!", "id_produto": produto_id}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@produtos_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    try:
        db = current_app.db  # Acessando a instância do banco
        produtos = ProdutoController.get_all(db)
        produtos_json = [{"id_produto": p.id_produto, "nome_produto": p.nome_produto, "preco": p.preco, "estoque": p.estoque} for p in produtos]
        return jsonify(produtos_json), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@pedidos_bp.route('/pedidos', methods=['POST'])
def criar_pedido():
    dados = request.json
    try:
        db = current_app.db  # Acessando a instância do banco
        pedido_id = PedidoController.criar_pedido(dados, db)
        return jsonify({"mensagem": "Pedido criado com sucesso!", "id_pedido": pedido_id}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
