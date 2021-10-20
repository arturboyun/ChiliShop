import axios from 'axios';
import { apiUrl } from '@/env';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`
    }
  }
}

export const api = {
  async logInGetToken(username, password) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token) {
    return axios.get(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token, data) {
    return axios.put(`${apiUrl}/api/v1/users/me`, data, authHeaders(token));
  },
  async getUsers(token) {
    return axios.get(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async updateUser(token, userId, data) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token, data) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async getCategories(skip = 0, limit = 100) {
    return await axios.get(`${apiUrl}/api/v1/categories/?skip=${skip}&limit=${limit}`);
  },
  async getCategory(id) {
    return await axios.get(`${apiUrl}/api/v1/categories/${id}`);
  },
  async getCategoryBySlug(slug) {
    return await axios.get(`${apiUrl}/api/v1/categories/slug/${slug}`);
  },
  async createCategory(token, data) {
    return await axios.post(`${apiUrl}/api/v1/categories`, data, authHeaders(token));
  },
  async deleteCategory(token, id) {
    return await axios.delete(`${apiUrl}/api/v1/categories/${id}`, authHeaders(token));
  },

  // Products
  async getProductBySlug(slug) {
    return await axios.get(`${apiUrl}/api/v1/products/slug/${slug}`);
  },
  async getProductsByCategoryID(id, skip = 0, limit = 100) {
    return await axios.get(`${apiUrl}/api/v1/products/category/${id}?skip=${skip}&limit=${limit}`);
  },
  async getProductsByCategorySlug(slug, skip = 0, limit = 100) {
    return await axios.get(`${apiUrl}/api/v1/products/category/slug/${slug}?skip=${skip}&limit=${limit}`);
  },
}
