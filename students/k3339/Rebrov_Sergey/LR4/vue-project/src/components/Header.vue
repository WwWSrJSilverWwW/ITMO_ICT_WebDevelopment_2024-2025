<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>Library Manager</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn to="/home">Главная</v-btn>
    <v-btn to="/books">Книги</v-btn>
    <v-btn to="/libraries">Библиотеки</v-btn>
    <v-btn to="/profile">Профиль</v-btn>
    <v-btn v-if="isAuthenticated" @click="handleLogout">Выйти</v-btn>
  </v-app-bar>
</template>

<script>
export default {
  props: {
    isAuthenticated: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    handleLogout() {
      this.$emit('logout');
    },
  },
};
</script>

<style scoped>
</style>
