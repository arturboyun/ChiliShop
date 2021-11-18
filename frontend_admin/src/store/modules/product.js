import { api } from '@/api';

const state = {
  products: [],
};

const getters = {
  getProducts(state) {
    return state.products;
  },
  getProductsCount(state) {
    return state.products.length;
  },
};

const actions = {
  async fetchProducts({ commit }, payload) {
    try {
      const response = await api.product.getProducts(
        payload.skip,
        payload.limit
      );
      await commit('setProducts', response.data);
    } catch (err) {}
  },
  async fetchProductById({ commit }, payload) {
    try {
      const response = await api.product.getProductById(payload.id);
    } catch (err) {}
  },
  async fetchProductBySlug({ commit }, payload) {
    try {
      const response = await api.product.getProductBySlug(payload.slug);
    } catch (err) {}
  },
  async createProduct({ commit, dispatch, rootState }, payload) {
    try {
      const response = await api.product.createProduct(
        rootState.auth.authToken,
        payload
      );
      await dispatch('fetchProducts', { skip: 0, limit: 500 });
    } catch (err) {}
  },
  async updateProduct({ commit, dispatch, rootState }, payload) {
    try {
      const response = await api.product.updateProduct(
        rootState.auth.authToken,
        payload
      );
      await dispatch('fetchProducts', { skip: 0, limit: 500 });
    } catch (err) {}
  },
  async deleteProduct({ commit, dispatch, rootState }, { id }) {
    try {
      const response = await api.product.deleteProduct(
        rootState.auth.authToken,
        id
      );
      await dispatch('fetchProducts', { skip: 0, limit: 500 });
    } catch (err) {}
  },
};

const mutations = {
  setProducts(state, payload) {
    state.products = payload;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
