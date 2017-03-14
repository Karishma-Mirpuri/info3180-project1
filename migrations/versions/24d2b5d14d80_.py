"""empty message

Revision ID: 24d2b5d14d80
Revises: 004f816558db
Create Date: 2017-03-11 21:43:59.271256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24d2b5d14d80'
down_revision = '004f816558db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'date')
    # ### end Alembic commands ###