import axios from 'axios';
 const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';
export const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(
  (response) =>response,
  async(error)=>{
    const originalRequest = error.config;
    if (error.response?.status === 401 && !originalRequest._retry){
      originalRequest._retry = true;
      try{
        await apiClient.post('/users/refresh/');
        return apiClient(originalRequest);
      }catch(refresError){
        //Rediriger vers login si refresh echoue
        if(typeof window !== 'undefined') {
          window.location.href = '/auth/login';
        }
        return Promise.reject(refresError);
      }
    }
    return Promise.reject(error);
  }
);
