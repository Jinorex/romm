"""update to 2.0.0

Revision ID: 2.0.0
Revises: 1.8.3
Create Date: 2023-08-10 22:18:24.012779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2.0.0"
down_revision = "1.8.3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=255), nullable=True),
        sa.Column("hashed_password", sa.String(length=255), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column(
            "role", sa.Enum("VIEWER", "EDITOR", "ADMIN", name="role"), nullable=True
        ),
        sa.Column("avatar_path", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_users_username"), ["username"], unique=True
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_users_username"))

    op.drop_table("users")
    # ### end Alembic commands ###
