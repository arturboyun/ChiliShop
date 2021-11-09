import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../views/Dashboard.vue';

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/orders',
    name: 'Orders',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/Orders.vue'),
  },
  {
    path: '/products',
    name: 'Products',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/Products.vue'),
  },
  {
    path: '/categories',
    name: 'Categories',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/Categories.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/NotFoundPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
