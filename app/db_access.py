from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Database:
    def __init__(self, host, database, user, password, port):
        self.engine = self.create_engine(host, database, user, password, port)
        self.Session = sessionmaker(bind=self.engine)

    def create_engine(self, host, database, user, password, port):
        db_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
        
        try:
            engine = create_engine(db_url)
            print("Connection to MySQL DB successful using SQLAlchemy")
            return engine
        except Exception as e:
            print(f"Failed to connect to DB: {str(e)}")
            return None

    def get_session(self):
        # Cria uma sessão para interação com o banco
        return self.Session()

    def create_all(self):
        # Cria todas as tabelas definidas na Base
        Base.metadata.create_all(self.engine)
