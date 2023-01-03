<script setup>
import { store } from '../store/store';
import TitleParagraphSection from './partials/TitleParagraphSection.vue';
</script>

<script>
export default {
  methods: {
    getListOfLemmas() {
      return store.textCorrections.most_occurring_lemmas.map((lemma) => ({ title: lemma.lemma, value: lemma.occurrences }));
    }
  },
  components: { TitleParagraphSection }
}
</script>

<template>

  <div>
    <TitleParagraphSection title="Veel gebruikte woorden" />
    <v-list three-line="true" lines="three" title="Veel gebruikte woorden" :items="getListOfLemmas()">

    </v-list>
  </div>
</template>
<style scoped>
@media (min-width: 1024px) {}
</style>

