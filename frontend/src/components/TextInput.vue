<script setup>
import { store } from '../store/store';
import { analyzeText } from '../api/cmt'
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
      return analyzeText(this.text)
        .then((res) => {
          store.setTextCorrections(res.data);
        })
        .catch((e) => {
          console.error(e);
        });
    }
  }
}
</script>

<template>
  <v-textarea @update:modelValue="print" placeholder="Laten we eens proberen met een placeholder text. Waarom werkt dit niet."/>
  <v-btn @click="sendTextToBackend">Verbeter mijn tekst!</v-btn>
</template>
<style scoped>
@media (min-width: 1024px) {}
</style>

