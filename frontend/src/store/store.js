import { reactive } from 'vue'

export const store = reactive({
    textCorrections: {},
    setTextCorrections(response) {
        console.log(response);
        this.textCorrections = response;
    }
})