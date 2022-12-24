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

export function deleteSinglePage(token, idx) {
    console.log("getCurrentPage: ", idx)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('PId', idx);
    return axios.delete("/passage/passage/" + idx + "/", formData)
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

export function insertReply(token, PId, Content, CodeName) {
    console.log("insertReply ", PId, Content, CodeName)
    const formData = new FormData();
    formData.append('AttachedPId', PId);
    formData.append('Content', Content);
    formData.append('Replier', CodeName);
    return axios.post("/reply/", formData)
}

export function getReplyFromPassage(token, PId) {
    console.log("getReplyFromPassage: ", PId)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('PId', PId);
    return axios.get("/passage/reply/" + PId + "/", formData)
}