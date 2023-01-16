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
    scrollToSynonyms() {
      document.getElementById("synonyms").scrollIntoView({
        behavior: "smooth",
        block: 'center',
        inline: 'center'
      });
    },
    print(text) {
      this.text = text;
    },
    sendTextToBackend() {
      store.isLoading = true;
      store.currentlyAnalyzedText = this.text;
      return analyzeText(this.text)
        .then((res) => {
          store.isLoading = false;
          this.scrollToSynonyms();
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
    <p class="intro">Deze tool gaat op zoek naar veel gebruikte woorden in jouw tekst en zoekt voor die woorden gepaste
      synoniemen uit.</p>

    <p class="intro">De tool kan verschillende woordvormen linken aan 1 kernwoord (lemma) - dus ' blijven' en 'bleef'
      worden als eenzelfde woord aanzien. De synoniemen suggesties zijn gegenereerd door Machine Learning, gebruik is
      dus op eigen risico.</p>
    <v-textarea id="text-input" @update:modelValue="print" :placeholder="store.currentlyAnalyzedText" />
    <v-btn v-on:keyup.enter="sendTextToBackend()" type="submit" @click="sendTextToBackend">Stel synoniemen voor!</v-btn>
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

