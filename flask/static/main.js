var input = new Vue({
    el: '#input',
    data: {
    deliveryId : 900078542781
    },
    methods: {
    getData: function () {
        axios.post('/getData/', {
            deliveryId: this.deliveryId
            })
            .then(function (response) {
            console.log(response.data);
            console.log(responseData['DongPoo']])
            var responseData = response.data
            if (responseData.DongPoo.error != true){
                console.log(responseData)
            }
            })
            .catch(function (error) {
            alert(error);
            });
        }
    }
});
var DongPoo = new Vue({
    el: '#DongPoo',
    data: {
        display: 'none',
        deliveryId : null
    },
    methods: {
        show : function() {

        }
    }
});