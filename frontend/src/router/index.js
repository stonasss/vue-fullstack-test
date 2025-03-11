import { createRouter, createWebHistory } from 'vue-router'
import Binho from '@/components/Binho.vue'
import Games from '@/components/Games.vue'
import Authentication from '@/components/Authentication.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/binho',
      name : 'Binho',
      component : Binho
    },
    {
      path: '/',
      name : 'Games',
      component : Games
    },
    {
      path:'/auth',
      name: 'Authentication',
      component : Authentication
    }
  ],
})

export default router
