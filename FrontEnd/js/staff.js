var rootUrl="http://127.0.0.1:5000";

createUser = function(id, firstname, lastname, contactNumber, email, password) {
	var encodedPassword = btoa(password);
	let body = JSON.stringify({customerId: id, firstName: firstname, lastName: lastname, contactNum: contactNumber, emailAddress: email, password: encodedPassword})
	console.log(body);



	$.ajax({
		type: 'POST',
		url: rootUrl+"/Customers",
		dataType: 'json',
		contentType: "application/json",
		data: body,
		success: () => {
			alert("User Added to Database")
		},
		error: (body) => {
			console.log("Error");
			console.log(body);
		}
	})


}




$(document).ready(function(){



});


