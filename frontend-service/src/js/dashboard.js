import { protectPage } from "./utils.js";
import { logout } from "./auth.js";

protectPage();

const token = localStorage.getItem("token");

if (token) {
    const payload = JSON.parse(atob(token.split('.')[1]));

    document.getElementById("userInfo").innerText =
        `Welcome ${payload.sub} | Role: ${payload.role}`;

    if (payload.role !== "admin") {
        document.getElementById("adminSection").style.display = "none";
    }
}

document.getElementById("logoutBtn").addEventListener("click", logout);