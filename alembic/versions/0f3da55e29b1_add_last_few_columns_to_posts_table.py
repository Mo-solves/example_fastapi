"""add last few columns to posts table

Revision ID: 0f3da55e29b1
Revises: cc45d84bb1ce
Create Date: 2025-09-27 17:21:31.185446

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0f3da55e29b1"
down_revision: Union[str, Sequence[str], None] = "cc45d84bb1ce"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        table_name="posts",
        column=sa.Column(
            "published", sa.Boolean, nullable=False, server_default="TRUE"
        ),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
