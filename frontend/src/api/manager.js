import axios from "../axios";

export function login(username, password) {
    console.log(username, password)
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return axios.post("/index/POST/login", formData)
}

export function register(username, password, pwConfirm) {
    console.log(username, password)
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('pwConfirm', pwConfirm);
    return axios.post("/index/POST/enroll", formData)
}

export function revoke(username, password) {
    console.log(username, password)
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return axios.post("/index/POST/revoke", formData)
}

export function getInfo(token) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    return axios.post("/index/POST/info", formData)
}

export function logout() {
    console.log("logging out")
    return axios.post("/index/POST/logout")
}
