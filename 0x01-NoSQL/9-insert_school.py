#!/usr/bin/env python3
"""
Inserting a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection

    Args:
        mongo_collection: the mongoDB collection
        kwargs: the document
        return: the new document id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
