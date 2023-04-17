"""empty message

Revision ID: 1.7.2
Revises: 1.7.1
Create Date: 2023-04-17 12:03:19.163501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1.7.2'
down_revision = '1.7.1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roms', sa.Column('p_name', sa.String(length=150), nullable=True))
    op.add_column('roms', sa.Column('url_cover', sa.Text(), nullable=True))
    op.alter_column('roms', 'name', new_column_name='r_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roms', 'p_name')
    op.drop_column('roms', 'url_cover')
    op.alter_column('roms', 'r_name', new_column_name='name')
    # ### end Alembic commands ###
