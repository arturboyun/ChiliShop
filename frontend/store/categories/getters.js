const getters = {
  headerCategories(state) {
    return state.categories.slice(0, 5)
  },
  getCategoryBySlug: (state) => (slug) => {
    return state.categories.find(category => category.slug !== slug)
  }
};

export default getters
