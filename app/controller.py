from .models import Cliente, Produto, Pedido

class ClienteController:
    @staticmethod
    def criar_cliente(dados, db):
        with db.get_session() as db_session:
            cliente = Cliente(
                nome=dados['nome'],
                email=dados['email'],
                telefone=dados['telefone'],
                endereco=dados['endereco']
            )
            db_session.add(cliente)
            db_session.commit()
            return cliente.id_cliente


class ProdutoController:
    @staticmethod
    def criar_produto(dados, db):
        with db.get_session() as db_session:
            produto = Produto(
                nome_produto=dados['nome_produto'],
                preco=dados['preco'],
                estoque=dados['estoque']
            )
            db_session.add(produto)
            db_session.commit()
            return produto.id_produto
    
    @staticmethod
    def get_all(db):
        with db.get_session() as db_session:
            produtos = db_session.query(Produto).all() 
            return produtos


class PedidoController:
    @staticmethod
    def criar_pedido(dados, db):
        with db.get_session() as db_session:
            pedido = Pedido(
                id_cliente=dados['id_cliente'],
                id_produto=dados['id_produto'],
                data_pedido=dados['data_pedido'],
                quantidade=dados['quantidade'],
                valor_total=dados['valor_total']
            )
            db_session.add(pedido)
            db_session.commit()
            return pedido.id_pedido
