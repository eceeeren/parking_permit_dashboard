"""empty message

Revision ID: 0c3a9428d85a
Revises: 87934700c38f
Create Date: 2022-03-28 00:07:53.129194

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0c3a9428d85a'
down_revision = '87934700c38f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plate', 'owner',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('plate', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('plate', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plate', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('plate', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('plate', 'owner',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
