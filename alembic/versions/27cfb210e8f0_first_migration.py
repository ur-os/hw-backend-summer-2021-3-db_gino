"""first migration

Revision ID: 27cfb210e8f0
Revises: 0629735fb076
Create Date: 2021-09-12 04:05:31.349150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27cfb210e8f0'
down_revision = '0629735fb076'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('questions_title_key', 'questions', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('questions_title_key', 'questions', ['title'])
    # ### end Alembic commands ###
