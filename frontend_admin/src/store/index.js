import { createStore } from 'vuex';
import auth from '@/store/modules/auth';
import category from '@/store/modules/category';
import product from '@/store/modules/product';

export default createStore({
  modules: {
    auth,
    category,
    product,
  },
});
