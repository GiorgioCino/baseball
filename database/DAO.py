from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(t.`year`)
from teams t
where t.year >= 1980
"""

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllTeams():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.year,t.teamCode,t.name
                   from teams t



    """

        cursor.execute(query)

        for row in cursor:
            results.append(Team(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(anno, id_map_teams):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.teamCode
                       from teams t
                       where t.year = %s



        """

        cursor.execute(query, (anno,))

        for row in cursor:
            results.append(id_map_teams[row["teamCode"]])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getSalariSquadre(anno):
        conn = DBConnect.get_connection()
        results = {}

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT s.teamCode AS teamCode, SUM(s.salary) AS salarioTotale
            FROM salaries s
            WHERE s.year = %s
            GROUP BY s.teamCode
        """

        cursor.execute(query, (anno,))

        for row in cursor:
            results[row["teamCode"]] = row["salarioTotale"]

        cursor.close()
        conn.close()
        return results
