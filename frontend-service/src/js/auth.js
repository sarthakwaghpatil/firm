import { apiRequest } from "./api.js";

export async function login(email, password) {
    const data = await apiRequest("/auth/login", "POST", { email, password });

    localStorage.setItem("token", data.access_token);

    window.location.href = "dashboard.html";
}

export function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}