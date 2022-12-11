import axios from "../axios";

export function getCurrentPage(token, index) {
    console.log("getCurrentPage: ", index)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('page', index);
    return axios.get("/passage/passages/" + index + "/", formData)
}

export function updatePostContent(token, id, content) {
    console.log("getCurrentPage: ", id)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('id', id);
    formData.append('content', content);
    return axios.post("/announcements/update", formData)
}

export function newPost(token, content) {
    console.log("getCurrentPage: ", id)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('id', id);
    formData.append('content', content);
    return axios.post("/announcements/update", formData)
}