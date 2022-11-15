<template>
  <div>You must Login first</div>
</template>

<script>
export default {
    name: 'NotPermission',
    created() {
      console.log(this.$store.state.token)
    }
}
</script>

<style>

</style>