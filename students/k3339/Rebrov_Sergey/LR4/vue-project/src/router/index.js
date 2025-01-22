import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue';
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';
import Books from '@/components/Books.vue';
import Libraries from '@/components/Libraries.vue';
import Profile from '@/components/Profile.vue';
import RentBook from '@/components/RentBook.vue';
import ReturnBook from '@/components/ReturnBook.vue';
import AttachUser from "@/components/AttachUser.vue";

const routes = [
  { path: '/home', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/books', component: Books },
  { path: '/libraries', component: Libraries },
  { path: '/profile', component: Profile },
  { path: '/rent-book', component: RentBook },
  { path: '/return-book', component: ReturnBook },
  { path: '/attach-user', component: AttachUser },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
