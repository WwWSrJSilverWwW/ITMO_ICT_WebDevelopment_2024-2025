<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>Library Manager</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn to="/rent-book">Выдача книги</v-btn>
    <v-btn to="/return-book">Возврат книги</v-btn>
    <v-btn to="/attach-user">Прикрепить пользователя</v-btn>
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
