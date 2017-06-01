<template lang="pug">
  .card
    | {{ responseData }}

</template>

<script>
export default {
  name: 'BlackCat',
  props: ['responseData'],
  data () {
    return {
      responseData: null
    }
  }
}
</script>

<style scope>

</style>
