<script setup>
defineProps({
    label: {
        type: String,
        required: false
    },

    onClick: {
        type: Function,
        required: true
    }
})
</script>

<template>
    <Button class="button" />
</template>

<style scoped>
.text-input {
    height: 2rem;
    width: 100vh;
    height: 50vh;
}

@media (min-width: 1024px) {

    .greetings h1,
    .greetings h3 {
        text-align: left;
    }
}
</style>
