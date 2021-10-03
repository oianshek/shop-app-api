"""create_users_table

Revision ID: 9d8160d329fa
Revises: 
Create Date: 2021-09-28 15:01:12.282507

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9d8160d329fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('users')
