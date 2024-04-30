import axios from 'axios';

export default function () {
    axios.defaults.baseURL = process.env.NUXT_ENV_API_URL;
}
