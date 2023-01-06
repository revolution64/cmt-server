import { reactive } from 'vue'

export const store = reactive({
    textCorrections: { most_occurring_lemmas: [] } ,
    setTextCorrections(response) {
        this.textCorrections = response;
    }
})