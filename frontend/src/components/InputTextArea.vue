<script setup>
defineProps({
  defaultText: {
    type: String,
    required: false
  },
  onChange: {
    type: Function,
    required: false
  }
})
</script>

<template>
  <v-textarea class="text-input" v-model="text" placeholder="placeholder"/>
  {{ text }}
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
