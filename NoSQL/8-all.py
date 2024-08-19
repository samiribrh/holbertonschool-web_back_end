#!/usr/bin/env python3
"""Module for list_all function"""
import pymongo


def list_all(mongo_collection):
    """ List all elements in a collection """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
