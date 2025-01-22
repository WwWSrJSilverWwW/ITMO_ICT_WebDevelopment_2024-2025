<template>
  <v-container>
    <HeaderLib @logout="handleLogout" is-authenticated/>
    <v-row justify="center" style="margin-top: 50px;">
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>
            <span class="headline">Привязка пользователя</span>
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="attachUser">
              <v-select
                item-title="fullName"
                item-value="id"
                v-model="selectedReader"
                :items="readers"
                label="Выберите пользователя"
                outlined
                required
              ></v-select>

              <v-select
                item-title="name"
                item-value="id"
                v-model="selectedLibrary"
                :items="libraries"
                label="Выберите библиотеку"
                outlined
                required
                @update:model-value="fetchHalls"
              ></v-select>

              <v-select
                item-title="name"
                item-value="id"
                v-model="selectedHall"
                :items="halls"
                label="Выберите зал"
                outlined
                required
              ></v-select>

              <v-btn type="submit" color="primary" block>Привязать пользователя</v-btn>
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
      libraries: [],
      halls: [],
      selectedReader: null,
      selectedLibrary: null,
      selectedHall: null,
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
        this.readers = response.data.map(user => ({
          id: user.id,
          fullName: `${user.surname} ${user.name} ${user.patronymic || ""}`.trim(),
        }));
      } catch (error) {
        console.error("Ошибка при загрузке пользователей:", error);
      }
    },

    async fetchLibraries() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/libraries/", {
          headers: {
            Authorization: `Token ${localStorage.getItem("access")}`,
          },
        });
        this.libraries = response.data.map(library => ({
          id: library.id,
          name: library.name,
        }));
      } catch (error) {
        console.error("Ошибка при загрузке библиотек:", error);
      }
    },

    async fetchHalls() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/halls/", {
          headers: {
            Authorization: `Token ${localStorage.getItem("access")}`,
          },
        });

        this.halls = response.data
          .filter(hall => hall.library.id === this.selectedLibrary)
          .map(hall => ({
            id: hall.id,
            name: hall.name,
          }));

      } catch (error) {
        console.error("Ошибка при загрузке залов:", error);
      }
    },

    async attachUser() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/v1/attach_user/",
          {
            reader: this.selectedReader,
            hall: this.selectedHall,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("access")}`,
            },
          }
        );
        alert(`${response.data.detail}`);
      } catch (error) {
        alert("Не удалось привязать пользователя. Проверьте данные и попробуйте снова.");
      }
    },

    handleLogout() {
      localStorage.removeItem("access");
      this.$router.push("/login");
    },
  },
  created() {
    this.fetchReaders();
    this.fetchLibraries();
  },
};
</script>

<style scoped>
</style>
