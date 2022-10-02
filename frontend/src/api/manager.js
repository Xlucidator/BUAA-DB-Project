import axios from "../axios";

export function login(username, password) {
    console.log(username, password)
    return axios.post("/login-post/", {username, password})
}

// export function getinfo() {
//     return axios.post("/POST/info")
// }