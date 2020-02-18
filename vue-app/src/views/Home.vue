<template>
  <b-container fluid>
    <br>
    <button class="btn btn-success" @click="getData">Start scraper</button>
    <br>
    <br>
    <vue-good-table
      :columns="columns"
      :rows="rows"
      theme="black-rhino"
      styleClass="vgt-table bordered"
      :pagination-options="{
        enabled: true,
        mode: 'records',
        perPage: 10,
        position: 'bottom',
        perPageDropdown: [15, 30, 50],
        dropdownAllowAll: false,
        nextLabel: 'next',
        prevLabel: 'prev',
        rowsPerPageLabel: 'Categories per page',
        ofLabel: 'of',
        pageLabel: 'page', // for 'pages' mode
        allLabel: 'All',
      }"
      >
        <div slot="table-actions">
        <!-- <button class="btn btn-success" @click="getData">Start scraper</button> -->
      </div>
      <template slot="table-row" slot-scope="props">
      <span v-if="props.column.field == 'btn'">
        <button class="btn btn-danger btn-sm" @click="deleteCategory( props.row.id )"> Delete</button>
      </span>
      <span v-else-if="props.column.field == 'books'">
        <button class="btn btn-primary btn-sm" @click="showBooks( props.row )"> Books</button>
      </span>
      <span v-else-if="props.column.field == 'name'">
        <span style="font-weight: bold;">{{props.row.name}}</span>
      </span>
      <span v-else>
        {{props.formattedRow[props.column.field]}}
      </span>
  </template>
  <div slot="emptystate">
    <p style="font-weight: bold; color: red">No data, please start the scraper in order to get data</p>
  </div>
    </vue-good-table>

  </b-container>
</template>

<script>
// @ is an alias to /src
// import the styles
import 'vue-good-table/dist/vue-good-table.css'
import { VueGoodTable } from 'vue-good-table'

export default {
  name: 'Home',
  components: {
    VueGoodTable
  }
}
</script>
