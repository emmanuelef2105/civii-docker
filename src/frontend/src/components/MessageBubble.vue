<!-- src/frontend/src/components/MessageBubble.vue -->
<template>
    <div :class="['bubble', typeClass]">
      {{ text }}
    </div>
  </template>
  
  <script>
  export default {
    name: 'MessageBubble',
    props: {
      text: { type: String, required: true },
      type: { type: String, default: 'usuario' }
    },
    computed: {
      typeClass() {
        return this.type === 'usuario' ? 'bubble-user' : 'bubble-chatbot'
      }
    }
  }
  </script>
  
  <style scoped>
  .bubble {
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 0.5rem;
    max-width: 60%;
    word-wrap: break-word;
  }
  
  .bubble-user {
    background-color: #cef;
    align-self: flex-end;
  }
  
  .bubble-chatbot {
    background-color: #eee;
    align-self: flex-start;
  }
  </style>
  