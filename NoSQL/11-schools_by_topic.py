#!/usr/bin/env python3
"""Module that lists all schools with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return list of schools having a specific topic"""

    return mongo_collection.find({"topics": topic})
