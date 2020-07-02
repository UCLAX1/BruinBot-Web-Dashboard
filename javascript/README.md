The Javascript source code constructs a web dashboard for the BruinBot project. The dashboard has three features: controls, sensor data, and data log. For controls, users can input data to tell the robot how much to move forward/backward and turn left/right. For sensor data, the sensor values on the robot will be updated on the dashboard in real time. And for the data log, users can download a CSV file that contains the entire history of sensor data that is stored in Firebase.

----

To setup and run the code:

* In src/config/fb.js, update 'config' with the web app's Firebase configuration, found on the BruinBot Firebase project
* Run 'npm install' in this directory
* Run 'npm audit fix' in this directory
* Run 'npm start' in this directory
* You should see a browser window launch displaying the web app
