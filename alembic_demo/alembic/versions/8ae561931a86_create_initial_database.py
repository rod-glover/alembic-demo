"""create initial database

Revision ID: 8ae561931a86
Revises: 
Create Date: 2017-07-10 17:01:45.007435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ae561931a86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('login', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )


def downgrade():
    op.drop_table('users')
