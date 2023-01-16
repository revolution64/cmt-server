<script>
export default {
  props: ['lemma', 'occurences', 'synonyms'],
  data() {
    return {
      lemma: this.lemma,
      occurences: this.occurences,
      synonyms: this.synonyms || []
    }
  }
}
</script >

<template>
  <div>
    Het woord '<overline class="font-weight-black">{{ lemma }}</overline>'
    komt <overline class="font-weight-black">{{ occurences }} </overline> keer voor in jouw tekst
  </div>
  <div v-if="synonyms.length > 0">Enkele mogelijke <overline class="font-weight-black">synoniemen voor {{ lemma }}</overline> zijn: {{
    synonyms.map((woord) => ` ${woord}`).toString()
  }}
  </div>
  <div v-else>
    Ons AI model heeft geen synoniemen gevonden, zoek synoniemen voor <overline class="font-weight-black">{{ lemma }}</overline> op <a
      :href="'https://synoniemen.net/index.php?zoekterm=' + lemma">synoniemen.net</a>
  </div>
</template>

