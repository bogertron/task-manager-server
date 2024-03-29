"""empty message

Revision ID: 0e5279ed109c
Revises: e65dd1dec0c4
Create Date: 2019-07-20 12:12:08.983358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e5279ed109c'
down_revision = 'e65dd1dec0c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assignment', sa.String(length=255), nullable=True),
    sa.Column('createdTS', sa.DateTime(timezone=True), nullable=True),
    sa.Column('completedTS', sa.DateTime(timezone=True), nullable=True),
    sa.Column('isComplete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
