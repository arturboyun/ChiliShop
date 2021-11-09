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
          import(/* webpackChunkName: "login" */ '@/views/auth/Login.vue'),
      },
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () =>
          import(/* webpackChunkName: "dashboard" */ '@/views/Dashboard.vue'),
      },
      {
        path: 'orders',
        name: 'Orders',
        component: () =>
          import(/* webpackChunkName: "orders" */ '@/views/Orders.vue'),
      },
      {
        path: 'products',
        name: 'Products',
        component: () =>
          import(/* webpackChunkName: "products" */ '@/views/Products.vue'),
      },
      {
        path: 'categories',
        name: 'Categories',
        component: () =>
          import(/* webpackChunkName: "categories" */ '@/views/Categories.vue'),
      },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    component: () =>
      import(
        /* webpackChunkName: "not_found_page" */ '@/views/NotFoundPage.vue'
      ),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
