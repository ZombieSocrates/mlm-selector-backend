import os
import time


from dotenv import load_dotenv


from models import ChideoEmployee, HostEngagements, get_engine
from scrape_chideoers import chideo_employees_from_html


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


def load_host_records():
	pass


def populate_database():
	db_uri = get_database_uri()
	db_engine = get_engine(db_uri, echo = False)
	load_chideoer_records(db_engine = db_engine)


if __name__ == "__main__":

	populate_database()




