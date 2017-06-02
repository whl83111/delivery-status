<template lang="pug">
  .ts.raised.card
    .secondary.extra.content
      .header 黑貓宅急便
    .content
      .description
        table.ts.celled.selectable.table
          thead
            tr
              th #
              th 目前狀態
              th 資料登入時間
              th 負責營業所
          tbody
            tr(v-for="row in responseData.rows", :class="isPositive(row.status)")
              td {{ row.rowNum }}
              td {{ row.status }}
              td {{ row.time }}
              td {{ row.location }}
</template>

<script>
export default {
  name: 'BlackCat',
  props: ['responseData'],
  data () {
    return {
    }
  },
  methods: {
    isPositive (status) {
      if (String(status).indexOf('順利送達') !== -1) {
        return true
      }
    }
  }
}
</script>

<style scope>

</style>
