import axios from "axios";

const httpClient = axios.create({
    baseURL: "http://localhost:8000/api/v1",
    headers: {
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "application/json"
    }
});

export const getRequest = async (path: string) => {
    try {
        const response = await httpClient.get(path);
        if (response && response.data) {
            return response.data;
        }
    } catch(error: any) {
        return error;
    }
}

export const postRequest = async (path: string, data: any) => {
    try {
        const response = await httpClient.post(path, data);
        if (response && response.data) {
            return response.data;
        }
    } catch(error: any) {
        return error;
    }
}