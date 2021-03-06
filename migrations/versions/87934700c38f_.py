"""empty message

Revision ID: 87934700c38f
Revises: 
Create Date: 2022-03-28 00:04:04.095700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87934700c38f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plate',
    sa.Column('plate', sa.String(), nullable=False),
    sa.Column('owner', sa.String(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('plate')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plate')
    # ### end Alembic commands ###
