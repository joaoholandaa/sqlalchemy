from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

repo.insert('Batman', 'Acao', 2022)
repo.delete('Dracula')

data = repo.select()

print(data)