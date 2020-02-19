<template>
    <div>
    <b-navbar type="dark" variant="dark">
        <b-navbar-brand  @click="HomeRoute">BookScraper</b-navbar-brand>
        <b-navbar-nav align="end">
        <b-nav-item @click="HomeRoute()" >Home</b-nav-item>
        <b-nav-item @click="AboutRoute()" >About</b-nav-item>
        </b-navbar-nav>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    HomeRoute: function () {
      if (this.$router.currentRoute.name !== 'Home') {
        this.$router.push({ name: 'Home', params: { showButtonCat: true } })
      }
    },
    AboutRoute: function () {
      if (this.$router.currentRoute.name !== 'About') {
        this.$router.push({ name: 'About', params: { showButtonCat: true } })
      }
    }
  }

}
</script>

<style scoped>
.header {

color:aliceblue;
text-align: center;

}
</style>
