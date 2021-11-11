<template>
  <div class="login">
    <form class="form" @submit.prevent="onSubmit">
      <h2 class="form__title">Вход</h2>
      <div class="form__inputs">
        <it-input
          v-model="username"
          label-top="Логин"
          prefix-icon="person"
          :status="usernameErrors.length ? 'danger' : null"
          :message="usernameErrors.length ? usernameErrors[0] : null"
          type="text"
          placeholder="John Doe"
        />
        <it-input
          v-model="password"
          label-top="Пароль"
          prefix-icon="lock"
          type="password"
          placeholder="Must have at least 6 characters"
        />
        <it-button block type="primary" @click="null"> Sign up </it-button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref, getCurrentInstance } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export default {
  name: 'Login',
  setup(props, context) {
    const app = getCurrentInstance();
    const store = useStore();
    const router = useRouter();

    const showMessage = app.appContext.config.globalProperties.$Message;

    const username = ref('');
    const password = ref('');
    const usernameErrors = ref([]);
    const passwordErrors = ref([]);

    const onSubmit = async () => {
      await store.dispatch('loginGetToken', {
        username: username.value,
        password: password.value,
      });

      if (store.getters.isLoggedIn) {
        showMessage.success({ text: 'Вы успешно вошли!' });
        router.push({ path: '/' });
      } else {
        showMessage.danger({ text: 'Ой. Логин или пароль не верны!' });
      }
    };

    return { username, password, usernameErrors, passwordErrors, onSubmit };
  },
};
</script>

<style scoped lang="scss">
.login {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: calc(100vh - 56px);
}

.form {
  border-radius: 4px;
  border: 1px dashed rgba(#2a2a2a, 0.3);
  padding: 24px 38px 24px 38px;

  &__title {
    text-align: center;
    font-size: 1.2em;
    font-weight: 700;
    margin-bottom: 25px;
  }

  &__inputs > * + * {
    margin: 16px 0;
  }
}
</style>
