import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/date<br/>"
        f"/api/v1.0/prcp<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/measurement"
    )


@app.route("/api/v1.0/prcp")
def precipitation():
    """Return a list of all prcp data"""
    # Query all data
    results = session.query(Measurement.prcp,Measurement.date).all()

   

    return jsonify(all_prcp)


if __name__ == '__main__':
    app.run(debug=True)
