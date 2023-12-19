"""new init

Revision ID: ade934fba88f
Revises: fbd88ae53458
Create Date: 2023-12-18 19:54:10.652345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ade934fba88f'
down_revision = 'fbd88ae53458'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('addon_name', sa.String(length=255), nullable=False),
    sa.Column('addon_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_addons'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles'))
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_name', sa.String(length=255), nullable=False),
    sa.Column('room_description', sa.Text(), nullable=True),
    sa.Column('room_capacity', sa.Integer(), nullable=True),
    sa.Column('room_address', sa.Text(), nullable=True),
    sa.Column('room_city', sa.Text(), nullable=True),
    sa.Column('room_longlat', sa.Text(), nullable=True),
    sa.Column('room_price', sa.Integer(), nullable=False),
    sa.Column('room_status', sa.Enum('available', 'unavailable'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_rooms')),
    sa.UniqueConstraint('room_name', name=op.f('uq_rooms_room_name'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['role'], ['roles.id'], name=op.f('fk_users_role_roles')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.Date(), nullable=True),
    sa.Column('end_time', sa.Date(), nullable=True),
    sa.Column('addons', sa.JSON(), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], name=op.f('fk_bookings_room_id_rooms')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_bookings_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bookings'))
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('rate', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], name=op.f('fk_ratings_room_id_rooms')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_ratings_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_ratings'))
    )
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('refresh_token', sa.Text(), nullable=False),
    sa.Column('access_token', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_tokens_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tokens'))
    )
    op.drop_index('my_index', table_name='models', mysql_length={'name': 255})
    op.drop_table('models')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.TEXT(), nullable=True),
    sa.Column('value', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('my_index', 'models', ['name'], unique=False, mysql_length={'name': 255})
    op.drop_table('tokens')
    op.drop_table('ratings')
    op.drop_table('bookings')
    op.drop_table('users')
    op.drop_table('rooms')
    op.drop_table('roles')
    op.drop_table('addons')
    # ### end Alembic commands ###