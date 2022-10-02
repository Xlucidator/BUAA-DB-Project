import axios from "axios";

const service = axios.create({
    baseURL: '/api/',
});

export default service