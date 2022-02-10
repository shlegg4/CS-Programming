import sqlite3

def CreateFilmTble():
    with sqlite3.connect("library.db") as db:
        cursor = db.cursor()
        cursor.execute("""
    Create TABLE Film(
    BorrowerID integer,
    BorrowerName text,
    BorrowerEmail text,
    Primary Key(BorrowerID));
    """)
        db.commit

def InsertRecord():
    with sqlite3.connect("library.db") as db:
        cursor = db.cursor()
        sql = """insert into Film (BorrowerName,BorrowerEmail)
        values("Sam","Sam@ryde")"""
        cursor.execute(sql)
        db.commit()
    
CreateFilmTble()
InsertRecord()