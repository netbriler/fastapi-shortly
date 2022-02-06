"""Init

Revision ID: 8cb75180a8a4
Revises: 
Create Date: 2022-02-06 14:51:07.024536

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '8cb75180a8a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('alias', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('original_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_link_alias'), 'link', ['alias'], unique=False)
    op.create_index(op.f('ix_link_id'), 'link', ['id'], unique=False)
    op.create_index(op.f('ix_link_original_url'), 'link', ['original_url'], unique=False)
    op.create_index(op.f('ix_link_title'), 'link', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_link_title'), table_name='link')
    op.drop_index(op.f('ix_link_original_url'), table_name='link')
    op.drop_index(op.f('ix_link_id'), table_name='link')
    op.drop_index(op.f('ix_link_alias'), table_name='link')
    op.drop_table('link')
    # ### end Alembic commands ###