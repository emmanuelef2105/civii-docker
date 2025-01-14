<!-- src/frontend/src/components/Sidebar.vue -->
<template>
    <div class="sidebar">
      <button @click="updateData">Actualizar Datos</button>
      <nav>
        <!-- enlaces de navegación -->
      </nav>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    name: 'Sidebar',
    setup() {
      const updateData = async () => {
        try {
          const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/api/crawl`)
          const data = await response.json()
          console.log(data)
        } catch (error) {
          console.error('Error al hacer crawling:', error)
        }
      }
      return {
        updateData
      }
    }
  }
  </script>
  