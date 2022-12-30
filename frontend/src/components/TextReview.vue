<script setup>
import { store } from '../store/store';
import TitleParagraphSection from './partials/TitleParagraphSection.vue';
</script>

<script>
export default {
    data() {
        return {
            textCorrections: store.textCorrections
        };
    },
    methods: {},
    components: { TitleParagraphSection }
}
</script>

<template>
  
  <div>
    <TitleParagraphSection title="Spelfouten" text="Geen spelfouten gevonden" />
    <TitleParagraphSection title="Veel gebruikte woorden" :text="store.textCorrections.most_occurring_lemmas" />
    <TitleParagraphSection title="Veel gebruikte zinsstructuren" :text="store.textCorrections.most_occurring_pos"/>
  </div>
</template>
<style scoped>
@media (min-width: 1024px) {}
</style>

