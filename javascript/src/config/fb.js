
import firebase from 'firebase'

const config = {
  //initialize config here
}

firebase.initializeApp(config);
firebase.firestore().settings({timestampsInSnapshots: true});

  export default firebase;
