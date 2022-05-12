"""
loads and stores mongodb instance for project wide access
"""


import mongo_loader


regalia22_db = mongo_loader.get_cluster0()
