<template lang="pug">
  #app
    .ts.centered
      .ts.action.fluid.input.myBoxShadow#input
        input(type="text", v-model="deliveryId", placeholder="輸入單號")
        button.ts.button(@click='buttonClicked') 查詢
      .myBoxShadow#segment
        .ts.primary.flatted.segment
          p 目前支援東風貨運、黑貓宅急便、速立達。
      .myBoxShadow#segment
        .ts.positive.flatted.segment
          p 可批次搜尋，以","分隔。範例："123456,234567"
      Response(v-for="data in responseDatas", :key="index", :response="data")


</template>

<script>
import axios from 'axios'
import Response from './components/Response'

export default {
  name: 'app',
  components: {
    Response
  },
  data () {
    return {
      deliveryId: null,
      hasRespond: false,
      responseDatas: [
        { 'data': {
          'skyLeader': [
            { 'status': 'test', 'time': 'test' },
            { 'status': '貨件到達桃園轉運中心', 'time': '2017-03-28 09:20:45' },
            { 'status': '貨件正前往所屬站所', 'time': '2017-03 - 28 09: 21:58' },
            { 'status': '貨件已在桃園站所', 'time': '2017-03 - 28 09: 56:59' },
            { 'status': '貨件已上車，正在派送途中', 'time': '2017-03 - 28 10: 25:26' },
            { 'status': '貨件已簽收，期待下次再為您服務', 'time': '2017- 03 - 28 17: 19:40' }
          ],
          'dongPoo': {},
          'blackCat': {
            'test': 456
          }
        },
          'deliveryId': 300003938454
        }
      ]
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
  margin-top: 30px;
}

#segment {
  margin-top: 20px;
}

.myBoxShadow {
  box-shadow: 0px 0px 50px #555555;
}

#app {
  padding-bottom: 100px;
}

</style>
