"""empty message

Revision ID: ac1b25f2c714
Revises: 
Create Date: 2023-02-17 19:11:03.616902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac1b25f2c714'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('ativo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuarios_email'), 'usuarios', ['email'], unique=False)
    op.create_index(op.f('ix_usuarios_id'), 'usuarios', ['id'], unique=False)
    op.create_index(op.f('ix_usuarios_nome'), 'usuarios', ['nome'], unique=False)
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('detalhes', sa.String(), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('disponivel', sa.Boolean(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], name='fk_usuarios'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_produtos_detalhes'), 'produtos', ['detalhes'], unique=False)
    op.create_index(op.f('ix_produtos_disponivel'), 'produtos', ['disponivel'], unique=False)
    op.create_index(op.f('ix_produtos_id'), 'produtos', ['id'], unique=False)
    op.create_index(op.f('ix_produtos_nome'), 'produtos', ['nome'], unique=False)
    op.create_index(op.f('ix_produtos_preco'), 'produtos', ['preco'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_produtos_preco'), table_name='produtos')
    op.drop_index(op.f('ix_produtos_nome'), table_name='produtos')
    op.drop_index(op.f('ix_produtos_id'), table_name='produtos')
    op.drop_index(op.f('ix_produtos_disponivel'), table_name='produtos')
    op.drop_index(op.f('ix_produtos_detalhes'), table_name='produtos')
    op.drop_table('produtos')
    op.drop_index(op.f('ix_usuarios_nome'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_id'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_email'), table_name='usuarios')
    op.drop_table('usuarios')
    # ### end Alembic commands ###
