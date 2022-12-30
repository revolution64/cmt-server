<script setup>
  import axios from 'axios'
</script>

<script>
  export default {
    data() {
      return {
        text: ""
      }
    },
    methods: {
      print(text) {
        this.text = text;
      },
      sendTextToBackend() {
        return axios.post(`http://localhost:5000`, {
          "text": this.text
        })
                .then((res) => {
                  console.log(res);
                })
                .catch((e) => {
                  console.error(e);
                });
      }
    }
  }
</script>

<template>
  <v-textarea @update:modelValue="print"/>
  <v-btn @click="sendTextToBackend">Verbeter mijn tekst!</v-btn>
</template>
<style scoped>
@media (min-width: 1024px) {}
</style>

