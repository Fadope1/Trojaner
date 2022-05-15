from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///test.db', echo=True)
db_connection = engine.connect()

meta = MetaData()

client_table = Table(
   'client', meta,
   Column('id', Integer, primary_key=True),
   Column('ip', String),
   Column('port', Integer),
)
meta.create_all(engine)
