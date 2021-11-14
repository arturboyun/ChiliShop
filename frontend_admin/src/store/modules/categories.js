import { api } from '../../api';

const state = {
  categories: [],
  currentCategory: {},
};

const getters = {
  getCategories(state) {
    return state.categories;
  },
  getCurrentCategory(state) {
    return state.currentCategory;
  },
};

const actions = {
  async fetchCategories({ commit }, payload) {
    try {
      const response = await api.getCategories(payload.skip, payload.limit);
      await commit('setCategories', response.data);
    } catch (err) {}
  },
  async fetchCategoryBySlug({ commit }, payload) {
    try {
      const response = await api.getCategoryBySlug(payload.slug);
      await commit('setCurrentCategory', response.data);
    } catch (err) {}
  },
  async createCategory({ commit, dispatch, rootState }, payload) {
    try {
      const response = await api.createCategory(
        rootState.auth.authToken,
        payload
      );
      await dispatch('fetchCategories', { skip: 0, limit: 500 });
    } catch (err) {}
  },
  async deleteCategory({ commit, dispatch, rootState }, { categoryId }) {
    try {
      const response = await api.deleteCategory(
        rootState.auth.authToken,
        categoryId
      );
      await dispatch('fetchCategories', { skip: 0, limit: 500 });
    } catch (err) {}
  },
};

const mutations = {
  setCategories(state, payload) {
    state.categories = payload;
  },
  setCurrentCategory(state, payload) {
    state.currentCategory = payload;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
