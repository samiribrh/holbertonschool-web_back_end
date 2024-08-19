#!/usr/bin/env python3
"""Module for insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """Function for inserting new schools"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
