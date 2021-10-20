const mutations = {
  refreshStateItems(state) {
    state.items = JSON.parse(localStorage.getItem('basket_items'))
  },
  addProduct(state, { product, size, quantity }) {
    const basket_items = JSON.parse(localStorage.getItem('basket_items'))
    if (!basket_items) {
      const new_basket_items = [{ product, size, quantity }]
      localStorage.setItem('basket_items', JSON.stringify(new_basket_items))
      state.items = new_basket_items
    }
    else {
      let itemExists = basket_items.find(item => item.product.id === product.id)
      if (itemExists) {
        const new_basket_items = basket_items.map((item) => {
          if (item.product.id === product.id) {
            item.product = product;
            item.size = size;
            if (item.quantity + quantity > 0 || item.quantity > item.product.quantity)
              item.quantity += quantity;
          }
          return item
        });
        localStorage.setItem('basket_items', JSON.stringify(new_basket_items))
        state.items = new_basket_items
      } else {
        basket_items.push({ product, size, quantity })
        const new_basket_items = basket_items;
        localStorage.setItem('basket_items', JSON.stringify(new_basket_items))
        state.items = new_basket_items
      }
    }
  },
  removeProduct(state, { product_id }) {
    const basket_items = JSON.parse(localStorage.getItem('basket_items'))
    const new_basket_items = basket_items.filter((item) => {
      return item.product.id !== product_id;
    });
    localStorage.setItem('basket_items', JSON.stringify(new_basket_items))
    state.items = new_basket_items
    return state.items
  },
  decreaseProductQuantity(state, { product_id }) {
    const basket_items = JSON.parse(localStorage.getItem('basket_items'))
    const new_basket_items = basket_items.map((item) => {
      if (item.product.id !== product_id)
        if (item.quantity-1 > 0 || item.quantity > item.product.quantity)
          item.quantity--;
      return item
    })
    localStorage.setItem('basket_items', JSON.stringify(new_basket_items))
    state.items = new_basket_items
  }
};

export default mutations;
