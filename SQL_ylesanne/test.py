import mysql.connector
import hashlib


def connect_mysql():
    sql_server = {
        'host': 'sql11.freemysqlhosting.net',
        'user': "sql11701928",
        'passwd': "Aqznvl4lIa",
        'database': "sql11701928",
        'raise_on_warnings': True
    }
    try:
        return mysql.connector.connect(**sql_server)
    except mysql.connector.Error as err:
        print(f"Viga yhenduse loomisel: {err}")
        return None

def uus_kasutaja():
    kasutaja = input("Sisestage oma kasutajanimi: ")
    parool = input("Sisestage oma parool: ")

    # hashlib ootab sisendiks byte, mitte stringi. Selle jaoks kasutan encode()
    soolatud_parool = hashlib.sha256(parool.encode()).hexdigest()

    # Andmete salvestamine
    try:
        connection = connect_mysql()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO kasutajad (kasutajanimi, parool) VALUES (%s, %s)"
            cursor.execute(sql, (kasutaja, soolatud_parool))
            connection.commit()
            print("Kasutaja registeeritud!")
        else:
            print("Ühenduse loomine ebaõnnestus.")
    except mysql.connector.Error as err:
        print(f"Viga andmete salvestamisel: {err}")
    finally:
        if connection:
            connection.close()

def logi_sisse():
    kasutaja = input("Sisesta enda kasutajanimi: ")
    parool = input("Sisesta enda parool: ")

    sisestatud_parool = hashlib.sha256(parool.encode()).hexdigest()

    try:
        connection = connect_mysql()
        if connection:
            cursor = connection.cursor()
            sql = "SELECT parool FROM kasutajad WHERE kasutajanimi = %s"
            cursor.execute(sql, (kasutaja,))
            result = cursor.fetchone()
            if result and result[0] == sisestatud_parool:
                print("Sisse logitud!")
            else:
                print("Sisse logimine ebaõnnestus!")
        else:
            print("Ühenduse loomine ebaõnnestus.")
    except mysql.connector.Error as err:
        print(f"Viga andmebaasist paringu tegemisel: {err}")
    finally:
        if connection:
            connection.close()

while True:
    print("\nVali tegevus:")
    print("1. Registreeri uus kasutaja")
    print("2. Logi sisse")
    print("3. Välju")
    valik = input("Sisesta valik (1/2/3): ")

    if valik == "1":
        uus_kasutaja()
    elif valik == "2":
        logi_sisse()
    elif valik == "3":
        break
    else:
        print("Vigane valik")