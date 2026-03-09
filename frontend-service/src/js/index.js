import { login } from "./auth.js";
import { apiRequest } from "./api.js";

// Elements
const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");

const showLoginBtn = document.getElementById("showLogin");
const showRegisterBtn = document.getElementById("showRegister");

const loginBtn = document.getElementById("loginBtn");
const registerBtn = document.getElementById("registerBtn");


// Toggle Forms
showLoginBtn.addEventListener("click", () => {
    loginForm.classList.remove("hidden");
    registerForm.classList.add("hidden");
    showLoginBtn.classList.add("active");
    showRegisterBtn.classList.remove("active");
});

showRegisterBtn.addEventListener("click", () => {
    registerForm.classList.remove("hidden");
    loginForm.classList.add("hidden");
    showRegisterBtn.classList.add("active");
    showLoginBtn.classList.remove("active");
});


// Login Button
loginBtn.addEventListener("click", async () => {

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    try {
        await login(email, password);
    } catch (err) {
        console.log(err);
    }
});


// Register Button
registerBtn.addEventListener("click", async () => {

    const email = document.getElementById("registerEmail").value;
    const password = document.getElementById("registerPassword").value;

    try {
        await apiRequest("/auth/register", "POST", { email, password });
        alert("Registration successful. Please login.");
        showLoginBtn.click();
    } catch (err) {
        console.log(err);
    }
});