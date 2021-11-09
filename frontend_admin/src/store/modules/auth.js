import { api } from '@/api';

const state = { authToken: '' };
const getters = {
  isLoggedIn(state) {
    return !!state.authToken;
  },
};
const actions = {
  async loginGetToken({ commit }, { username, password }) {
    const response = await api.loginGetToken(username, password);
    const { access_token } = response.data;
    await commit('setAuthToken', access_token);
  },
  async getMe({ state, commit }) {
    const response = await api.getMe(state.authToken);
    console.log(response.data);
  },
};
const mutations = {
  setAuthToken(state, authToken) {
    state.authToken = authToken;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
