#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by longqi on 4/21/15
"""
__author__ = 'longqi'

from cqlengine import columns
from cqlengine import Model


class ExampleModel(Model):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at = columns.DateTime()
    description = columns.Text(required=False)
