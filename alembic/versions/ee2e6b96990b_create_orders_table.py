"""create_orders_table

Revision ID: ee2e6b96990b
Revises: 9d8160d329fa
Create Date: 2021-09-28 15:59:16.032820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee2e6b96990b'
down_revision = '9d8160d329fa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date_created', sa.DateTime, nullable=False),
        sa.Column('price', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('item_id', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('orders')
