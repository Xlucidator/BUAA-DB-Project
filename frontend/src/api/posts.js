import axios from "../axios";

export function getCurrentPage(token, index) {
    console.log("getCurrentPage: ", index)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('pageNum', index);
    return axios.post("/announcements", formData)
}

export function updatePostContent(token, id, content) {
    console.log("getCurrentPage: ", id)
    const formData = new FormData();
    formData.append('token', token);
    formData.append('id', id);
    formData.append('content', content);
    return axios.post("/announcements/update", formData)
}