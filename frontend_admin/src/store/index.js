import { createStore } from 'vuex';
import auth from '@/store/modules/auth';
import categories from '@/store/modules/categories';

export default createStore({
  modules: {
    auth,
    categories,
  },
});
