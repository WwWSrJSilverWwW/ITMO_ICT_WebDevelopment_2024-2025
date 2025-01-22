<template>
  <v-container>
    <HeaderComponent :isAuthenticated="isAuthenticated" @logout="handleLogout" />

    <v-row style="margin-top: 75px;">
      <v-col>
        <template v-if="books.length">
          Здесь показаны книги, которые вы взяли:
        </template>
        <template v-else>
          <v-alert type="warning">
            У вас нет взятых книг. Запишитесь в читательский зал и возьмите книгу.
          </v-alert>
        </template>
      </v-col>
    </v-row>

    <v-row v-if="books.length">
      <v-col v-for="book in books" :key="book.id" cols="12" md="4">
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
  </v-container>
</template>

<script>
import HeaderComponent from '@/components/Header.vue';
import axios from 'axios';

export default {
  components: { HeaderComponent },
  data() {
    return {
      books: [],
      hall: {
        name: '',
        library: '',
      },
    };
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('access');
    },
  },
  methods: {
    async fetchBooks() {
      try {
        const userResponse = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('access')}`,
          },
        });
        const userId = userResponse.data.id;

        const readersResponse = await axios.get('http://127.0.0.1:8000/api/v1/readers/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('access')}`,
          },
        });

        const reader = readersResponse.data.find(reader => reader.user === userId);

        if (reader) {
          const booksResponse = await axios.get(`http://127.0.0.1:8000/api/v1/book_reader/${reader.id}`, {
            headers: {
              Authorization: `Token ${localStorage.getItem('access')}`,
            },
          });

          this.books = booksResponse.data;
          console.log(`http://127.0.0.1:8000/api/v1/book_reader/${reader.id}`);
        } else {
          this.books = [];
        }
      } catch (error) {
        console.error('Ошибка при загрузке данных о книгах:', error);
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
      this.fetchBooks();
    }
  },
};
</script>
