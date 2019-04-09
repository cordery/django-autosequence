from contextlib import contextmanager

from django.db import connection, transaction
from psycopg2.sql import Identifier, SQL


@contextmanager
def lock_table(model):
    with transaction.atomic():
        try:
            with connection.cursor() as cursor:
                sql = SQL('LOCK TABLE {tbl} IN SHARE ROW EXCLUSIVE MODE') \
                    .format(
                    tbl=Identifier(model._meta.db_table),
                )
                cursor.execute(sql)
                yield
        finally:
            pass
