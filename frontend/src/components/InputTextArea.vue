<script setup>
defineProps({
  defaultText: {
    type: String,
    required: false
  }
})
</script>

<template>
  <textarea class="text-input"/>
</template>

<style scoped>

.text-input {
  height: 2rem;
  width: 100vh;
  height: 50vh;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
