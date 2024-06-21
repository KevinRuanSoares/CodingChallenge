import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'https://api.codechallenge.kevinsoares.com.br',
    headers: {
        'Content-Type': 'application/json',
    },
});

export default axiosInstance;
