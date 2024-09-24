import axios from 'axios';

const stage = {
    development: {
        baseURL: 'http://localhost:3000',
    },
    production: {
        baseURL: 'https://api.codechallenge.kevinsoares.com.br',
    },
};

const axiosInstance = axios.create({
    baseURL: stage.production.baseURL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default axiosInstance;
