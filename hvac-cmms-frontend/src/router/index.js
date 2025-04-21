import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import EquipmentList from '../views/EquipmentList.vue'
import TaskList from '../views/TaskList.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/equipment',
    name: 'Equipment',
    component: EquipmentList
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: TaskList
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router