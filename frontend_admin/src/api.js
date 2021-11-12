import axios from 'axios';
import { apiUrl } from '@/env';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async loginGetToken(username, password) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);
    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async testAuthToken(token) {
    return axios.post(
      `${apiUrl}/api/v1/login/test-token`,
      {},
      authHeaders(token)
    );
  },
  async getMe(token) {
    return axios.get(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  // Categories
  async getCategories(skip = 0, limit = 100) {
    const params = new URLSearchParams();
    params.append('skip', skip);
    params.append('limit', limit);
    return axios.get(`${apiUrl}/api/v1/categories`, params);
  },
  async getCategoryBySlug(slug) {
    return axios.get(`${apiUrl}/api/v1/categories/slug/${slug}`);
  },
  async createCategory(token, category) {
    return axios.post(
      `${apiUrl}/api/v1/categories`,
      JSON.stringify(category),
      authHeaders(token)
    );
  },
};
