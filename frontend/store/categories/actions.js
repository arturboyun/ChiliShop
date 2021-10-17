import { api } from '@/api';

const actions = {
  async getCategories(context, { skip = 0, limit = 999 }) {
    const response = await api.getCategories(skip, limit);
    if (response) {
      context.commit('setCategories', response.data);
    }
    return response.data
  },
  async getCategoryBySlug(context, { slug }) {
    const response = await api.getCategoryBySlug(slug);
    if (response) {
      context.commit('setCategory', response.data);
    }
    return response.data
  },
  async createCategory(context, payload) {
    const response = (await Promise.all([
      await api.getCategories(context.rootState.main.token, payload),
      await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
    ]))[0];
    if (response) {
      context.commit('setCategory', response.data);
      return response.data
    }
  },
};

export default actions;
