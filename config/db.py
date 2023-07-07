from sqlalchemy import create_engine, MetaData

#engine = create_engine("mysql+pymysql://root:@localhost:3306/news")
engine = create_engine("mysql+pymysql://uuxbcszkci1q50hq:HSWqLkRqGOKKTrC47Gj5@by3tkwb22zo3nffnstse-mysql.services.clever-cloud.com:3306/by3tkwb22zo3nffnstse")
meta = MetaData()
conn = engine.connect()