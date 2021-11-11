import { api } from '../../api';
import utils from '../../utils';

// State
const state = {
  isLoggedIn: false,
  authToken: '',
  userInfo: {},
};

// Getters
const getters = {
  isLoggedIn(state) {
    return state.isLoggedIn;
  },
  getUsername(state) {
    return state.userInfo.full_name
      ? state.userInfo.full_name
      : state.userInfo.username;
  },
};

// Actions
const actions = {
  async loginGetToken({ commit, dispatch }, { username, password }) {
    try {
      const response = await api.loginGetToken(username, password);
      const { access_token } = response.data;
      await commit('saveAuthToken', access_token);
      await commit('setLoggedIn', true);
    } catch (err) {
      await dispatch('logout');
    }
  },
  async testToken({ state, commit, dispatch }) {
    const authToken = await utils.getAuthToken();
    if (authToken) {
      try {
        await api.testAuthToken(authToken);
        await commit('setLoggedIn', true);
        await commit('setAuthToken', authToken);
      } catch (err) {
        await dispatch('logout');
      }
    } else {
      await dispatch('logout');
    }
  },
  async getMe({ state, commit, dispatch }) {
    const authToken = await utils.getAuthToken();
    try {
      const response = await api.getMe(authToken);
      await commit('setUserInfo', response.data);
    } catch (err) {
      await dispatch('logout');
    }
  },
  async logout({ commit }) {
    await utils.removeAuthToken();
    await commit('setLoggedIn', false);
    await commit('setAuthToken', '');
  },
};

// Mutations
const mutations = {
  async saveAuthToken(state, authToken) {
    state.authToken = authToken;
    await utils.saveAuthToken(authToken);
  },
  setLoggedIn(state, loggedIn) {
    state.isLoggedIn = loggedIn;
  },
  setAuthToken(state, payload) {
    state.authToken = payload;
  },
  setUserInfo(state, payload) {
    state.userInfo = payload;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
