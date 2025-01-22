<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>
            <span class="headline">Вход</span>
          </v-card-title>

          <v-card-text>
            <v-form @submit.prevent="handleLogin">
              <v-text-field
                v-model="username"
                label="Имя пользователя"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                type="password"
                label="Пароль"
                required
              ></v-text-field>
              <v-btn type="submit" color="primary" block>Войти</v-btn>
            </v-form>
            <v-divider class="my-4"></v-divider>
            <v-row>
              <v-col class="text-center">
                <router-link to="/register">Зарегистрироваться</router-link>
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
      password: '',
    };
  },
  methods: {
    async handleLogin() {
      try {
        const loginResponse = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
          username: this.username,
          password: this.password,
        });
        const token = loginResponse.data.auth_token;

        localStorage.setItem('access', token);

        const userResponse = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        });

        if (userResponse.data.is_staff) {
          this.$router.push('/rent-book');
        } else {
          this.$router.push('/home');
        }
      } catch (error) {
        console.error('Ошибка авторизации:', error.response?.data || error.message);
        alert('Не удалось войти. Проверьте введенные данные.');
      }
    },
  },
  created() {
    if (localStorage.getItem('access')) {
      this.$router.push('/home');
    }
  },
};
</script>
