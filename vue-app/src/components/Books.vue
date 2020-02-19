<template>
  <b-container fluid>
    <br>
    <h2> <strong>{{categoryName}}</strong></h2>
    <br>
    <vue-good-table
      :columns="columns"
      :rows="books"
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
    rowsPerPageLabel: 'Books per page',
    ofLabel: 'of',
    pageLabel: 'page', // for 'pages' mode
    allLabel: 'All',
  }"
      >
  <template slot="table-row" slot-scope="props">
      <span v-if="props.column.field == 'btn'">
        <button class="btn btn-danger btn-sm" @click="deleteBook( props.row.id )"> Delete</button>
      </span>
      <span v-else-if="props.column.field == 'title'">
      <span style="font-weight: bold;">{{props.row.title}}</span>
      </span>
      <span v-else-if="props.column.field == 'thumbnail'">
        <b-img thumbnail  height="130" width="100" v-bind:src="props.row.thumbnail" alt="Image ">{{props.row.thumbnail}}</b-img>
      </span>
      <span v-else-if="props.column.field == 'product_description'">
        {{ props.row.product_description.substring(0, 250) }}
        <b-link id="show-btn" @click="$bvModal.show(props.row.id.toString())">Show more..</b-link>
          <b-modal v-bind:id= "props.row.id.toString()" scrollable hide-footer v-bind:title="props.row.title">
          <p class="my-4">{{props.row.product_description}}</p>
        </b-modal>
      </span>
      <span v-else>
        {{props.formattedRow[props.column.field]}}
      </span>
  </template>
  <div slot="emptystate">
    <p style="font-weight: bold; color: red"> Error, please come back to home and try again.</p>
  </div>
    </vue-good-table>
   </b-container>
</template>

<script>
// import the styles
import 'vue-good-table/dist/vue-good-table.css'
import { VueGoodTable } from 'vue-good-table'
import axios from 'axios'

// const urlBooks = 'http://django-server:8000/books/'
// const urlBooks = 'http://192.168.99.100:8000/books/' // Docker on windows
const urlBooks = 'http://127.0.0.1:8000/books/'
// const urlCategories = 'http://django-server:8000/categories/'// Docker url
// const urlCategories = 'http://192.168.99.100:8000/categories/' // # Docker on windows
const urlCategories = 'http://127.0.0.1:8000/categories/' // Docker url

export default {
  name: 'Books',
  // add to component
  components: {
    VueGoodTable
  },
  data () {
    return {
      columns: [
        {
          label: 'Title',
          field: 'title',
          filterOptions: {
            enabled: true, // enable filter for this column
            placeholder: 'Search title', // placeholder for filter input
            filterValue: '', // initial populated value for this filter
            filterFn: this.filterFn// custom filter function that
          }
        },
        {
          label: 'Thumbnail',
          field: 'thumbnail'
        },
        {
          label: 'Description',
          field: 'product_description',
          // type: 'number',
          filterOptions: {
            enabled: true, // enable filter for this column
            placeholder: 'Search description', // placeholder for filter input
            filterValue: '', // initial populated value for this filter
            filterFn: this.filterFn// custom filter function that
          }
        },
        {
          label: 'Price',
          field: 'price',
          filterOptions: {
            enabled: true, // enable filter for this column
            placeholder: 'Price', // placeholder for filter input
            filterValue: '', // initial populated value for this filter
            filterFn: this.filterFn// custom filter function that
          }
        },
        {
          label: 'Stock',
          field: 'stock',
          type: 'number',
          filterOptions: {
            enabled: true, // enable filter for this column
            placeholder: 'Search', // placeholder for filter input
            filterValue: '', // initial populated value for this filter
            filterFn: this.stockFilterFn// custom filter function that
          }
        },
        {
          label: 'UPC',
          field: 'upc',
          filterOptions: {
            enabled: true, // enable filter for this column
            placeholder: 'Search', // placeholder for filter input
            filterValue: '', // initial populated value for this filter
            filterFn: this.filterFn// custom filter function that
          }
        },

        {
          label: 'Action',
          field: 'btn',
          html: true
        }
      ],
      books: [],
      categoryId: '',
      categoryName: '',
      test: 'http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg'
    }
  },
  created () {
    this.categoryId = this.$route.params.id
    this.categoryName = this.$route.params.name
    var urlBooksCat = urlCategories + this.categoryId + '/books/'
    this.getBooks(urlBooksCat)
  },
  methods: {
    getBooks: function (urlBooksCat) {
      axios.get(urlBooksCat)
        .then(res => { this.books = res.data })
        .catch(err => console.log(err))
    },
    stockFilterFn: function (data, filterString) {
      var x = parseInt(filterString)
      return data === x
    },
    filterFn: function (data, filterString) {
      filterString = filterString.toLowerCase().trim()
      data = data.toLowerCase().trim()
      if (filterString.length > 0) {
        if (data.indexOf(filterString) !== -1) {
          return true
        }
      }
    },
    deleteBook: async function (bookId) {
      var urlBookDelete = urlBooks + bookId
      await axios.delete(urlBookDelete)
        .then(res => { this.books = this.books.filter(book => book.id !== bookId) })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>
