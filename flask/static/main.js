var input = new Vue({
    el: '#input',
    data: {
    deliveryId : 900032521962
    },
    methods: {
        getData: function () {
            axios.post('/getData/', {
                deliveryId: this.deliveryId
                })
                .then(function (response) {
                    var responseData = response.data;
                    if (responseData.DongPoo.error != true){
                        DongPoo.showData(responseData.DongPoo);
                }
                })
                .catch(function (error) {
                    alert(error);
                });
            },
        testtest : function () {
            alert('testest');
        }
    }
});
var DongPoo = new Vue({
    el: '#DongPoo',
    data: {
        visibility: 'hidden',
        deliveryId : null,
        messenge : null,
    },
    methods: {
        showData : function(responseData) {
            console.log(responseData);
            this.display = 'visible';
            if (responseData.expired == true) {
                this.deliveryId = responseData.deliveryId;
            }
            else {
                this.messenge = '資料已過期，無法顯示。';
            }
                
        }
    }
});