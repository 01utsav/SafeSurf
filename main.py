import utils, scraper, report, json
from flask import Flask,render_template, request
from flask import jsonify
from firebase import firebase
from firebase_admin import credentials, initialize_app, db
import json
firebase = firebase.FirebaseApplication("<YOUR_Firebase_Database_URL>", authentication=None)
# Initialize Firebase Admin SDK with service account credentials


# Path to the service account key file
SERVICE_ACCOUNT_KEY_PATH = "<YOUR_JSON_PATH>"
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)

initialize_app(cred, {
    'databaseURL': '<YOUR_Firebase_Database_URL>'
})

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return 'home'

@app.route("/genReport", methods=['GET'])
def genReport():

    id = request.args.get('id')
    url = request.args.get('url')

    try:
        web_html = utils.getHTML(url)
        qna = utils.divideIntoQnA(web_html)
        print(qna)
        output = report.generate_report(qna)
        print(output)
        db.reference('/privacy/' + id).update({'data': json.dumps(output), 'status': 'DONE'})
        return jsonify({'status': 'DONE', 'data': output})
    
    except:
        db.reference('/privacy/' + id).update({'status': 'ERROR'})
        return jsonify({'status': 'ERROR', 'message': 'error'})





@app.route("/api2/", methods=['GET'])
def scaperApi():
    #?url=
    url = request.args.get('url')
    #?id=
    id = request.args.get('id')
    try:
        output2 = scraper.scrap(url)
        # db.reference('/gdpr/' + id).update({'data': json.dumps(output2), 'status': 'DONE'})
        db.reference('/gdpr/' + id).update({'data': json.dumps(output2), 'status': 'DONE'})
        
        # Fetch data from Firebase based on the provided ID
        firebase_data = db.reference('/gdpr/' + id).get()

        if firebase_data:
            print(jsonify(firebase_data))
            return jsonify(firebase_data)
        else:
            return jsonify({'error': 'Data not found for the provided ID'})
    except:
        db.reference('/gdpr/' + id).update({'status': 'ERROR'})

    return "True"

if __name__ == '__main__':
    app.run(debug=True)