"""third

Revision ID: 4ac70cf96318
Revises: 99ce62f63880
Create Date: 2024-01-19 12:22:41.120515

"""
from alembic import op
import sqlalchemy as sa
from infra.configs.connection import DBConnectionHandler


# revision identifiers, used by Alembic.
revision = '4ac70cf96318'
down_revision = '99ce62f63880'
branch_labels = None
depends_on = None


def upgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    engine.execute(
        '''
          INSERT INTO filmes (titulo, genero, ano)
          VALUES
          ('Estou', 'aqui', 25);
        '''
    )


def downgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    engine.execute(
        '''
          DELETE FROM filmes
          WHERE titulo='Estou';
        '''
    )