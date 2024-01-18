from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:admin@localhost:3306/cinema')
response = engine.execute('SELECT * FROM filmes')

for row in response:
  print(row)
  print(row.titulo)