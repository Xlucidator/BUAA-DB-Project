import axios from "../axios";

export function login(username, password) {
    return axios.post("/POST/login",{username, password})
}

export function getinfo() {
    return axios.post("/POST/info")
}