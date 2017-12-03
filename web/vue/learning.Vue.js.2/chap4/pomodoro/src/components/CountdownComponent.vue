<template>
  <div class="well">
    <div class="pomodoro-timer">
      <span>{{ min | leftpad }}:{{ sec | leftpad }}</span>
    </div>
  </div>
</template>

<style scoped>
</style>

<script>
  export default {
    data () {
      return {
        min: 10,
        sec: 2
      }
    }
  }
</script>
