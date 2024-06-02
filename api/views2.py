from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

from flask import (
    Blueprint,
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

import joblib
import models_loader, input_preprocessor, agregate_columns
from datetime import datetime
import pandas as pd

total_trip_model = models_loader.load_total_trip_model()
duration_trip_model = models_loader.load_duration_trip_model()

app = Flask(__name__)

class TaxiForm(FlaskForm):
    pickUpDateTime = StringField('Pick Up DateTime', validators=[DataRequired()])
    passengersNumber = IntegerField('Number of Passengers', validators=[DataRequired()])
    pickUpId = IntegerField('Pick Up Location ID', validators=[DataRequired()])
    dropOffId = IntegerField('Drop Off Location ID', validators=[DataRequired()])
    paymentMethodId = IntegerField('Payment Method ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

router = Blueprint("app_router", __name__, template_folder="templates")

@router.route('/', methods=['GET', 'POST'])

def index():
    form = TaxiForm()
    if form.validate_on_submit():
        data = {}
        data["tpep_pickup_datetime"] = datetime.strptime(form.pickUpDateTime.data, "%Y-%m-%d %H:%M:%S")
        data["passenger_count"] = form.passengersNumber.data
        data["PULocationID"] = form.pickUpId.data
        data["DOLocationID"] = form.dropOffId.data
        # Aquí puedes agregar los valores predeterminados para las otras columnas

        df = pd.DataFrame(data, index=[0])
        #df = agregate_columns.agregate_columns_to_input(df)
        #column_order = ['PULocationID', 'DOLocationID', 'mta_tax','airport_fee','pickup_year','pickup_day','pickup_day_of_week','pickup_hour','pickup_minute','average_speed_mph']
        #df = df[column_order]
        df = input_preprocessor.preprocess_input_data(df)

        results_total = total_trip_model.predict(df)
        results_duration = duration_trip_model.predict(df)

        return render_template('results.html', total=results_total[0], duration=results_duration[0])

    return render_template('index.html', form=form)