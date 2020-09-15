import psycopg2
from psycopg2.extras import DictCursor, NamedTupleCursor
COL_NAME = 'first_name'

class Actor:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def get_actors(self, table_name, lines=100):
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user,
                                     password=self.password, host=self.host)
        self.cursor = self.conn.cursor(cursor_factory=NamedTupleCursor)
        self.cursor.execute(f'select * from {table_name}')
        self.records = self.cursor.fetchmany(size=lines)
        self.cursor.close()
        self.conn.close()
        return self.records


act = Actor('sql_mastery', 'cobra', 'ujytdj', 'localhost')

for i in act.get_actors('actor', 2):
    print(i.actor_id, i.first_name, i.last_name)

