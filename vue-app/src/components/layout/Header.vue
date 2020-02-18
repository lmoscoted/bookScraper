<template>
    <div>
    <b-navbar type="dark" variant="dark">
        <b-navbar-brand  to="/">BookScraper</b-navbar-brand>
        <b-navbar-nav align="end">
        <b-nav-item to="/" >Home</b-nav-item>
        <b-nav-item to="/about" >About</b-nav-item>
        </b-navbar-nav>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
.header {

color:aliceblue;
text-align: center;

}
</style>