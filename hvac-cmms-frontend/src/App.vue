<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">HVAC CMMS</a>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Dashboard</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/equipment" class="nav-link">Equipment</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/tasks" class="nav-link">Tasks</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    
    <div class="container mt-4">
      <router-view/>
    </div>
  </div>
</template>

<style>
@import 'bootstrap/dist/css/bootstrap.min.css';
</style>