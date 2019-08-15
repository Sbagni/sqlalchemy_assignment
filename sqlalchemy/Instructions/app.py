import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,inspect, func
from sqlalchemy import Date, cast

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
Last_year_date = dt.date(2017,8,23)-dt.timedelta(days =365)
today = '2017-08-23'


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return ("Welcome:  <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/date/<start>/<end><br/>"
        )
@app.route('/api/v1.0/precipitation')
def prcptn():
     session = Session(engine)
     prcptns = session.query( Measurement.date, Measurement.prcp).filter(Station.station == Measurement.station).all()
     lst_prcp=[]
     for prcptn in prcptns:
        prcptn_dict1 = {}
        prcptn_dict1["date"] = prcptn[0]
        prcptn_dict1['prcp'] = prcptn[1]
        lst_prcp.append(prcptn_dict1)
        return jsonify(lst_prcp)
@app.route('/api/v1.0/stations')
def station():
    session = Session(engine)
    return jsonify(session.query(Station.station).all())
@app.route('/api/v1.0/tobs')   
def tobs():
    session = Session(engine)
    tobs = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date>=Last_year_date).filter(Measurement.date<=today).filter(Station.station == Measurement.station).filter(Station.station == 'USC00519281').all()
    lst_tobs=[]
    for tob in tobs:
        tobs_dict = {}
        tobs_dict["Date"] = tob[0]
        tobs_dict['Temp'] = tob[1]
        lst_tobs.append(tobs_dict)
        return jsonify(lst_tobs)
@app.route ('/api/v1.0/<start>')
def strt(start):
    session = Session(engine)
    s = jsonify(session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>=start).all()
    return s
@app.route("/api/v1.0/date/<start_date>/<end_date>")
def st_end(start_date = None,end_date = None):

        session = Session(engine)
        st_end = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>=start_date).filter(Measurement.end_date<=end).all()
        return jsonify(st_end) 

    
    
if __name__ == '__main__':
    app.run(debug=True)









        
    
    
    
    
 
