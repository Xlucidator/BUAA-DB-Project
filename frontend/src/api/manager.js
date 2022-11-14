import axios from "../axios";

export function jsonToFormData(config) {
    const formData = new FormData();
    //循环传入的值转换formData
    Object.keys(config).forEach((key) => {
        formData.append(key, config[key]);
    })
    return formData;
}

export function login(username, password) {
    console.log("login: ", username, password)
    const formData = new FormData();
    formData.append('CodeName', username);
    formData.append('Password', password);
    return axios.post("/login/login/", formData)
}

export function register(form) {
    console.log("register", form)
    const formData = jsonToFormData(form)
    return axios.post("/login/enroll/", formData)
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
    return axios.post("/index/user/GET/user/", formData)
}

export function getApplyForm(token) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    return axios.post("index/application/GET/", formData)
}

export function getUserForm(token) {
    console.log(token)
    const formData = new FormData();
    formData.append('token', token);
    return axios.post("index/user/GET/users/", formData)
}

export function editApplyForm(token, row) {
    console.log(token)
    row['token'] = token
    const formData = jsonToFormData(row)
    return axios.post("/index/application/PUT/application/", formData)
}

export function rejectApply(token, row) {
    console.log(token)
    row['token'] = token
    const formData = jsonToFormData(row)
    return axios.post("index/application/reject/", formData)
}

export function acceptApply(token, row) {
    console.log(token)
    row['token'] = token
    const formData = jsonToFormData(row)
    return axios.post("index/application/consent/", formData)
}

export function addUser(token, row) {
    console.log(token)
    row['token'] = token
    const formData = jsonToFormData(row)
    return axios.post("/index/POST/addUser/", formData)
}
