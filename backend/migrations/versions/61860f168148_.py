"""empty message

Revision ID: 61860f168148
Revises: 
Create Date: 2019-11-11 00:06:20.472174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61860f168148'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('edges',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('beginning_stop', sa.String(length=10), nullable=True),
    sa.Column('ending_stop', sa.String(length=10), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('links',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('stop_id', sa.String(length=10), nullable=True),
    sa.Column('route_id', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routes',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stops',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stops')
    op.drop_table('routes')
    op.drop_table('links')
    op.drop_table('edges')
    # ### end Alembic commands ###
