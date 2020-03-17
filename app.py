import os

from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, and_ 

from models import ChideoEmployee, HostEngagement

app = Flask(__name__)
app.config.from_object(os.getenv("APP_CONFIG"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)


def most_recent_mlm_week():
    '''Contingent on this table being kept up to date. A missing week would 
    mess this up.

    Alternatively, hosting date could be passed from front end'''
    host_date = db.session.query(func.max(HostEngagement.week_of_hosting))
    return host_date.first()[0]


def serialize_hosts(query_all_result):
    parsed_hosts = []
    for host_info in query_all_result:
        parsed_hosts.append({"id": host_info[0], "name": host_info[1]})
    return parsed_hosts


@app.route("/status")
def status():
    return '''<h1>
    NOW WITNESS THE POWER OF THIS FULLY OPERATIONAL BATTLE STATION
    </h1>'''


@app.route("/getEligibleHosts", methods = ["GET"])
def get_eligible_hosts():
    '''Find every chideoer who hasnt hosted yet in the year of the
    next MLM'''
    last_mlm = most_recent_mlm_week()
    next_mlm = last_mlm + timedelta(days = 7)
    hosts = (
        db.session.query(
            ChideoEmployee.id,
            ChideoEmployee.name
        )
        .outerjoin(HostEngagement, and_(
            ChideoEmployee.id == HostEngagement.chideoer_id,  
            func.date_part("YEAR", HostEngagement.week_of_hosting) == next_mlm.year
            )
        )
        .filter(HostEngagement.id == None)
        .all()
    )
    return jsonify({
        "HostCount":len(hosts),
        "HostList": serialize_hosts(hosts),
        "LastHostWeek": datetime.strftime(last_mlm, "%Y-%m-%d"),
        "NextHostWeek": datetime.strftime(next_mlm, "%Y-%m-%d")
        })


if __name__ == "__main__":
    app.run()
