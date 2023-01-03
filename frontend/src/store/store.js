import { reactive } from 'vue'

export const store = reactive({
    textCorrections: { most_occurring_lemmas: [{ lemma: "tryout", occurrences: 5, synonyms: ["Test", "Test3"] }] },
    setTextCorrections(response) {
        this.textCorrections = response;
    }
})