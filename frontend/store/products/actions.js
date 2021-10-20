import { api } from '@/api';

const actions = {
  async getProductBySlug(context, payload) {
    try {
      const response = await api.getProductBySlug(payload.slug);
      if (response) {
        // context.commit('setCategories', response.data);
      }
      return response.data
    } catch (e) {
      return null
    }
  },
  async getProductsByCategorySlug(context, { slug, skip = 0, limit = 999 }) {
    try {
      const response = await api.getProductsByCategorySlug(slug, skip, limit);
      if (response) {
        // context.commit('setCategories', response.data);
      }
      return response.data
    } catch (e) {
      return null
    }
  },
  async getProductsByCategoryID(context, { id, skip = 0, limit = 999 }) {
    try {
      const response = await api.getProductsByCategoryID(id, skip, limit);
      if (response) {
        // context.commit('setProducts', response.data);
      }
      return response.data
    } catch (e) {
      return null
    }
  },
}

export default actions
