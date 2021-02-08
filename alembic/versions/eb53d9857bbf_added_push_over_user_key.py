"""added push over user key

Revision ID: eb53d9857bbf
Revises: 441330c50063
Create Date: 2021-02-09 02:32:31.796695

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy import BIGINT, TIMESTAMP, VARCHAR, Column, text

# revision identifiers, used by Alembic.
revision = "eb53d9857bbf"
down_revision = "441330c50063"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("account", Column("user_key", VARCHAR(255)))


def downgrade():
    pass
