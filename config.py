"""
loads and stores mongodb instance for project wide access
"""


import mongo_loader


regalia22_db = mongo_loader.get_cluster0()

days = ["16", "20"]  # regalia'22 starts on 19th of may'22
