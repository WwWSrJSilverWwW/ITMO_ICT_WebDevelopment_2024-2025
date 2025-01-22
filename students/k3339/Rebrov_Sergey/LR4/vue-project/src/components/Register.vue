<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>
            <span class="headline">Регистрация</span>
          </v-card-title>

          <v-card-text>
            <v-form @submit.prevent="handleRegister">
              <v-text-field
                v-model="username"
                label="Имя пользователя"
                required
              ></v-text-field>
              <v-text-field
                v-model="firstName"
                label="Имя"
                required
              ></v-text-field>
              <v-text-field
                v-model="lastName"
                label="Фамилия"
                required
              ></v-text-field>
              <v-text-field
                v-model="email"
                label="Email"
                type="email"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                type="password"
                label="Пароль"
                required
              ></v-text-field>
              <v-btn type="submit" color="primary" block>Зарегистрироваться</v-btn>
            </v-form>
            <v-divider class="my-4"></v-divider>
            <v-row>
              <v-col class="text-center">
                <router-link to="/login">Уже есть аккаунт? Войти</router-link>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async handleRegister() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/users/', {
          username: this.username,
          first_name: this.firstName,
          last_name: this.lastName,
          email: this.email,
          password: this.password,
        });
        console.log('Успешная регистрация:', response.data);
        this.$router.push('/login');
      } catch (error) {
        console.error('Ошибка регистрации:', error.response.data);
      }
    },
  },
  created() {
    if (localStorage.getItem('access')) {
      this.$router.push('/');
    }
  },
};
</script>
