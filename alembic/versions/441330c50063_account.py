"""account

Revision ID: 441330c50063
Revises: 
Create Date: 2021-02-08 22:52:14.644725

"""
from alembic import op
from sqlalchemy import BIGINT, TIMESTAMP, VARCHAR, Column, text

# revision identifiers, used by Alembic.
revision = "441330c50063"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "account",
        Column("id", BIGINT, primary_key=True),
        Column("name", VARCHAR(255), nullable=False),
        Column("api_key", VARCHAR(255), nullable=False),
        Column("secret", VARCHAR(255), nullable=False),
        Column("coins", VARCHAR(255), nullable=False),
        Column("created_at", TIMESTAMP, server_default=text("now()")),
    )


def downgrade():
    op.drop_table("account")
