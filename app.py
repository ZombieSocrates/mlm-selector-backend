import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 

from models import ChideoEmployee, HostEngagement

app = Flask(__name__)
app.config.from_object(os.getenv("APP_CONFIG"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)


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
    '''No need to specify join fields because I defined the 
    relationship in models.py'''
    hosts = (
        db.session.query(
            ChideoEmployee.id,
            ChideoEmployee.name
        )
        .outerjoin(HostEngagement)
        #TODO: date filter to current year
        .filter(HostEngagement.id == None)
        .all()
    )
    return jsonify({
        "HostCount":len(hosts),
        "HostList": serialize_hosts(hosts)
        })


if __name__ == "__main__":
    app.run()
