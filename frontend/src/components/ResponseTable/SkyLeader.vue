<template lang="pug">
  .ts.raised.card
    .secondary.extra.content
      .header 速立達
    .content
      .description
        table.ts.celled.selectable.table
          thead
            tr
              th 時間
              th 狀態
          tbody
            tr(v-for="data in responseData", :class="{ positive : isPositive(data.status) }")
              td {{ data.time }}
              td {{ data.status }}
</template>

<script>
export default {
  name: 'SkyLeader',
  props: ['responseData'],
  data () {
    return {
    }
  },
  methods: {
    isPositive (status) {
      if (String(status).indexOf('貨件已簽收') !== -1) {
        return true
      }
    }
  }
}
</script>

<style scope>

</style>
