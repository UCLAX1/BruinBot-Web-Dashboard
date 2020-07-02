import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import time


cred = credentials.Certificate('./firebase_admin.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def updateData(sensor_name, data):

    doc_ref = db.collection(u'Sensors').document(sensor_name)
    doc = doc_ref.get()
    upload_data = [data]

    if doc.exists:
        doc_ref = db.collection(u'Sensors').document(sensor_name)
        values = doc.to_dict()['values']

        values.append(data)
        upload_data = values

    doc_ref.set({
        u'value': data['value'],
        u'values': upload_data
    })


while True:

    count = random.randint(1,10)
    data = {
        'timestamp': time.asctime(),
        'value': count
    }

    updateData("Long", data)
    updateData("Lat", data)
    updateData("SIV", data)
    updateData("X", data)
    updateData("Y", data)
    updateData("Z", data)
    updateData("Sensor1", data)
    updateData("Sensor2", data)
    updateData("Sensor3", data)
    updateData("Sensor4", data)
