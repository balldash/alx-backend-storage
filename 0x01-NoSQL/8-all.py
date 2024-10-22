#!/usr/bin/env python3
"""
List all documents using python
"""


def list_all(mongo_collection):
    """
    A function to list all documents in a collection.

    Args:
        mongo_collection: the collection to query
        return: the documents
    """
    return mongo_collection.find()
