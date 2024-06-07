from database.DB_connect import DBConnect
from model.metodo import Metodo
from model.prodotto import Prodotto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getMetodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
        from go_methods g"""

        cursor.execute(query)

        for row in cursor:
            result.append(Metodo(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(metodo,anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.*
                    from go_daily_sales gds
                    join go_products gp on gds.Product_number =gp.Product_number 
                    where year( gds.`Date` )=%s and gds.Order_method_code=%s"""

        cursor.execute(query, (anno,metodo,))

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPrezzoTot( metodo, anno):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gds.Product_number as prodotto,sum(Unit_sale_price*Quantity) as prezzo
                    from go_daily_sales gds
                    where year( gds.`Date` )=%s and gds.Order_method_code=%s
                    group by gds.Product_number """

        cursor.execute(query, (anno, metodo))

        for row in cursor:
            result[row["prodotto"]]=row["prezzo"]

        cursor.close()
        conn.close()
        return result


