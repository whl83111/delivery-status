<template lang="pug">
  #app
    .ts.centered
    .ts.action.fluid.input.raised#input
      input(type="text", v-model="deliveryId", placeholder="輸入單號")
      button.ts.button(@click='buttonClicked') 查詢
    .ts.primary.segment
      p 目前支援東風貨運、黑貓宅急便。
    response(:response="responseIds", v-if="hasRespond")


</template>

<script>
import axios from 'axios'
import Response from './components/Response'

export default {
  name: 'app',
  components: {
    Response,
  },
  data () {
    return {
      deliveryId: null,
      hasRespond: false,
      responseIds: null,
    }
  },
  methods: {
    buttonClicked () {
      let self = this
      axios.post('/testPOST/', {
        deliveryId: this.deliveryId
      })
        .then((response) => {
          self.responseData = response.data
          self.blackCat = response.data.blackCat
          self.dongPoo = response.data.dongPoo
        })
        .catch((error) => {
          console.log(error)
        })
      this.hasRespond = true
    }
  }
}
</script>

<style scope>

#input {
  padding-top: 30px;
  padding-bottom: 20px;
}

</style>
