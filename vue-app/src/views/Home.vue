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
        <button class="btn btn-primary btn-sm" @click="showBooks( props.row )"> Get</button>
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
import axios from 'axios'

const urlCategories = 'http://django-server:8000/categories/'
// const urlCategories = 'http://192.168.99.100:8000/categories/' // Docker on Windows IP Machine
// const urlCategories = 'http://127.0.0.1:8000/categories/'

export default {
  name: 'Home',
  components: {
    VueGoodTable
  },
  data () {
    return {
      columns: [

        {
          label: 'Category Name',
          field: 'name',
          // type: 'number',
          filterOptions: {
            enabled: true, // enable filter for this column
            placeholder: 'Search category', // placeholder for filter input
            filterValue: '', // initial populated value for this filter
            filterFn: this.filterName// custom filter function that
          }
        },
        {
          label: 'Books',
          field: 'books'
        },
        {
          label: 'Action',
          field: 'btn',
          html: true
        }
      ],
      rows: []
    }
  },
  methods: {
    getData: async function () {
      await axios.get(urlCategories)
        .then(res => { this.rows = res.data })
        .catch(err => console.log(err))
    },
    filterName: function (data, filterString) {
      filterString = filterString.toLowerCase().trim()
      data = data.toLowerCase().trim()
      if (filterString.length > 0) {
        if (data.indexOf(filterString) !== -1) {
          return true
        }
      }
    },
    deleteCategory: async function (categoryId) {
      var urlCatDelete = urlCategories + categoryId + '/'
      // console.log(urlCatDelete)
      await axios.delete(urlCatDelete)
        .then(res => { this.rows = this.rows.filter(cat => cat.id !== categoryId) })
        .catch(err => console.log(err))
    },
    routerAbout: function (row) {
      this.$router.push('about')
    },
    showBooks: function (row) {
      // var urlBooksCat = urlCategories + row.id + '/books'
      this.$router.push({ name: 'Books', params: { id: row.id, name: row.name } })
      // console.log(urlBooksCat)
    }

  }
}
</script>
