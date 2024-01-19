"""second

Revision ID: 99ce62f63880
Revises: 8833af687881
Create Date: 2024-01-19 12:10:24.485963

"""
from alembic import op
import sqlalchemy as sa
from infra.repository.filmes_repository import FilmesRepository
from infra.configs.connection import DBConnectionHandler


# revision identifiers, used by Alembic.
revision = '99ce62f63880'
down_revision = '8833af687881'
branch_labels = None
depends_on = None


def upgrade() -> None:
    filmes_repository = FilmesRepository(DBConnectionHandler)
    filmes_repository.insert('Ola', 'Mundo', 123)


def downgrade() -> None:
    filmes_repository = FilmesRepository(DBConnectionHandler)
    filmes_repository.delete('Ola')