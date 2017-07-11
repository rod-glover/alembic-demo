"""add Addresses

Revision ID: 188868acd420
Revises: 8ae561931a86
Create Date: 2017-07-10 17:21:49.336815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '188868acd420'
down_revision = '8ae561931a86'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('addresses',
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=128), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=False),
    sa.Column('province', sa.String(length=32), nullable=False),
    sa.Column('postal_code', sa.String(length=6), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('address_id')
    )


def downgrade():
    op.drop_table('addresses')
