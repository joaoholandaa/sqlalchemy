from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.filmes import Filmes
from infra.entities.atores import Atores
from .filmes_repository import FilmesRepository

class ConnectionHandlerMock:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data=[
        (
          [mock.call.query(Filmes)],
          [Filmes(titulo="Alice", genero="MMM", ano=12)]
        ),
        (
          [
            mock.call.query(Filmes),
            mock.call.filter(Filmes.genero=='jajfjh')
          ],
          [Filmes(titulo="Ola", genero="MMM", ano=12)]
        )
      ]
    )
  
  def  __enter__(self):
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()

def test_select():
  film_repository = FilmesRepository(ConnectionHandlerMock)
  response = film_repository.select()
  print()
  print(response)
  assert isinstance(response, list)
  assert isinstance(response[0], Filmes)

def test_select_drama_filmes():
  film_repository = FilmesRepository(ConnectionHandlerMock)
  response = film_repository.select_drama_filmes()
  print()
  print(response)
  assert isinstance(response, Filmes)
  assert response.titulo == 'Ola'

def test_insert():
  film_repository = FilmesRepository(ConnectionHandlerMock)
  response = film_repository.insert('something', 'AAAA', 33)
  print()
  print(response)