<template>
  <div class="task-list">
    <h1>Maintenance Tasks</h1>
    <table class="table">
      <thead>
        <tr>
          <th>Equipment</th>
          <th>Task Type</th>
          <th>Next Due Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task.id">
          <td>{{ getEquipmentName(task.equipment) }}</td>
          <td>{{ formatTaskType(task.task_type) }}</td>
          <td>{{ task.next_due_date }}</td>
          <td>
            <button @click="logMaintenance(task)" class="btn btn-primary btn-sm">Log Completion</button>
          </td>
        </tr>
      </tbody>
    </table>
    
    <!-- Simple Modal for Logging -->
    <div v-if="showModal" class="modal-backdrop">
      <div class="modal-content">
        <h3>Log Maintenance</h3>
        <div class="form-group">
          <label>Technician Name:</label>
          <input v-model="logForm.technician_name" class="form-control" />
        </div>
        <div class="form-group">
          <label>Status:</label>
          <select v-model="logForm.status" class="form-control">
            <option value="completed">Completed</option>
            <option value="issue_found">Issue Found</option>
          </select>
        </div>
        <div class="form-group">
          <label>Notes:</label>
          <textarea v-model="logForm.notes" class="form-control"></textarea>
        </div>
        <button @click="submitLog" class="btn btn-success">Save</button>
        <button @click="showModal = false" class="btn btn-secondary">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TaskList',
  data() {
    return {
      tasks: [],
      equipment: [],
      showModal: false,
      logForm: {
        task: null,
        technician_name: '',
        status: 'completed',
        notes: ''
      }
    }
  },
  mounted() {
    this.fetchTasks();
    this.fetchEquipment();
  },
  methods: {
    fetchTasks() {
      axios.get('http://localhost:8000/api/tasks/')
        .then(response => {
          this.tasks = response.data;
        })
        .catch(error => {
          console.error('Error fetching tasks:', error);
        });
    },
    fetchEquipment() {
      axios.get('http://localhost:8000/api/equipment/')
        .then(response => {
          this.equipment = response.data;
        })
        .catch(error => {
          console.error('Error fetching equipment:', error);
        });
    },
    getEquipmentName(id) {
      const found = this.equipment.find(e => e.id === id);
      return found ? found.name : `Equipment #${id}`;
    },
    formatTaskType(type) {
      return type.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
    },
    logMaintenance(task) {
      this.logForm.task = task.id;
      this.showModal = true;
    },
    submitLog() {
      axios.post('http://localhost:8000/api/logs/', this.logForm)
        .then(() => {
          this.showModal = false;
          // Reset form
          this.logForm = {
            task: null,
            technician_name: '',
            status: 'completed',
            notes: ''
          };
          // Refresh tasks
          this.fetchTasks();
        })
        .catch(error => {
          console.error('Error logging maintenance:', error);
        });
    }
  }
}
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
  width: 500px;
}
.form-group {
  margin-bottom: 15px;
}
.form-control {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>