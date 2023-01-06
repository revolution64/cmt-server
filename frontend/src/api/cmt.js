import axios from 'axios'

function isLocalHost(url) {
    return url.indexOf('localhost') !== -1 || url.indexOf('127.0.0.1') !== -1;
}

function getHost(url) {
    return isLocalHost(url) ? 'http://localhost:5002' : 'https://revolution64.pythonanywhere.com'
}

export const analyzeText = (text) => axios.post(getHost(window.location.host), {
    "text": text
});