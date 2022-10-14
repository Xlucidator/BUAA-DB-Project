import axios from "../axios";

export function login(username, password) {
    console.log(username, password)
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return axios.post("/login/login", formData)
}

export function register(username, password, pwConfirm) {
    console.log(username, password)
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('pwConfirm', pwConfirm);
    return axios.post("/login/enroll", formData)
}

export function revoke(token, password) {
    console.log(token, password)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('password', password);
    return axios.post("/login/revoke", formData)
}

export function getInfo(token) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    return axios.post("/login/info", formData)
}

export function getApplyForm(token) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    return axios.post("/index/POST/getApplyForm", formData)
}

export function getUserForm(token) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    return axios.post("/index/POST/getUserForm", formData)
}

export function editApplyForm(token, username, permission) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('username', username);
    formData.append('permission', permission);
    return axios.post("/index/POST/editApplyForm", formData)
}

export function rejectApply(token, username) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('username', username);
    return axios.post("index/application/reject", formData)
}

export function acceptApply(token, username) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('username', username);
    return axios.post("index/application/consent", formData)
}

export function addUser(token, username) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('username', username);
    return axios.post("/index/POST/addUser", formData)
}
