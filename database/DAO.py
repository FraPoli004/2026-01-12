from database.DB_connect import DBConnect
from model.Constructor import Constructor


class Costruttore:
    pass


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(ai,af):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.constructorId , c.constructorRef, c.name, c.nationality
                    from constructors c 
                    join results r on c.constructorId = r.constructorId join races r2 on r.raceId = r2.raceId
                    where r2.year >= %s and r2.year <= %s and r.position is not null"""

        cursor.execute(query, (ai,af))

        for row in cursor:
            results.append(Constructor(**row))

        cursor.close()
        conn.close()
        return results

