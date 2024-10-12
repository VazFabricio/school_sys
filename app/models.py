from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Date
from .db_access import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255))
    email = Column(String(255))
    telefone = Column(String(255))
    endereco = Column(String(255))

    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

class Produto(Base): 
    __tablename__ = 'produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome_produto = Column(String(255))
    preco = Column(DECIMAL(10, 2))  
    estoque = Column(Integer)  

    def __init__(self, nome_produto, preco, estoque):
        self.nome_produto = nome_produto
        self.preco = preco
        self.estoque = estoque

class Pedido(Base): 
    __tablename__ = 'pedido'

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente')) 
    id_produto = Column(Integer, ForeignKey('produto.id_produto'))  
    data_pedido = Column(Date)
    quantidade = Column(Integer)
    valor_total = Column(DECIMAL(10, 2))  

    def __init__(self, id_pedido, id_cliente, id_produto, data_pedido, quantidade, valor_total):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.data_pedido = data_pedido
        self.quantidade = quantidade
        self.valor_total = valor_total
