<template>
  <v-container>
    <HeaderLib @logout="handleLogout" is-authenticated/>
    <v-row justify="center" style="margin-top: 50px;">
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>
            <span class="headline">Возврат книги</span>
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="returnBook">
              <v-select
                item-title="fullName"
                item-value="id"
                v-model="selectedReader"
                :items="readers"
                label="Выберите читателя"
                outlined
                required
              ></v-select>
              <v-select
                item-title="name"
                item-value="id"
                v-model="selectedBook"
                :items="books"
                label="Выберите книгу"
                outlined
                required
              ></v-select>
              <v-btn type="submit" color="primary" block>Вернуть книгу</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HeaderLib from "@/components/HeaderLib.vue";
import axios from "axios";

export default {
  components: { HeaderLib },
  data() {
    return {
      readers: [],
      books: [],
      selectedReader: null,
      selectedBook: null,
    };
  },
  methods: {
    async fetchReaders() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/readers/", {
          headers: {
            Authorization: `Token ${localStorage.getItem("access")}`,
          },
        });
        this.readers = response.data
          .map(user => ({
            id: user.id,
            fullName: `${user.surname} ${user.name} ${user.patronymic || ""}`.trim(),
          }));
      } catch (error) {
        console.error("Ошибка при загрузке пользователей:", error);
      }
    },
    async fetchBooks() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/books/", {
          headers: {
            Authorization: `Token ${localStorage.getItem("access")}`,
          },
        });
        this.books = response.data.map(book => ({
          id: book.id,
          name: book.name,
        }));
      } catch (error) {
        console.error("Ошибка при загрузке книг:", error);
      }
    },
    async returnBook() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/v1/return_book/",
          {
            reader: this.selectedReader,
            book: this.selectedBook,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("access")}`,
            },
          }
        );
        alert(`${response.data.detail}`);
      } catch (error) {
        alert("Не удалось вернуть книгу. Проверьте данные и попробуйте снова.");
      }
    },
    handleLogout() {
      localStorage.removeItem("access");
      this.$router.push("/login");
    },
  },
  created() {
    this.fetchReaders();
    this.fetchBooks();
  },
};
</script>

<style scoped>
</style>
