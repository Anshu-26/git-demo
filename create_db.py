from sqlite3 import connect

db_name = 'results_db.sql'


con = connect(db_name)
sql_query = """CREATE TABLE 'records' (
  'location' varchar(100) DEFAULT NULL,
  'phrase' varchar(100) DEFAULT NULL,
  'letters' varchar(100) DEFAULT NULL,
  'results' varchar(100) DEFAULT NULL
)"""

con.execute(sql_query)

con.commit()
con.close()



