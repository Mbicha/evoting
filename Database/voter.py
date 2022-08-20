from database import connection, cursor

class Voter:
    def __init__(self, name):
        self.name = name

    def insert_voter(self, first_name, middle_name,\
         last_name, id_number, gender, county, country,\
         constituency, ward, poling_station):
        
        sql = ("INSERT INTO evoting.voter (first_name, middle_name,\
         last_name, id_number, gender, county, country,\
         constituency, ward, poling_station) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        
        cursor.execute(sql, (first_name, middle_name,\
         last_name, id_number, gender, county, country,\
         constituency, ward, poling_station,))

        connection.commit()
