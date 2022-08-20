from unittest import result
from database import cursor, connection

class Operation:
    """
        Class holding common database operations
    """
    def count_total(self, tbl, col_name, value):
        """
            Function to return count
            Accepts 3 parameters
            tbl: Table Name
            col_name: Name of the Column
            value: Filter value
            Return count
        """

        sql = ("SELECT COUNT(id) FROM {0} WHERE {1}=%s".format(tbl, col_name))
        cursor.execute(sql, (value,))
        return cursor.fetchall()

    def search_single_entry(self, tbl, col_name, value):
        """
            Function to return all cols of searched single entry
            Accepts 3 parameters
            tbl: Table Name
            col_name: Name of the Column
            value: Filter value
        """

        sql = ("SELECT * FROM {0} WHERE {1}=%s".format(tbl, col_name))
        cursor.execute(sql, (value,))
        return cursor.fetchall()
