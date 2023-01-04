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
    <p class="intro">Gebruik NLP en Machine Learning technieken om synoniemen te vinden voor jouw tekst.</p>
    <v-textarea @update:modelValue="print" placeholder="Plak hier jouw tekst!" />
    <v-btn @click="sendTextToBackend">Stel synoniemen voor!</v-btn>
  </div>
  <div class="loader" v-else>
    <v-progress-circular indeterminate color="var(--secondary-color)" size="48" />
  </div>
</template>
<style scoped>
.intro {
  padding: 1rem 0
}

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

