#!/usr/bin/env python3
"""
Update documents
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all the topics of a school document

    Args:
        mongo_collection: the collection
        name: the name of the topic
        topics: the topics to update
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
