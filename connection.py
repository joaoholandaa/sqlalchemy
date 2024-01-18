from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Configuracoes 
engine = create_engine('mysql+pymysql://root:admin@localhost:3306/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filmes(Base):
  __tablename__ = "filmes"

  titulo = Column(String, primary_key=True)
  genero = Column(String, nullable=False)
  ano = Column(Integer, nullable=False)

  def __repr__(self):
    return f"Filme [titulo={self.titulo}, ano={self.ano}]"

# SQL
# Insert
data_insert = Filmes(titulo="Sonic", genero="Aventura", ano=2020)
session.add(data_insert)
session.commit()

# Delete
session.query(Filmes).filter(Filmes.titulo=="Batman").delete()
session.commit()

# Update
session.query(Filmes).filter(Filmes.genero=="Drama").update({"ano": 2000})
session.commit()

# Select
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

session.close()