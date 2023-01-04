<script setup>
import { store } from '../store/store';
import { analyzeText } from '../api/cmt'
</script>

<script>
export default {
  data() {
    return {
      text: "",
      isLoading: false
    }
  },
  methods: {
    print(text) {
      this.text = text;
    },
    sendTextToBackend() {
      this.isLoading = true;
      return analyzeText(this.text)
        .then((res) => {
          this.isLoading = false;
          store.setTextCorrections(res.data);
        })
        .catch((e) => {
          this.isLoading = false;
          console.error(e);
        });
    }
  }
}
</script>

<template>
  <div v-if="this.isLoading === false">
    <v-textarea @update:modelValue="print"
      placeholder="Laten we eens proberen met een placeholder text. Waarom werkt dit niet." />
    <v-btn @click="sendTextToBackend">Stel synoniemen voor!</v-btn>
  </div>
  <v-progress-circular v-else indeterminate />
</template>
<style scoped>
@media (min-width: 1024px) {}
</style>

