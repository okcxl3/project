<?php
unset($response);
$response=array("name_error" => "" , "email_error" => "", "message_error" => "");
$firstname = $_POST["firstname"];
$lastname = $_POST["lastname"];
$email = $_POST["email"];
$message = $_POST["message"];
unset($invalid_email);
unset($empty_email);
unset($empty_name);
unset($empty_message);
if($firstname){
	filter($firstname);
}
else{
	$empty_name=true;
	$str="<h6 class='error'>Your full name is required</h6>";
	$response["name_error"]=$str;
}
if($lastname){
	filter($lastname);
}
else{
	$empty_name=true;
	$str="<h6 class='error'>Your full name is required</h6>";
	$response["name_error"]=$str;
}
if($email){
	$email = filter_var($email,FILTER_VALIDATE_EMAIL);
	if($email){
		
	}
	else{
		$invalid_email=true;
		$str="<h6 class='error'>Please fill in a valid email</h6>";
		$response["email_error"]=$str;
	}
}
else{
	$empty_email=true;
	$str="<h6 class='error'>Please fill in a valid email</h6>";
	$response["email_error"]=$str;
}	
if($message){
	filter($message);
}
else{
	$empty_message=true;
	$str="<h6 class='error'>Your message is required</h6>";
	$response["message_error"]=$str;
}

function filter($info){
		$info=trim($info);
		$info=stripslashes($info);
		$info=htmlspecialchars($info);
		return $info;
}

if(isset($empty_name) == false && isset($empty_message) == false && isset($empty_email) == false && isset($invalid_email)==false){
	$time = date("m-d-Y G:i:s");
	$connection = mysqli_connect("localhost","root","");
	mysqli_select_db($connection,"db");
	$query="insert into contact (firstname,lastname,email,message,time) values ('".$firstname."','".$lastname."','".$email."','".$message."','".$time."');";
	mysqli_query($connection,$query);
}

else{
	echo json_encode($response);
}
?>
