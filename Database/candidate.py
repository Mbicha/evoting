from nis import maps
from database import connection, cursor

class Candidate:
    _table_name = ""

    def __init__(self):
        self._table_name = "candidate"

    def insert_candidate(self, candidate_id, position):
        sql = ("INSERT INTO candidate(candidate_id, electoral_position) VALUES (%s,%s)")
        cursor.execute(sql, (candidate_id, position,))
        connection.commit()
        print("Successfully Created")

    def list_mp_candidates(self, pos="MP"):
        sql = ("SELECT * FROM candidate WHERE electoral_position=%s")
        cursor.execute(sql,(pos,))
        mps = cursor.fetchall()

        for mp in mps:
            print(mp)