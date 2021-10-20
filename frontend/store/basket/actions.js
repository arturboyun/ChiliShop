const actions = {
  refreshStateItems(context) {
    context.commit('refreshStateItems')
  },
  addItem(context, payload) {
    context.commit('addProduct', payload)
  },
  removeItem(context, { product_id }) {
    return context.commit('removeProduct', { product_id })
  },
  decreaseProductQuantity(context, { product_id }) {
    context.commit('decreaseProductQuantity', { product_id })
  }
}

export default actions
