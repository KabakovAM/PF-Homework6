import sqlalchemy
import databases

DATABASE_URL = "sqlite:///Homework6/mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

goods = sqlalchemy.Table(
    'goods',
    metadata,
    sqlalchemy.Column('g_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(32)),
    sqlalchemy.Column('description', sqlalchemy.String(256)),
    sqlalchemy.Column('price', sqlalchemy.Float)
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('o_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('u_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.u_id')),
    sqlalchemy.Column('data', sqlalchemy.String(10)),
    sqlalchemy.Column('status', sqlalchemy.String(16))
)

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('u_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(16)),
    sqlalchemy.Column('sur_name', sqlalchemy.String(16)),
    sqlalchemy.Column('email', sqlalchemy.String(16)),
    sqlalchemy.Column('password', sqlalchemy.String(16))
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)

metadata.create_all(engine)
