import { createRouter, createWebHistory } from 'vue-router'
import CVPage from '../views/CVView.vue' 
import HomeView from '../views/HomeView.vue' 
import InfoView from '../views/InfoView.vue' 
import TGView from '../views/TGView.vue' 

const routes = [
    { path: '/' , component:HomeView},
    { path: '/cv' , component:CVPage},
    { path: '/info' , component:InfoView},
    { path: '/tg' , component:TGView},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router