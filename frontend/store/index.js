import Vuex from 'vuex'
import categoriesModule from './categories'
import productsModule from './products'
import basketModule from './basket'

new Vuex.Store({
  modules: {
    categories: categoriesModule,
    products: productsModule,
    basket: basketModule,
  }
})
