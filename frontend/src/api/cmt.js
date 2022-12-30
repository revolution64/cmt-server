import axios from 'axios'

export const analyzeText = (text) => axios.post(`http://localhost:5000`, {
    "text": text
});