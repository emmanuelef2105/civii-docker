<!-- src/frontend/src/views/ChatView.vue -->
<template>
    <div class="chat-container">
      <div class="messages">
        <MessageBubble
          v-for="(msg, index) in messages"
          :key="index"
          :text="msg.text"
          :type="msg.message_type"
        />
      </div>
  
      <div class="input-area">
        <input
          v-model="userMessage"
          @keyup.enter="sendMessage"
          placeholder="Escribe tu mensaje..."
        />
        <button @click="sendMessage">Enviar</button>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  import MessageBubble from '../components/MessageBubble.vue'
  import { useChatStore } from '../store/chatStore'
  
  export default {
    name: 'ChatView',
    components: {
      MessageBubble
    },
    setup() {
      const chatStore = useChatStore()
      const userMessage = ref('')
  
      const sendMessage = async () => {
        if (!userMessage.value.trim()) return
        await chatStore.sendMessage(userMessage.value)
        userMessage.value = ''
      }
  
      return {
        messages: chatStore.messages,
        userMessage,
        sendMessage
      }
    }
  }
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 100%;
  }
  .messages {
    flex: 1;
    overflow-y: auto;
    margin-bottom: 1rem;
  }
  .input-area {
    display: flex;
    gap: 0.5rem;
  }
  </style>
  