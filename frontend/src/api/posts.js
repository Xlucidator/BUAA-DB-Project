import axios from "../axios";
import {jsonToFormData} from "./manager";

export function getCurrentPage(token, index) {
    console.log("getCurrentPage: ", index)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('page', index);
    return axios.get("/passage/passages/" + index + "/", formData)
}

export function getSinglePage(token, idx) {
    console.log("getCurrentPage: ", idx)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('PId', idx);
    return axios.get("/passage/passage/" + idx + "/", formData)
}

export function updatePostContent(token, id, content) {
    console.log("updatePostContent: ", id, content)

    return axios.put("/passage/passage/" + id + "/", content)
}

export function newPost(token, content) {
    console.log("newPost: ", content)
    let jsonData = content._rawValue
    console.log("jsonData: ", jsonData)
    const formData = jsonToFormData(jsonData)
    return axios.post("/passage/passages/", formData)
}