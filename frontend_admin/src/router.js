import { createRouter, createWebHistory } from 'vue-router';
import Main from '@/views/Main';

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main,
    children: [
      {
        path: 'login',
        name: 'Login',
        component: () =>
          import(/* webpackChunkName: "login" */ '@/pages/auth/Login.vue'),
      },
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () =>
          import(/* webpackChunkName: "dashboard" */ '@/pages/Dashboard.vue'),
      },
      {
        path: 'orders',
        name: 'Orders',
        component: () =>
          import(/* webpackChunkName: "orders" */ '@/pages/Orders.vue'),
      },
      {
        path: 'products',
        name: 'Products',
        component: () =>
          import(/* webpackChunkName: "products" */ '@/pages/Products.vue'),
      },
      {
        path: 'categories',
        name: 'Categories',
        component: () =>
          import(/* webpackChunkName: "categories" */ '@/pages/Categories.vue'),
      },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    component: () =>
      import(
        /* webpackChunkName: "not_found_page" */ '@/pages/NotFoundPage.vue'
      ),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
