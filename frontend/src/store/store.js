import { reactive } from 'vue'

export const store = reactive({
    textCorrections: { most_occurring_lemmas: [] } ,
    isLoading: false,
    currentlyAnalyzedText: "Plak hier jouw tekst!",
    setTextCorrections(response) {
        this.textCorrections = response;
    }
})