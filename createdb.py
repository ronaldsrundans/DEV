import sqlite3
# connection object
connection_obj = sqlite3.connect('catalog.db') 
# cursor object
cursor_obj = connection_obj.cursor() 
# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS CATALOG")
# Creating table
tableteam = """ CREATE TABLE CATALOG (
            ID INT NOT NULL,      
            NOSAUKUMS VARCHAR(255),
            APRAKSTS VARCHAR(255),
            ATBSTR VARCHAR(255),
            DATUMS VARCHAR(255),
            SAITE VARCHAR(255),
            FAILS VARCHAR(255),
            LASISANA VARCHAR(255),
            SVARIGUMS VARCHAR(255),
            KATEGORIJA VARCHAR(255),
            AKTIVS VARCHAR(255)
        ); """
cursor_obj.execute(tableteam)
# Close the connection
connection_obj.close()
