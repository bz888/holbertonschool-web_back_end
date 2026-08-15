#!/usr/bin/env python3
"""Module for changing all topics of a doc based on name"""


def update_topics(mongo_collection, name, topics):
    """change all topics of a doc"""

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
