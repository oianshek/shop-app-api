"""create order_item table

Revision ID: e821a68cf805
Revises: 185418fe8cd8
Create Date: 2021-10-06 14:59:10.343470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e821a68cf805'
down_revision = '185418fe8cd8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'order_item',
        sa.Column('order_id', sa.Integer, sa.ForeignKey('orders.id')),
        sa.Column('item_id', sa.Integer, sa.ForeignKey('items.id'))
    )


def downgrade():
    pass
