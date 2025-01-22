<template>
  <v-container>
    <HeaderComponent :isAuthenticated="isAuthenticated" @logout="handleLogout" />
    <v-row style="margin-top: 75px;">
      <v-col>
        <v-text-field v-model="searchQuery.title" label="Поиск по названию книги" outlined></v-text-field>
      </v-col>
    </v-row>
    <v-row v-if="filteredBooks.length">
      <v-col v-for="book in filteredBooks" :key="book.id" cols="12" md="4">
        <v-card>
          <v-card-title>{{ book.name }}</v-card-title>
          <v-card-subtitle>
            Автор:
            <span v-for="(author, index) in book.authors" :key="author.id">
              {{ author.name }} {{ author.surname }}{{ index < book.authors.length - 1 ? ', ' : '' }}
            </span>
          </v-card-subtitle>
          <v-card-subtitle style="margin-bottom: 20px;">
            Издательство: {{ book.publisher.name }} ({{ book.publisher.year }})
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
import axios from "axios";

export default {
  components: { HeaderComponent },
  data() {
    return {
      books: [],
      searchQuery: {
        title: '',
      },
    };
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('access');
    },
    filteredBooks() {
      return this.books.filter(book =>
        book.name && book.name.toLowerCase().includes(this.searchQuery.title.toLowerCase())
      );
    },
  },
  methods: {
    async handleSearch() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/books/');
        this.books = response.data;
      } catch (error) {
        console.error('Ошибка при поиске книг:', error);
      }
    },
    handleLogout() {
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      this.$router.push('/login');
    },
    async fetchBooks() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/books/');
        this.books = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке книг:', error);
      }
    },
  },
  created() {
    if (!this.isAuthenticated) {
      this.$router.push('/login');
    } else {
      this.fetchBooks();
    }
  },
};
</script>
