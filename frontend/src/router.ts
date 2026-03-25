import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/Home.vue';
import Login from './pages/Login.vue';

export const router = createRouter({
    routes: [
        {
            path: "/",
            component: Home
        },
        {
            path: "/login",
            component: Login
        }
    ],
    history: createWebHistory()
});