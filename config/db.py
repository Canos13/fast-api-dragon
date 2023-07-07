from sqlalchemy import create_engine, MetaData

#engine = create_engine("mysql+pymysql://root:@localhost:3306/news")
engine = create_engine("mysql+pymysql://rx49pld6m8rwe7z2qe83:pscale_pw_8dJeUKWkuFUJVL3LK0I9yimZE9leMe3HQmVKZfdfxms@aws.connect.psdb.cloud:3306/news")
meta = MetaData()
conn = engine.connect()