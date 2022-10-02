import axios from "../axios";

export function login(username, password) {
    console.log(username, password)
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return axios.post("/index/POST/login", formData)
}

// export function getinfo() {
//     return axios.post("/POST/info")
// }