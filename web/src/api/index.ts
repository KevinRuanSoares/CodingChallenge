import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'https://api.codechallenge.kevinsoares.com.br',
});

export default axiosInstance;
