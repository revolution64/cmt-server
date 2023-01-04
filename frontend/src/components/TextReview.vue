<script setup>
import { getCurrentInstance } from 'vue';
import TitleParagraphSection from './partials/TitleParagraphSection.vue';
import { store } from '../store/store';

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
      return lemmas.map((lemma) => ({ title: lemma.lemma, value: lemma.occurrences })).slice(0,10);
    }
  },
  components: { TitleParagraphSection }
}
</script>

<template>
    <v-list className="synonymList" :key="componentKey" three-line="true" lines="three" title="Veel gebruikte woorden">
      <v-list-item v-for="item in store.textCorrections.most_occurring_lemmas" :key="item.lemma">
        <div>
          Het woord <overline class="font-weight-black" >'{{ item.lemma }}'</overline> 
          komt <overline class="font-weight-black">{{ item.occurences }} </overline> keer voor in jouw tekst
        </div>
         Enkele mogelijke <overline class="font-weight-black">synoniemen voor {{item.lemma}}</overline> zijn: {{ item.synonyms.map((woord) => ` ${woord}`).toString() }}
      </v-list-item>
    </v-list>
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

