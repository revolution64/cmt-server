<script setup>
import InputTextArea from './InputTextArea.vue'
</script>

<script>
  export default {
    methods: {
      print(text) {
        console.log(print);
      }
    }
  }
</script>

<template>
  <InputTextArea />
  <button @click="print">Verbeter mijn tekst!</button>
</template>
<style scoped>
@media (min-width: 1024px) {}
</style>

