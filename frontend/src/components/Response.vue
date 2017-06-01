<template lang="pug">
  div {{ response }}
  DongPoo(:responseData="responseId.dongPoo", v-if="dongPoo != null")
  BlackCat(:responseData="responseId.blackCat", v-if="blackCat == null")
</template>

<script>
import DongPoo from './DongPoo'
import BlackCat from './BlackCat'
export default {
  name: 'response',
  props: ['responseId'],
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
