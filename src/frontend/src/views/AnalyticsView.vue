<!-- src/frontend/src/views/AnalyticsView.vue -->
<template>
    <div>
      <h1>Analíticas</h1>
      <p>Número de mensajes: {{ stats.totalMessages }}</p>
      <p>Tiempo promedio de respuesta: {{ stats.avgResponseTime }} ms</p>
      <p>Emociones más frecuentes: {{ stats.topEmotions.join(', ') }}</p>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue'
  
  export default {
    name: 'AnalyticsView',
    setup() {
      const stats = ref({
        totalMessages: 0,
        avgResponseTime: 0,
        topEmotions: []
      })
  
      onMounted(async () => {
        try {
          // Supongamos que tu backend tiene un endpoint para analíticas
          const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/api/stats`)
          const data = await response.json()
          stats.value = data
        } catch (error) {
          console.error('Error cargando estadísticas:', error)
        }
      })
  
      return {
        stats
      }
    }
  }
  </script>
  