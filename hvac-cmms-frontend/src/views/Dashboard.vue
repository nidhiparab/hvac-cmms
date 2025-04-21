<template>
  <div class="dashboard">
    <h1>HVAC Maintenance Dashboard</h1>
    <div class="dashboard-stats">
      <div class="stat-card">
        <h3>Equipment</h3>
        <p class="stat">{{ summary.equipment_count || 0 }}</p>
      </div>
      <div class="stat-card">
        <h3>Tasks Due Soon</h3>
        <p class="stat">{{ summary.tasks_due_soon || 0 }}</p>
      </div>
      <div class="stat-card">
        <h3>Completed Tasks</h3>
        <p class="stat">{{ summary.tasks_completed || 0 }}</p>
      </div>
      <div class="stat-card">
        <h3>Issues Found</h3>
        <p class="stat">{{ summary.tasks_with_issues || 0 }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DashboardView',
  data() {
    return {
      summary: {}
    }
  },
  mounted() {
    this.fetchDashboardData();
  },
  methods: {
    fetchDashboardData() {
      axios.get('http://localhost:8000/api/dashboard-summary/')
        .then(response => {
          this.summary = response.data;
        })
        .catch(error => {
          console.error('Error fetching dashboard data:', error);
        });
    }
  }
}
</script>

<style scoped>
.dashboard-stats {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
.stat-card {
  background-color: #f0f0f0;
  border-radius: 5px;
  padding: 20px;
  width: 23%;
  text-align: center;
}
.stat {
  font-size: 2em;
  font-weight: bold;
}
</style>