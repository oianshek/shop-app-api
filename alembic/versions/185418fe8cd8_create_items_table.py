"""create items table

Revision ID: 185418fe8cd8
Revises: 4803989967c9
Create Date: 2021-10-06 14:58:34.305640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '185418fe8cd8'
down_revision = '4803989967c9'
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
