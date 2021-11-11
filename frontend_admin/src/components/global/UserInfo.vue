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

  .name {
    margin-right: 15px;
  }

  .icon {
    font-size: 24px;
    padding: 6px;
    border-radius: 50%;
    color: #fff;
    background-color: #6065be;
  }
}
</style>
