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
export default {
  name: 'Books',
  // add to component
  components: {
    VueGoodTable
  }
}
</script>

<style scoped>

</style>
