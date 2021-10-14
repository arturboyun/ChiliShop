import Vue from 'vue';
import Router from 'vue-router';

import RouterComponent from './components/RouterComponent.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import(/* webpackChunkName: "start" */ './views/site/Main.vue'),
      children: [
        {
          path: 'admin',
          component: () => import(/* webpackChunkName: "start" */ './views/admin/Start.vue'),
          children: [
            {
              path: 'login',
              component: () => import(/* webpackChunkName: "login" */ './views/Login.vue'),
            },
            {
              path: 'dashboard',
              component: () => import(/* webpackChunkName: "main-dashboard" */ './views/admin/Dashboard.vue'),
            },
            {
              path: 'profile',
              component: RouterComponent,
              redirect: 'profile/view',
              children: [
                {
                  path: 'view',
                  component: () => import(
                    /* webpackChunkName: "main-profile" */ './views/admin/profile/UserProfile.vue'),
                },
                {
                  path: 'edit',
                  component: () => import(
                    /* webpackChunkName: "main-profile-edit" */ './views/admin/profile/UserProfileEdit.vue'),
                },
                {
                  path: 'password',
                  component: () => import(
                    /* webpackChunkName: "profile-password" */ './views/admin/profile/UserProfileEditPassword.vue'),
                },
              ],
            },
            {
              path: 'superuser',
              component: () => import(/* webpackChunkName: "main-admin" */ './views/admin/superuser/Admin.vue'),
              redirect: 'admin/users/all',
              children: [
                {
                  path: 'users',
                  redirect: 'users/all',
                },
                {
                  path: 'users/all',
                  component: () => import(
                    /* webpackChunkName: "main-admin-users" */ './views/admin/superuser/AdminUsers.vue'),
                },
                {
                  path: 'users/edit/:id',
                  name: 'admin-superuser-users-edit',
                  component: () => import(
                    /* webpackChunkName: "main-admin-users-edit" */ './views/admin/superuser/EditUser.vue'),
                },
                {
                  path: 'users/create',
                  name: 'admin-superuser-users-create',
                  component: () => import(
                    /* webpackChunkName: "main-admin-users-create" */ './views/admin/superuser/CreateUser.vue'),
                },
              ],
            },
          ],
        },
      ],
    },
    {
      path: '/*', redirect: '/',
    },
  ],
});
