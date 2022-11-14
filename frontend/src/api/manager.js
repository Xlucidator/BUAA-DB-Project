import axios from "../axios";
import {getToken} from "../composable/auth";

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
    formData.append('password', password);
    return axios.post("/login/revoke/", formData)
}

export function getInfo() {
    console.log("getInfo")
    return axios.get("/index/user/@self/")
}

export function getApplyForm() {
    console.log("getApplyForm")
    return axios.get("index/application/")
}

export function getUserForm() {
    console.log("getUserForm")
    return axios.get("index/user/")
}

export function editApplyForm(row) {
    console.log("editApplyForm")
    return axios.put("/index/application/" + row['CodeName'] + "/")
}

export function rejectApply(row) {
    console.log("rejectApply")
    return axios.delete("index/application/" + row['CodeName'] + "/")
}

export function acceptApply(row) {
    console.log("acceptApply")
    return axios.post("index/application/" + row['CodeName'] + "/")
}