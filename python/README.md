'uploadData.py' is a sample program that assigns random values to placeholder variables, and uploads this data to the BruinBot Firebase project. The program's intention is to serve as a template for the BruinBot Controls team to use, to upload sensor data into Firebase.

----

Note: This program was run on Python 3.8.1.

----

To setup and run the code:

* Download the private key from Firebase and save the resulting JSON file as 'firebase_admin.json', and save this JSON file in the same directory as 'uploadData.py'
* Install 'firebase_admin' using pip
* Run 'uploadData.py' with Python
* You should be able to see updated values added to the Sensors collection on Cloud Firestore on the BruinBot Firebase project's Database tab
