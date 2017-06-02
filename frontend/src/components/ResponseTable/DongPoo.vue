<template lang="pug">
  .ts.raised.card
    .secondary.extra.content
      .header 東風
    .content
      .description
        table.ts.celled.table
          thead
            tr
              th 資料日期
              th 到件日期
              th 收件人
              th 代收款
          tbody
            tr
              td {{ responseData.bookingDate }}
              td {{ responseData.handleDate }}
              td {{ responseData.consigneeName }}
              td {{ responseData.realCcPrice }}
        table.ts.celled.selectable.table
          thead
            tr
              th #
              th 日期
              th 時間
              th 貨況
          tbody
            tr(v-for="row in responseData.details", :class="{ positive : isPositive(row.remark) }")
              td {{ row.rowNum }}
              td {{ row.handleDate }}
              td {{ row.handleTime }}
              td {{ row.remark }}
</template>

<script>
export default {
  name: 'DongPoo',
  props: ['responseData'],
  data () {
    return {
    }
  },
  methods: {
    isPositive (remark) {
      if (String(remark).indexOf('配完') !== -1) {
        return true
      }
    }
  }
}
</script>

<style scope>
</style>
