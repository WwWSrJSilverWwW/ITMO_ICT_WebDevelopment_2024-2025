<template>
  <v-container>
    <HeaderComponent :isAuthenticated="isAuthenticated" @logout="handleLogout" />
    <v-row style="margin-top: 75px;">
      <v-col>
        <v-text-field v-model="searchQuery.name" label="Поиск по названию библиотеки" outlined></v-text-field>
      </v-col>
    </v-row>
    <v-row v-if="filteredLibraries.length">
      <v-col v-for="library in filteredLibraries" :key="library.id" cols="12" md="4">
        <v-card>
          <v-card-title>{{ library.name }}</v-card-title>
          <v-card-subtitle style="margin-bottom: 20px;">
            Адрес: {{ library.address }}
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col>
        <v-alert type="info">Нет результатов для поиска.</v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HeaderComponent from '@/components/Header.vue';
import axios from 'axios';

export default {
  components: { HeaderComponent },
  data() {
    return {
      libraries: [],
      searchQuery: {
        name: '',
      },
    };
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('access');
    },
    filteredLibraries() {
      return this.libraries.filter(library =>
        library.name && library.name.toLowerCase().includes(this.searchQuery.name.toLowerCase())
      );
    },
  },
  methods: {
    async fetchLibraries() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/libraries/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('access')}`,
          },
        });
        this.libraries = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке библиотек:', error);
      }
    },
    handleLogout() {
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      this.$router.push('/login');
    },
  },
  created() {
    if (!this.isAuthenticated) {
      this.$router.push('/login');
    } else {
      this.fetchLibraries();
    }
  },
};
</script>
