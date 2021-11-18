"""product top_sizes

Revision ID: 3cc20ceb0b4d
Revises: 8182381e49b6
Create Date: 2021-11-15 09:26:56.433987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cc20ceb0b4d'
down_revision = '8182381e49b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('top_sizes', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'top_sizes')
    # ### end Alembic commands ###
