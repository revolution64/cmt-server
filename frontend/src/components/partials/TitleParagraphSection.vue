<script setup>
</script>

<script>
export default {
  props: {
    title: String,
    text: String 
  }
}
</script>

<template>
  <div>
    <div class="text-h6">{{title}}</div>
    <div class="text-body-1">{{text}}</div>
  </div>
</template>