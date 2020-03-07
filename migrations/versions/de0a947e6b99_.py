"""empty message

Revision ID: de0a947e6b99
Revises: 
Create Date: 2020-03-07 04:10:12.961450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de0a947e6b99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('chats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user1_username', sa.String(length=40), nullable=True),
    sa.Column('user2_username', sa.String(length=40), nullable=True),
    sa.Column('writer_username', sa.String(length=40), nullable=True),
    sa.Column('message', sa.String(length=1000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user1_username'], ['users.username'], ),
    sa.ForeignKeyConstraint(['user2_username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chats')
    op.drop_table('users')
    # ### end Alembic commands ###
