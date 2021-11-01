import os
import shutil
import sqlite3

def get_build_query_from_file(filename: str) -> str:
    """
    Load .sql query that rebuilds the DB snapshot
    """
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        filename
    )
    if os.path.exists(path):
        with open(path, "r") as fin:
            return fin.read()
    else:
        raise FileExistsError("File does not exist: ", path)


def build_testdb_snapshot(db_url: str, sql_filename: str) -> None:
    """
    Rebuild *.sqlite3 database from *.sql file
    """
    build_string = get_build_query_from_file(sql_filename)
    with sqlite3.connect(db_url) as conn:
        conn.executescript(build_string)

def delete_testdb_snapshot(db_path: str):
    """
    Deletes DB snapshot
    """
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        db_path
    )
    if os.path.exists(path):
        os.remove(path)


if __name__ == "__main__":
    testdata_dir = "data"
    db_sql_path = os.path.join(testdata_dir, "build_matching_testdb.sql")
    db_path = os.path.join(testdata_dir, "built_db.sqlite3")
    
    delete_testdb_snapshot(db_path)
    build_testdb_snapshot(db_path, db_sql_path)
