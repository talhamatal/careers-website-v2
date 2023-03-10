from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine (db_connection_string,
                       connect_args ={
                         "ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                         }
                       })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    stmt = text("select * from jobs where id = :x")
    stmt =stmt.bindparams(x=id)
    result = conn.execute(stmt)
    rows = result.all()[0]
    if len(rows) == 0:
      return None
    else: 
      return (rows._asdict())
  
  #print ("type(result):", type(result))
  #result_all = result.all()
  #print("type(result_all):", type(result_all))
  #first_result = result_all[0]
  #print("type(first_result):", type(first_result))
  #print(first_result)
  #first_result_dict = first_result._asdict()
  #print("type(first_result_dict):", type(first_result_dict))
  #print(first_result_dict)