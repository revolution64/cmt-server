import { reactive } from 'vue'

export const store = reactive({
    textCorrections: { most_occurring_lemmas: [{ lemma: "tekst", occurences: 1, synonyms: ["geschrift", "document", "schrift"] }] },
    setTextCorrections(response) {
        this.textCorrections = response;
    }
})