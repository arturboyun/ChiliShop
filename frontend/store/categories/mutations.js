const mutations = {
  setCategories(state, payload) {
    state.categories = payload
  },
  setCategory(state, payload) {
    state.categories = state.categories.map((category) => {
        return category.id === payload.id ? payload : category
    })
  },
};

export default mutations;
