"""add content column to post table

Revision ID: affbed83cb3c
Revises: 3074464a0673
Create Date: 2025-09-27 17:00:55.529558

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "affbed83cb3c"
down_revision: Union[str, Sequence[str], None] = "3074464a0673"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
