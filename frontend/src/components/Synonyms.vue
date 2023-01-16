<script setup>
import { store } from '../store/store';
import TitleParagraphSection from './partials/TitleParagraphSection.vue';
import SynonymSuggestion from './SynonymSuggestion.vue';
</script>

<script>
export default {
  data() {
    return {
      store,
      componentKey: 0
    }
  },

  methods: {
    getMostOccurringLemmasInListForm(lemmas) {
      return lemmas.map((lemma) => ({ title: lemma.lemma, value: lemma.occurrences })).slice(0, 10);
    }
  },
  components: { TitleParagraphSection, SynonymSuggestion }
}
</script>

<template>
  <div id="synonyms">
    <v-list v-if="!store.isLoading" className="synonymList" :key="componentKey" three-line="true"
      lines="three" title="Veel gebruikte woorden">
      <v-list-item v-for="item in store.textCorrections.most_occurring_lemmas" :key="item.lemma">
        <SynonymSuggestion v-bind="item"/>
      </v-list-item>
    </v-list>
  </div>
</template>

<style scoped>
.synonymList {
  padding-top: 1rem
}

.v-list-item--density-default:not(.v-list-item--nav).v-list-item--three-line {
  padding-inline-start: 0px;
}

@media (min-width: 1024px) {}
</style>

