<template>
  <div class="equipment-list">
    <h1>Equipment</h1>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Location</th>
          <th>Installation Date</th>
          <th>Last Service</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in equipment" :key="item.id">
          <td>{{ item.name }}</td>
          <td>{{ item.location }}</td>
          <td>{{ item.installation_date }}</td>
          <td>{{ item.last_service_date || 'Not serviced' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EquipmentList',
  data() {
    return {
      equipment: []
    }
  },
  mounted() {
    this.fetchEquipment();
  },
  methods: {
    fetchEquipment() {
      axios.get('http://localhost:8000/api/equipment/')
        .then(response => {
          this.equipment = response.data;
        })
        .catch(error => {
          console.error('Error fetching equipment:', error);
        });
    }
  }
}
</script>