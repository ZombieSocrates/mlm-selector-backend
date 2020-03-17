import os
import time

from collections import namedtuple
from datetime import datetime
from dotenv import load_dotenv


from models import ChideoEmployee, HostEngagement, get_engine
from scrape_chideoers import chideo_employees_from_html


# Just FYI, I had to look this up after loading in the chideoer records based
# on my Google Calendar history
HostRow = namedtuple("HostRow", ["name","date", "emp_id"])
FOLKS_WHO_HOSTED = [
    HostRow(name = "Caralanay Cameron", date = "01/06/2020", emp_id = 3859),
    HostRow(name = "Tom Antony", date = "01/13/2020", emp_id = 31104),
    HostRow(name = "Jessica Randazza-Pade", date = "01/20/2020", emp_id = 31197),
    HostRow(name = "Peter Winter", date = "01/27/2020", emp_id = 25647),
    HostRow(name = "Ilan Brat", date = "02/03/2020", emp_id = 30934),
    HostRow(name = "Nate Tower", date = "02/10/2020", emp_id = 27391),
    HostRow(name = "Sam Becker", date = "02/17/2020", emp_id = 27962),
    HostRow(name = "Jennifer Riel", date = "02/24/2020", emp_id = 31808),
    HostRow(name = "Meredith Adams-Smart", date = "03/02/2020", emp_id = 3337),
    HostRow(name = "Chris Kucharczyk", date = "03/09/2020", emp_id = 27963),
    HostRow(name = "Jane Pak", date = "03/16/2020", emp_id = 31514),
    HostRow(name = "Amie Ninh",date = "03/23/2020", emp_id = 31843),
    HostRow(name = "Hitasha Bhatia", date = "03/30/2020", emp_id = 3480),
    HostRow(name = "Steve Schwall", date = "04/06/2020", emp_id = 99),
    HostRow(name = "Jason Chen", date = "04/13/2020", emp_id = 31006),
    HostRow(name = "James Zhou", date = "04/20/2020", emp_id = 30892),
]


def get_database_uri():
    load_dotenv()
    if os.getenv("ENV_NAME") == "DEVELOPMENT":
        return os.getenv("DEV_DB_URI")


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


def load_host_records(db_engine, host_records = FOLKS_WHO_HOSTED):
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
    db_engine = get_engine(db_uri, echo = False)
    load_chideoer_records(db_engine = db_engine)
    load_host_records(db_engine = db_engine)
    elapsed = time.perf_counter() - s
    print(f"{__file__} completed in {elapsed:0.2f} seconds")


if __name__ == "__main__":

    populate_database()




