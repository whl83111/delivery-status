var input = new Vue({
	el: '#input',
	data: {
		deliveryId: 900032521962
	},
	methods: {
		getData: function () {
			DongPoo.loding = true;
			DongPoo.visibility = 'visible';
			BlackCat.loding = true;
			BlackCat.visibility = 'visible';
			axios.post('/getData/', {
					deliveryId: this.deliveryId
				})
				.then(function (response) {
					var responseData = response.data;
					if (responseData.DongPoo.error != true) {
						DongPoo.showData(responseData.DongPoo);
					}
					if (responseData.BlackCat.error != true) {
						BlackCat.showData(responseData.BlackCat);
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
		loding: false,
		deliveryId: null,
		message: null,
		displayTable: false,
		handleDate: null,
		consigneeName: null,
		bookingDate: null,
		realCcPrice: null,
		rows: null,
	},
	components: {
		'message': {
			props: ['message'],
			template: '<div class="ts inverted info segment"><p>{{ message }}</p></div>'
		}
	},
	methods: {
		showData: function (responseData) {
			console.log(responseData);
			this.deliveryId = responseData.deliveryId;
			if (responseData.expired != true) {
				this.displayTable = true;
				this.handleDate = responseData.handleDate;
				this.consigneeName = responseData.consigneeName;
				this.bookingDate = responseData.bookingDate;
				this.realCcPrice = responseData.realCcPrice;
				this.rows = responseData.details;
			} else {
				this.displayTable = false;
				this.message = '資料已過期，無法顯示。';
			}
			this.loding = false;
		}
	}
});

var BlackCat = new Vue({
	el: '#BlackCat',
	data: {
		visibility: 'hidden',
		loding: false,
		deliveryId: null,
		message: null,
		displayTable: false,
		rows: null,
	},
	components: {
		'message': {
			props: ['message'],
			template: '<div class="ts inverted info segment"><p>{{ message }}</p></div>'
		}
	},
	methods: {
		showData: function (responseData) {
			console.log(responseData);
			this.deliveryId = responseData.deliveryId;
			if (responseData.expired != true) {
				this.displayTable = true;
				this.rows = responseData.rows;
			} else {
				this.displayTable = false;
				this.message = '資料已過期，無法顯示。';
			}
			this.loding = false;
		}
	}
});