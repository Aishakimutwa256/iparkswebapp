//stroring csrf_token to variable
const CSRF_TOKEN = document.querySelector('[name=csrfmiddlewaretoken]').value;

//spiner initialization
const spinnerWrapper = document.querySelector("#spinner-wrapper");

//booking form handler const initializations
// const bookingsFormHandler = document.getElementById("bookings-details-form");
const bookButtons = document.querySelectorAll("[data-slot_id]");

//create account const initailizations
const createAccountForm = document.querySelector("#create-account-form");
const createAccountButton = document.querySelector("#create-account-button");


// login constant initaializations
const loginForm = document.querySelector("#login-form");
const loginButton = document.querySelector("#login-button");


//request urls constants
const logoutURL=`${window.location.protocol}//${window.location.host}` +'/useraccounts/logout/';
const bookingURL =window.location.href + 'bookslot/';
const createAccountURL=`${window.location.protocol}//${window.location.host}` +'/useraccounts/register/';
const loginURL=`${window.location.protocol}//${window.location.host}` +'/useraccounts/login/';
