"""Coloured roles...

Revision ID: 45e42b78bc60
Revises: e761b419fc11
Create Date: 2023-02-22 23:22:32.798832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e42b78bc60'
down_revision = 'e761b419fc11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_role')
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role_name', sa.String(length=150), nullable=True))
        batch_op.drop_column('role')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
        batch_op.create_foreign_key(None, 'role', ['role'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=150), nullable=True))
        batch_op.drop_column('role_name')

    op.create_table('_alembic_tmp_role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('color', sa.VARCHAR(length=8), nullable=True),
    sa.Column('role_name', sa.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
