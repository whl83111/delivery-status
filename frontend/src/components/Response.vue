<template lang="pug">
  .ts.flatted.card#card
    .secondary.extra.content
      .header {{ response.deliveryId }}
    .content
      .description
        DongPoo(:responseData="response.data.dongPoo", v-if="response.data.dongPoo !== null")
        BlackCat(:responseData="response.data.blackCat", v-if="response.data.blackCat !== null")
        SkyLeader(:responseData="response.data.skyLeader", v-if="response.data.skyLeader !== null")

</template>

<script>
import DongPoo from './ResponseTable/DongPoo'
import BlackCat from './ResponseTable/BlackCat'
import SkyLeader from './ResponseTable/SkyLeader'

export default {
  name: 'response',
  props: ['response'],
  components: {
    DongPoo,
    BlackCat,
    SkyLeader
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
#card {
  margin-top: 20px;
  box-shadow: 0px 0px 50px #555555;
}
</style>
