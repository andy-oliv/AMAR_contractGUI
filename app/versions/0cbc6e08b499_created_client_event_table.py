"""created_client_event_table

Revision ID: 0cbc6e08b499
Revises: 69d93203baf3
Create Date: 2025-04-06 15:59:17.333223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0cbc6e08b499'
down_revision: Union[str, None] = '69d93203baf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "client_event",
        sa.Column("id", sa.Integer, autoincrement=True, primary_key=True),
                sa.Column("client_id", sa.String(36), nullable=False),
                sa.Column("event_id", sa.String(36), nullable=False)
    )

def downgrade() -> None:
    op.drop_table("client_event")