import os
import time

from collections import namedtuple
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles


from host_records import TEST_DB_HOSTS, DEV_DB_HOSTS
from models import ChideoEmployee, HostEngagement, get_engine
from scrape_chideoers import chideo_employees_from_html

# https://stackoverflow.com/questions/38678336/sqlalchemy-how-to-implement-drop-table-cascade
@compiles(DropTable, "postgresql")
def _compile_drop_table(element, compiler, **kwargs):
    return compiler.visit_drop_table(element) + " CASCADE"


def get_database_uri():
    load_dotenv()
    if os.getenv("ENV_NAME") == "DEVELOPMENT":
        return os.getenv("DEV_DB_URI")
    return os.getenv("TEST_DB_URI")


def get_host_records():
    if os.getenv("ENV_NAME") == "DEVELOPMENT":
        return DEV_DB_HOSTS
    return TEST_DB_HOSTS


def load_chideoer_records(db_engine):
    if ChideoEmployee.__table__.exists(db_engine):
        print(f"Dropping table {ChideoEmployee.__tablename__}...")
        ChideoEmployee.__table__.drop(db_engine)

    if not ChideoEmployee.__table__.exists(db_engine):
        print(f"Creating table {ChideoEmployee.__tablename__}...")
        ChideoEmployee.__table__.create(db_engine)

    print("Loading ChIDEO employees...")
    to_load = chideo_employees_from_html()
    db_engine.execute(ChideoEmployee.__table__.insert(), to_load)
    print(f"Just inserted {len(to_load)} ChIDEO employees...")
    print("Done!")


def load_host_records(db_engine, host_records):
    if HostEngagement.__table__.exists(db_engine):
        print(f"Dropping table {HostEngagement.__tablename__}...")
        HostEngagement.__table__.drop(db_engine)

    if not HostEngagement.__table__.exists(db_engine):
        print(f"Creating table {HostEngagement.__tablename__}...")
        HostEngagement.__table__.create(db_engine)

    print("Loading Past MLM Hosts...")
    to_load = []
    for record in host_records:
        record_week = datetime.strptime(record.date, "%m/%d/%Y")
        to_load.append({
            "chideoer_id": record.emp_id, 
            "week_of_hosting": record_week
            })
    db_engine.execute(HostEngagement.__table__.insert(), to_load)
    print(f"Just inserted {len(to_load)} MLM Host Slots...")
    print("Done!")


def populate_database():
    s = time.perf_counter()
    db_uri = get_database_uri()
    past_hosts = get_host_records()
    db_engine = get_engine(db_uri, echo = False)
    load_chideoer_records(db_engine = db_engine)
    load_host_records(db_engine = db_engine, host_records = past_hosts)
    elapsed = time.perf_counter() - s
    print(f"{__file__} completed in {elapsed:0.2f} seconds")


if __name__ == "__main__":

    populate_database()




