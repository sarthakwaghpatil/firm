import { BASE_URL } from "./config.js";

export async function apiRequest(endpoint, method="GET", body=null) {

    const loader = document.getElementById("loader");
    const errorDiv = document.getElementById("errorMessage");

    if (loader) loader.style.display = "block";
    if (errorDiv) errorDiv.innerText = "";

    try {
        const token = localStorage.getItem("token");

        const response = await fetch(`${BASE_URL}${endpoint}`, {
            method,
            headers: {
                "Content-Type": "application/json",
                "Authorization": token ? `Bearer ${token}` : ""
            },
            body: body ? JSON.stringify(body) : null
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong");
        }

        return data;

    } catch (error) {
        if (errorDiv) errorDiv.innerText = error.message;
        throw error;
    } finally {
        if (loader) loader.style.display = "none";
    }
}