<template>
  <div class="user-info">
    <p class="name">{{ name }}</p>
    <it-icon box class="icon" name="account_circle" />
  </div>
</template>

<script>
export default {
  props: {
    name: { type: String, required: true },
  },
  setup(props) {},
};
</script>

<style lang="scss" scoped>
.user-info {
  position: fixed;
  top: 15px;
  right: 25px;
  display: flex;
  align-items: center;
  background-color: #f1f0f5;
  padding: 5px 5px 5px 15px;
  border-radius: 40px;
  transition: 0.35s ease;
  cursor: default;

  &:hover {
    background-color: #d5cdf3;
  }

  .name {
    margin-right: 15px;
  }

  .icon {
    font-size: 24px;
    padding: 6px;
    border-radius: 50%;
    color: #fff;
    background-color: #3a3a3a;
  }
}
</style>
