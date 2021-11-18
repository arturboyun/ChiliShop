import axios from 'axios';
import { apiUrl } from '@/env';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

const auth = {
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
};

const category = {
  async getCategories(skip = 0, limit = 100) {
    const params = new URLSearchParams();
    params.append('skip', String(skip));
    params.append('limit', String(limit));
    return axios.get(`${apiUrl}/api/v1/categories`, { params });
  },
  async getCategoryBySlug(slug) {
    return axios.get(`${apiUrl}/api/v1/categories/slug/${slug}`);
  },
  async getCategoryById(id) {
    return axios.get(`${apiUrl}/api/v1/categories/${id}`);
  },
  async createCategory(token, category) {
    return axios.post(
      `${apiUrl}/api/v1/categories`,
      JSON.stringify(category),
      authHeaders(token)
    );
  },
  async updateCategory(token, { id, form }) {
    return axios.put(
      `${apiUrl}/api/v1/categories/${id}`,
      JSON.stringify(form),
      authHeaders(token)
    );
  },
  async deleteCategory(token, categoryId) {
    return axios.delete(
      `${apiUrl}/api/v1/categories/${categoryId}`,
      authHeaders(token)
    );
  },
};

const product = {
  async getProducts(skip = 0, limit = 100) {
    const params = new URLSearchParams();
    params.append('skip', String(skip));
    params.append('limit', String(limit));
    return axios.get(`${apiUrl}/api/v1/products/`, { params });
  },
  async getProductBySlug(slug) {
    return axios.get(`${apiUrl}/api/v1/products/slug/${slug}`);
  },
  async getProductById(id) {
    return axios.get(`${apiUrl}/api/v1/c/${id}`);
  },
  async createProduct(token, payload) {
    return axios.post(
      `${apiUrl}/api/v1/products/`,
      JSON.stringify(payload),
      authHeaders(token)
    );
  },
  async updateProduct(token, { id, form }) {
    return axios.put(
      `${apiUrl}/api/v1/products/${id}`,
      JSON.stringify(form),
      authHeaders(token)
    );
  },
  async deleteProduct(token, id) {
    return axios.delete(`${apiUrl}/api/v1/products/${id}`, authHeaders(token));
  },
};

export const api = {
  auth,
  category,
  product,
};
