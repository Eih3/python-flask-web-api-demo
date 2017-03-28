"""empty message

Revision ID: 7b9fa39b2d0f
Revises: 
Create Date: 2017-03-29 00:30:45.443000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b9fa39b2d0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_en_US', sa.String(length=255), nullable=True),
    sa.Column('description_en_US', sa.Text(), nullable=True),
    sa.Column('title_fr_FR', sa.String(length=255), nullable=True),
    sa.Column('description_fr_FR', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('updated_at', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title_en_US'),
    sa.UniqueConstraint('title_fr_FR')
    )
    op.create_index(op.f('ix_Units_is_active'), 'Units', ['is_active'], unique=False)
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('is_authenticated', sa.Boolean(), nullable=True),
    sa.Column('is_anonymous', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_editor', sa.Boolean(), nullable=True),
    sa.Column('is_member', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('updated_at', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.Integer(), nullable=True),
    sa.Column('locale', sa.String(length=30), nullable=True),
    sa.Column('timezone', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['unit_id'], ['Units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_email'), 'Users', ['email'], unique=True)
    op.create_index(op.f('ix_Users_is_active'), 'Users', ['is_active'], unique=False)
    op.create_index(op.f('ix_Users_locale'), 'Users', ['locale'], unique=False)
    op.create_index(op.f('ix_Users_timezone'), 'Users', ['timezone'], unique=False)
    op.create_index(op.f('ix_Users_username'), 'Users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Users_username'), table_name='Users')
    op.drop_index(op.f('ix_Users_timezone'), table_name='Users')
    op.drop_index(op.f('ix_Users_locale'), table_name='Users')
    op.drop_index(op.f('ix_Users_is_active'), table_name='Users')
    op.drop_index(op.f('ix_Users_email'), table_name='Users')
    op.drop_table('Users')
    op.drop_index(op.f('ix_Units_is_active'), table_name='Units')
    op.drop_table('Units')
    # ### end Alembic commands ###
