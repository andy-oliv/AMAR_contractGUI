"""created_tables_clients_events

Revision ID: 69d93203baf3
Revises: 
Create Date: 2025-04-06 14:05:52.494854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '69d93203baf3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'clients',
        sa.Column("id", sa.String(36), nullable=False, primary_key=True),
                 sa.Column("name", sa.String(50), nullable=False),
                 sa.Column("email", sa.String(120), nullable=False),
                 sa.Column("address", sa.String(255), nullable=False),
                 sa.Column("cpf", sa.String(11), nullable=False),
    )

    op.create_table(
        'events',
        sa.Column("id", sa.String(36), nullable=False, primary_key=True),
                 sa.Column("name", sa.String(100), nullable=False),
                 sa.Column("address", sa.String(255), nullable=False),
                 sa.Column("date", sa.String(10), nullable=False),
                 sa.Column("event_start_time", sa.String(5), nullable=False),
                 sa.Column("commuting_fee", sa.String(6), nullable=False),
                 sa.Column("payment_type", sa.String(6), nullable=False),
                 sa.Column("discount", sa.String(3), nullable=False),
                 sa.Column("payment_due_date", sa.String(10), nullable=False),
                 sa.Column("package", sa.String(50), nullable=False),
                 sa.Column("additional_service", sa.Boolean, nullable=False)
    )

def downgrade() -> None:
    op.drop_table('clients')
    op.drop_table('events')
