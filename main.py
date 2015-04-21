#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by longqi on 4/21/15
"""
__author__ = 'longqi'

from cqlengine import columns
from cqlengine import Model


class staff(Model):
    name = columns.Text(primary_key=True, default='Unknown')
    age = columns.Integer(index=True)
    hp = columns.Text(required=False)

# next, setup the connection to your cassandra server(s)...
from cqlengine import connection
from cassandra.auth import PlainTextAuthProvider

# see http://datastax.github.io/python-driver/api/cassandra/cluster.html for options
# the list of hosts will be passed to create a Cluster() instance
ap = PlainTextAuthProvider(username='lq', password='lq')

connection.setup(['172.21.77.197'], "test", auth_provider=ap)

# ...and create your CQL table

# sync_table(StaffModel)

# now we can create some rows:
em1 = staff.create(name='a', age=1, hp='hp1')
em2 = staff.create(name='b', age=2, hp='hp1')
em3 = staff.create(name='c', age=3, hp='hp1')
em4 = staff.create(name='E', age=99, hp='hp1')
em5 = staff.create(name='F', age=100, hp='hp1')

# and now we can run some queries against our table
print('we have records: ', staff.objects.count())

q = staff.objects(name='a')
q.count()

for instance in q:
    print(instance.name, instance.age, instance.hp)

# here we are applying additional filtering to an existing query
# query objects are immutable, so calling filter returns a new
# query object
'''
q2 = q.filter(age=2)

print(q2.count())

for instance in q2:
    print(instance.name, instance.age, instance.hp)
'''
