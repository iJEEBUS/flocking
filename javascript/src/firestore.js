import firebase from "@firebase/app";
import "@firebase/firestore";

const config = {
    apiKey: "AIzaSyCNtyCYpwKJ69l6_PC1BnIeWsQKVl7Vvk0",
    authDomain: "flocking-5edd4.firebaseapp.com",
    databaseURL: "https://flocking-5edd4.firebaseio.com",
    projectId: "flocking-5edd4",
    storageBucket: "",
    messagingSenderId: "17638056210",
    appId: "1:17638056210:web:e47cef4c9713ee57"
};

const app = firebase.initializeApp(config);
const firestore = firebase.firestore(app);

export default firestore;