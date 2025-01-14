// src/frontend/src/store/chatStore.js
import { defineStore } from 'pinia'

export const useChatStore = defineStore('chat', {
  state: () => ({
    messages: []
  }),
  actions: {
    async sendMessage(text) {
      // Creamos el payload
      const payload = {
        user_id: 'xyz',
        message: text,
        source: 'frontend',
        message_type: 'usuario',
        conversation_id: 'my_conversation_id'
      }

      // Llamamos al endpoint /chat
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/api/chat`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      })
      const data = await response.json()

      // Agregamos el mensaje del usuario al array
      this.messages.push({
        text,
        message_type: 'usuario'
      })

      // Agregamos la respuesta del chatbot
      this.messages.push({
        text: data.response,
        message_type: 'chatbot'
      })
    }
  }
})
