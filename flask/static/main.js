var input = new Vue({
    el: '#input',
    data: {
    deliveryId : 900032521962
    },
    methods: {
        getData: function () {
            DongPoo.loding = true;
            DongPoo.visibility = 'visible';
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
            }
    }
});
var DongPoo = new Vue({
    el: '#DongPoo',
    data: {
        visibility: 'hidden',
        loding : false,
        deliveryId : null,
        messenge : null,
        messengeDisplay : 'none',
        handleDate : null,
        consigneeName : null,
        bookingDate : null,
        realCcPrice : null,
        rows : null,
    },
    methods: {
        showData : function(responseData) {
            console.log(responseData);
            this.deliveryId = responseData.deliveryId;
            if (responseData.expired != true) {
                this.handleDate = responseData.handleDate;
                this.consigneeName = responseData.consigneeName;
                this.bookingDate = responseData.bookingDate;
                this.realCcPrice = responseData.realCcPrice;
                this.rows = responseData.details;
            }
            else {
                this.messengeDisplay = 'inline';
                this.messenge = '資料已過期，無法顯示。';
            }
            this.loding = false;
            
        }
    }
});