var rootUrl="http://127.0.0.1:5000";
var list;



login = async (id, password) => {
	let body = JSON.stringify({username: id, password: password })
	var encodedPassword = btoa(password);
	console.log(body)



	$.ajax({
		type: 'GET',
		url: rootUrl+"/Customers/search/"+id,
		dataType: "json",
		success: function(data) {
			for(i=0; i<data.length; i++){
				if(id == data[i].customerId && encodedPassword == data[i].password) {
					window.location.href="home.html";
					alert("Welcome "+data[i].firstName);
				} else {
					alert("Incorrect Login Details");
					return
				}
			}
		}
       })
	$.ajax({
		type: 'GET',
		url: rootUrl+"/Staff/search/"+id,
		dataType: "json",
		success: function(data) {
			for(i=0; i<data.length; i++){
				if(id == data[i].staffId && encodedPassword == data[i].password) {
					window.location.href="Staff.html";
					alert("Welcome "+data[i].firstName);
				} else {
					alert("Incorrect Login Details");
					return
				}
			}
		}
	})
};
