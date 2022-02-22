from multiprocessing import connection
import pymysql.cursors


def createConnectionDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="personinfobd",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


"""crud"""
# create


def insertNewPerson(person):
    connection = createConnectionDB()
    with connection.cursor() as cursor:
        sql = "INSERT INTO `personinfobd`.`persondata`(`id`,`name`,`age`,`salary`)VALUES(%s,%s,%s,%s);"
        cursor.execute(sql, (0, person.name, person.age, person.salary))
    connection.commit()


# show all persons


def selectAllPersons() -> list:
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM personinfobd.persondata;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


# show one person by id


def selectPersonBy(id) -> dict:
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM personinfobd.persondata where id=%s;"
            cursor.execute(sql, id)
            result = cursor.fetchone()
            return result


# update


def updatePerson(person):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `personinfobd`.`persondata` SET `name` = %s, `age` = %s, `salary` = %s WHERE `id` = %s;"
            cursor.execute(sql, (person.name, person.age, person.salary, person.id))
        connection.commit()


# delete
def deletePersonBy(id):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `personinfobd`.`persondata` WHERE id=%s;"
            cursor.execute(sql, id)
        connection.commit()
