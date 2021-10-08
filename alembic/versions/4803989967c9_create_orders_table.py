"""create orders table

Revision ID: 4803989967c9
Revises: 66eb599b5099
Create Date: 2021-10-06 14:56:39.601892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4803989967c9'
down_revision = '66eb599b5099'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date_created', sa.DateTime, nullable=False),
        sa.Column('price', sa.Integer, nullable=False),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'),nullable=False)
    )


def downgrade():
    op.drop_table('orders')
