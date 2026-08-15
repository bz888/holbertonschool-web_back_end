#!/usr/bin/env python3
"""Module for listing all docs in MongoDB collection"""


def list_all(mongo_collection):
    """list all docs in collection"""

    return list(mongo_collection.find())
