"""Add nome_cliente and nome_restaurante to Reserva

Revision ID: 6302b270345a
Revises: e733b4127f5f
Create Date: 2024-06-06 12:43:20.268500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6302b270345a'
down_revision = 'e733b4127f5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reserva', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome_cliente', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('nome_restaurante', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reserva', schema=None) as batch_op:
        batch_op.drop_column('nome_restaurante')
        batch_op.drop_column('nome_cliente')

    # ### end Alembic commands ###