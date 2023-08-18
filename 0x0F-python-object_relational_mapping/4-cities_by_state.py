#!/usr/bin/python3
"""
    select state module
"""


def main():
    """entry function"""
    import MySQLdb
    from sys import argv

    try:
        mysql = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                password=argv[2],
                db=argv[3]
                )
        c = mysql.cursor()
        c.execute(
                "SELECT c.id, c.name, s.name \
                FROM cities c \
                JOIN states s ON s.id = c.state_id \
                ORDER BY c.id"
                )

        for state in c.fetchall():
            print(state)

    except Exception as e:
        print("Error: ", e)
        return


if __name__ == "__main__":
    main()
