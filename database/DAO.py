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

    @staticmethod
    def getAllEdges(ai, af):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct c1.constructorId  as cn1, c2.constructorId  as cn2, count(distinct r1.driverId ) as peso
                   from constructors c1, constructors c2, results r1, results r2, races rs1, races rs2
                   where c1.constructorId < c2.constructorId 
                   and c1.constructorId = r1.constructorId 
                   and c2.constructorId = r2.constructorId 
                   and r1.driverId = r2.driverId
                   and rs1.raceId = r1.raceId
                   and rs2.raceId = r2.raceId
                   and rs1.year >=  %s and rs1.year <= %s and r1.position is not null
                   and rs2.year >=  %s and rs2.year <= %s and r2.position is not null	
                   group by c1.constructorId , c2.constructorId """
        cursor.execute(query, (ai,af,ai,af))
        for row in cursor:
            result.append((row["cn1"], row["cn2"], row["peso"]))
        cursor.close()
        conn.close()
        return result


