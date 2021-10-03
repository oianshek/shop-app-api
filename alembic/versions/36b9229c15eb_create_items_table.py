"""create items table

Revision ID: 36b9229c15eb
Revises: ee2e6b96990b
Create Date: 2021-10-01 15:21:59.439297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36b9229c15eb'
down_revision = 'ee2e6b96990b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('price', sa.Integer, nullable=False),
        sa.Column('description', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('items')
