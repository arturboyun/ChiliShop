const authTokenKey = 'auth-token';

export default {
  authTokenKey,
  async setLocalStorageItem(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  },
  async getLocalStorageItem(key) {
    return JSON.parse(localStorage.getItem(key));
  },
  async removeLocalStorageItem(key) {
    localStorage.removeItem(key);
  },
  async saveAuthToken(authToken) {
    this.setLocalStorageItem(authTokenKey, authToken);
  },
  async getAuthToken() {
    return this.getLocalStorageItem(authTokenKey);
  },
  async removeAuthToken() {
    this.removeLocalStorageItem(authTokenKey);
  },
};
