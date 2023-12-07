// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-app.js";
//import { getDatabase } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-database.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-auth.js";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDMSjkpGZ2qgXVTmF-kO8IhIB8znXuWmGk",
  authDomain: "adsite-50002.firebaseapp.com",
  databaseURL: "https://adsite-50002-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "adsite-50002",
  storageBucket: "adsite-50002.appspot.com",
  messagingSenderId: "200884782204",
  appId: "1:200884782204:web:1a9f3d3c650277351c35f9",
  measurementId: "G-HWCEQ20CFY"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
//const database = firebase.database()

const auth = getAuth();
const singup = document.getElementById("saveData");
const login = document.getElementById("logData");
const singv = document.getElementById("singup-v");
const logv = document.getElementById("log-v");
const sinbox = document.getElementById("sin-box");
const loginbox = document.getElementById("login-box");


singup.addEventListener('click',(e) => {
 var email = document.getElementById('email').value;
 var password = document.getElementById('password').value;

   createUserWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    const user = userCredential.user;
    alert('done')
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
  });
});



singv.addEventListener('click',(e) =>{
  window.location.href = 'login.html';
})
logv.addEventListener('click',(e) =>{
  window.location.href = 'singup.html';
})