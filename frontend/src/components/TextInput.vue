<script setup>
import IntroText from './IntroText.vue'
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
      store.isLoading = true;
      store.currentlyAnalyzedText = this.text;
      return analyzeText(this.text)
        .then((res) => {
          store.isLoading = false;
          store.hasFinishedCall = true;
          store.setTextCorrections(res.data);
        })
        .catch((e) => {
          store.isLoading = false;
          console.error(e);
        });
    }
  }
}
</script>

<template>
  <div v-if="store.isLoading === false">
    <IntroText />
    <v-textarea id="text-input" @update:modelValue="print" :placeholder="store.currentlyAnalyzedText" />
    <v-btn v-on:keyup.enter="sendTextToBackend()" type="submit" @click="sendTextToBackend">Stel synoniemen voor</v-btn>
  </div>
  <div class="loader" v-else>
    <v-progress-circular indeterminate color="var(--secondary-color)" size="48" />
  </div>
</template>
<style scoped>

.loader {
  display: flex;
  height: 50vw;


  align-items: center;
  justify-content: center;
}

@media (min-width: 1024px) {
  .loader {
    height: 25vw;
  }

}
</style>

