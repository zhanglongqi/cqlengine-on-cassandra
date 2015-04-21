__author__ = 'longqi'
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
import random
import string


def get_random_string():
    return ''.join(random.sample(string.letters, 10))


ap = PlainTextAuthProvider(username='longqi', password='zhang123')
cluster = Cluster(['155.69.214.102', '172.21.77.197'], auth_provider=ap)
session = cluster.connect()
session.set_keyspace('test')
session.default_timeout = 20

rows = session.execute('select * from t1 LIMIT 10')
for row in rows:
    print(row.name, row.age)

res = session.execute(
    """
    INSERT INTO t1 (name, age)
    VALUES (%s, %s)
    """,
    (get_random_string(), random.randint(1, 200))
)
