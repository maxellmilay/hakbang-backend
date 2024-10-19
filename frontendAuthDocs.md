```javascript
import axios from "axios";

const API_URL = "http://your-backend-url/api/";

const setAuthToken = (token) => {
    if (token) {
        axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    } else {
        delete axios.defaults.headers.common["Authorization"];
    }
};

export const register = async (userData) => {
    try {
        const response = await axios.post(`${API_URL}register/`, userData);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const login = async (credentials) => {
    try {
        const response = await axios.post(`${API_URL}login/`, credentials);
        const { access, refresh, user } = response.data;
        localStorage.setItem("access_token", access);
        localStorage.setItem("refresh_token", refresh);
        setAuthToken(access);
        return user;
    } catch (error) {
        throw error.response.data;
    }
};

export const logout = async () => {
    try {
        await axios.post(`${API_URL}logout/`);
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        setAuthToken(null);
    } catch (error) {
        console.error("Logout error:", error);
    }
};

export const getUserProfile = async () => {
    try {
        const response = await axios.get(`${API_URL}profile/`);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

// Interceptor to handle token refresh
axios.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
                const refreshToken = localStorage.getItem("refresh_token");
                const response = await axios.post(`${API_URL}token/refresh/`, {
                    refresh: refreshToken,
                });
                const { access } = response.data;
                localStorage.setItem("access_token", access);
                setAuthToken(access);
                originalRequest.headers["Authorization"] = `Bearer ${access}`;
                return axios(originalRequest);
            } catch (refreshError) {
                // If refresh fails, logout the user
                logout();
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);

// Initialize auth token from localStorage
const token = localStorage.getItem("access_token");
setAuthToken(token);
```
