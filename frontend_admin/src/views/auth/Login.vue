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
import { ref, watchEffect } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'Login',
  setup() {
    const store = useStore();

    const username = ref('');
    const password = ref('');
    const usernameErrors = ref([]);
    const passwordErrors = ref([]);

    const onSubmit = () => {
      store.dispatch('loginGetToken', {
        username: username.value,
        password: password.value,
      });
    };
    watchEffect(() => {
      if (!username.value.length) {
        usernameErrors.value.push('Это поле обязательно.');
      } else {
        usernameErrors.value = [];
      }
    });
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
