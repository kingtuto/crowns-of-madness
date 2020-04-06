"""Users table

Revision ID: 9dc8da3ba658
Revises: 
Create Date: 2020-04-03 11:55:46.129070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dc8da3ba658'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player1_id', sa.Integer(), nullable=True),
    sa.Column('player2_id', sa.Integer(), nullable=True),
    sa.Column('player3_id', sa.Integer(), nullable=True),
    sa.Column('player4_id', sa.Integer(), nullable=True),
    sa.Column('player5_id', sa.Integer(), nullable=True),
    sa.Column('player6_id', sa.Integer(), nullable=True),
    sa.Column('stats', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['player1_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['player2_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['player3_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['player4_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['player5_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['player6_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_game_timestamp'), 'game', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_game_timestamp'), table_name='game')
    op.drop_table('game')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
