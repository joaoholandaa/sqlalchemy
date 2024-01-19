"""first

Revision ID: 8833af687881
Revises: 
Create Date: 2024-01-19 11:58:40.406475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8833af687881'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
  op.create_table(
    'account',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(50), nullable=False),
    sa.Column('description', sa.Unicode(200))
  )


def downgrade() -> None:
  op.drop_table('account')
