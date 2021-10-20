export default {
  props: {
    show: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    hideModal() {
      this.$emit('update:show', false)
    }
  }
}
