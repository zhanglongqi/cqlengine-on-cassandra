#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by longqi on 4/21/15
"""
__author__ = 'longqi'

from cqlengine import columns
from cqlengine import Model


class StaffModel(Model):
    name = columns.Text(primary_key=True, default='Unknown')
    age = columns.Integer(index=True)
    hp = columns.Text(required=False)

# next, setup the connection to your cassandra server(s)...
from cqlengine import connection

# see http://datastax.github.io/python-driver/api/cassandra/cluster.html for options
# the list of hosts will be passed to create a Cluster() instance
connection.setup(['172.21.77.197'], "test", protocol_version=2)

# ...and create your CQL table
from cqlengine.management import sync_table

sync_table(StaffModel)

# now we can create some rows:
em1 = StaffModel.create(name='a', age=1, hp='hp1')
em2 = StaffModel.create(name='b', age=2, hp='hp1')
em3 = StaffModel.create(name='c', age=3, hp='hp1')
em4 = StaffModel.create(name='E', age=99, hp='hp1')
em5 = StaffModel.create(name='F', age=100, hp='hp1')

# and now we can run some queries against our table
StaffModel.objects.count()

q = StaffModel.objects(example_type=1)
q.count()

for instance in q:
    print(instance.name)

# here we are applying additional filtering to an existing query
# query objects are immutable, so calling filter returns a new
# query object
'''
>> > q2 = q.filter(example_id=em5.example_id)

>> > q2.count()
1
>> > for instance in q2:
    >> > print
instance.description
example5
'''