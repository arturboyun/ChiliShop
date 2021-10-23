"""sizes field array

Revision ID: 8182381e49b6
Revises: 8596a0c10215
Create Date: 2021-10-18 16:49:01.899930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8182381e49b6'
down_revision = '8596a0c10215'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('sizes', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'sizes')
    # ### end Alembic commands ###