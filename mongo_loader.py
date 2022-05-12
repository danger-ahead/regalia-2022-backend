import env_config


def get_cluster0():

    from pymongo import MongoClient

    CONNECTION_STRING = (
        "mongodb+srv://"
        + env_config.username
        + ":"
        + env_config.password
        + "@"
        + env_config.cluster_name
        + ".mongodb.net/"
        + env_config.database
        + "?retryWrites=true&w=majority"
    )

    from pymongo import MongoClient

    # regalia22 project object
    client = MongoClient(CONNECTION_STRING)

    # regalia22 database object
    db = client["regalia22"]

    return db


if __name__ == "__main__":
    dbname = get_cluster0()
