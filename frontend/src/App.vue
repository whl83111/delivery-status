<template lang="pug">
  #app
    .ts.centered
      .ts.action.fluid.input.myBoxShadow#input
        input(type="text", v-model="deliveryId", placeholder="輸入單號")
        button.ts.button(@click='fireSearch') 查詢
      .myBoxShadow#segment
        .ts.primary.flatted.inverted.segment
          | 目前支援 #[.ts.large.info.label 東風貨運]、#[.ts.large.info.label 黑貓宅急便]、#[.ts.large.info.label 速立達]。
      .myBoxShadow#segment
        .ts.positive.flatted.inverted.segment
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
      responseDatas: null
    }
  },
  methods: {
    fireSearch () {
      let self = this
      axios.post('/getData/', {
        deliveryId: this.deliveryId
      })
        .then((response) => {
          self.responseDatas = response.data
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
  border-radius: 2px;
}

#segment {
  margin-top: 20px;
  border-radius: 5px;

}

.myBoxShadow {
  box-shadow: 0px 0px 50px #222222;
}

#app {
  padding-bottom: 100px;
}

</style>
