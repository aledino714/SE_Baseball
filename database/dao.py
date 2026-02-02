from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def read_year_team():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT year 
                    FROM team
                    WHERE year >= 1980
                    GROUP BY year 
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

# result = [
#               {'year': 1980},
#               {'year': 1981},
#               {'year': 1982}
#          ]

#-----------------------------------------------------------------------------------------------
    @staticmethod
    def read_team():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT id, year, team_code, name
                    FROM team
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

# result = [
#               {'id': 1, 'year': 1871, 'team_code': 'BS1', 'name': 'Boston Red Stockings'},
#               {'id': 2, 'year': 1871, 'team_code': 'CH1', 'name': 'Chicago White Stockings'},
#               {'id': 3, 'year': 1871, 'team_code': 'CL1', 'name': 'Cleveland Forest Citys'}
#          ]

#-----------------------------------------------------------------------------------------------
    @staticmethod
    def read_id_team_salary():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select t.id as idteam, SUM(s.salary) as peso
                    from team as t
                    join salary as s on t.id = s.team_id 
                    group by t.id
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

# result = [
#               {'id': 1918, 'peso': 14807000},
#               {'id': 1919, 'peso': 11560712},
#               {'id': 1920, 'peso': 10897560}
#          ]