<template>
  <v-container>
    <HeaderComponent :isAuthenticated="isAuthenticated" @logout="handleLogout" />

    <v-row style="margin-top: 75px;">
      <v-col>
        <v-card>
          <v-card-title>
            <span class="headline">Профиль читателя</span>
          </v-card-title>
          <v-card-text>
            <v-form ref="profileForm" @submit.prevent="saveProfile">
              <v-text-field
                v-model="reader.surname"
                label="Фамилия"
                outlined
                required
              ></v-text-field>
              <v-text-field
                v-model="reader.name"
                label="Имя"
                outlined
                required
              ></v-text-field>
              <v-text-field
                v-model="reader.patronymic"
                label="Отчество"
                outlined
              ></v-text-field>
              <v-text-field
                v-model="reader.ticket"
                label="Читательский билет"
                outlined
                required
              ></v-text-field>
              <v-text-field
                v-model="reader.passport"
                label="Паспорт"
                outlined
                required
              ></v-text-field>

              <!-- Поле для даты рождения с пояснением формата -->
              <v-text-field
                v-model="reader.birth_date"
                label="Дата рождения"
                outlined
                required
                placeholder="дд.мм.гггг"
              ></v-text-field>

              <v-text-field
                v-model="reader.address"
                label="Адрес"
                outlined
              ></v-text-field>
              <v-text-field
                v-model="reader.phone"
                label="Телефон"
                outlined
                required
                placeholder="+7 (___) ___-__-__"
                mask="+7 (###) ###-##-##"
              ></v-text-field>
              <v-text-field
                v-model="reader.education"
                label="Образование"
                outlined
              ></v-text-field>
              <v-switch
                v-model="reader.is_academic"
                label="Научный сотрудник"
              ></v-switch>

              <v-btn type="submit" color="primary" block>
                Сохранить
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HeaderComponent from "@/components/Header.vue";
import axios from "axios";

export default {
  components: { HeaderComponent },
  data() {
    return {
      reader: {
        surname: "",
        name: "",
        patronymic: "",
        ticket: "",
        passport: "",
        birth_date: "",
        address: "",
        phone: "",
        education: "",
        is_academic: false,
      },
      readerId: null,
    };
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem("access");
    },
  },
  methods: {
    async fetchReader() {
      try {
        const userResponse = await axios.get(
          "http://127.0.0.1:8000/auth/users/me/",
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("access")}`,
            },
          }
        );
        const userId = userResponse.data.id;

        const readersResponse = await axios.get(
          "http://127.0.0.1:8000/api/v1/readers/",
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("access")}`,
            },
          }
        );

        const reader = readersResponse.data.find(
          (reader) => reader.user === userId
        );

        if (reader) {
          this.reader = reader;
          this.readerId = reader.id;
        } else {
          await this.createReader(userResponse.data);
        }
      } catch (error) {
        console.error("Ошибка при загрузке данных профиля:", error);
      }
    },
    async createReader(user) {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/v1/readers/",
          {
            user: user.id,
            surname: user.last_name,
            name: user.first_name,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("access")}`,
            },
          }
        );
        this.reader = response.data;
        this.readerId = response.data.id;
      } catch (error) {
        console.error("Ошибка при создании нового читателя:", error);
      }
    },
    async saveProfile() {
      try {
        await axios.patch(
          `http://127.0.0.1:8000/api/v1/readers/${this.readerId}`,
          this.reader,
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("access")}`,
            },
          }
        );
        alert("Профиль успешно сохранен!");
      } catch (error) {
        console.error("Ошибка при сохранении профиля:", error);
        alert("Не удалось сохранить профиль.");
      }
    },
    handleLogout() {
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      this.$router.push("/login");
    },
  },
  created() {
    if (!this.isAuthenticated) {
      this.$router.push("/login");
    } else {
      this.fetchReader();
    }
  },
};
</script>
