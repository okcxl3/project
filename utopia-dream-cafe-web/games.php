<!doctype html>
<?php
header("Content-Type: text/html; charset=UTF-8");
?>
<html lang="en">
<head>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<meta charset="UTF-8"/>
	<title>Utopia Dream Cafe</title>
	<script src ="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous"/>
	<link rel="stylesheet" type="text/css" href="games.css"/>
	<link rel="stylesheet" type="text/css" href="typography_games.css"/>
	<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
</head>
<body>
	<div id="sitewrapper">
	<div id = "firstlayer_background"></div>
	<div id = "firstlayer">
		<nav class="navbar">
			<a href="index.html" class="navbar-brand pull-md-left"><img src="icons/logo.png" height="65" width="65"/></a>
			<ul class="navbar-nav pull-md-right">
				<li class= "nav-item hidden-sm-down"><a class = "nav-link link" href="index.html">OVERVIEW</a></li>
				<li class= "nav-item hidden-sm-down"><a class = "nav-link link" href="menu.html">MENU</a></li>
				<li class= "nav-item hidden-sm-down"><a class = "nav-link link" href="games.php">GAMES</a></li>
				<li class= "nav-item hidden-sm-down"><a class = "nav-link link" href="contact.html">CONTACT</a></li>
				<li id="menu_icon" class= "nav-item hidden-md-up m-t-1 pull-xs-right"><img src="icons/menuicon.png" height="40" width="40"/></li>
			</ul>
		</nav>
		<ul id="mobile_menu" class="nav hidden-md-up">
			<li class="nav-item"><a href="index.html" class="nav-link link_mobile">OVERVIEW</a></li>
			<li class="nav-item"><a href="games.php" class="nav-link link_mobile">GAMES</a></li>
			<li class="nav-item"><a href="menu.html" class="nav-link link_mobile">MENU</a></li>
			<li class="nav-item"><a href="contact.html" class="nav-link link_mobile">CONTACT</a></li>
		</ul>
		<h1 id="opening">WE ARE DELIGHTFUL TO SATISFY YOUR GAMING NEEDS</h1>
	</div>
	<div id="gamelistlayer">
		<div class="container p-y-3">
			<div class="row">
				<div class="col">
					<ul class="list-group">
						<?php
							echo "<h1 class='display1' style='text-align:center'>Games</h1>";
							$fp = fopen("games.txt","r");
							while(!feof($fp)){
								$line = fgets($fp);
								$items = explode("^",$line);
								$count=1;
								echo "<li class=list-group-item>";
								while($count < count($items)){
									if ($count ==1){
										echo "<span class='label label-primary label-pill pull-xs-right'>{$items[$count]}</span>";
									}
									else if ($count==2){
										echo "<span class='label label-info label-pill pull-xs-right'>{$items[$count]}</span>";
									}
									
									$count++;
								}
								$str=iconv('GB2312','UTF-8',$items[0]);
								echo "{$str}</li>";
							}
							fclose($fp);
						?>
						
					
					</ul>
				</div>
			</div>
		</div>
		
	</div>
	
	
	
	<footer>
		<img id="footerlogo" src="icons/logo.png" height="84" width="84"/>
		<ul id="footermenu">
			<a href="index.html"><li class="footer_menu_items">HOME</li></a>
			<a href="games.php"><li class="footer_menu_items">GAMES</li></a>
			<a href="menu.html"><li class="footer_menu_items">MENU</li></a>
			<a href="contact.html"><li class="footer_menu_items">CONTACT</li></a>
		</ul>
		<p id="copyright">&copy2012-2016 Utopia Dream Acafe. All rights reserved</p>
		<ul id="footersocial">
			<a href="https://www.instagram.com/okcxl3/"><li class="social"><img src="icons/instagram.png" height="32" width="32"/></li></a>
			<a href="https://www.facebook.com/xin.chen.712"><li class="social"><img src="icons/facebook.png" height="32" width="32"/></li></a>
		</ul>
		
	</footer>
	</div>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
	<script src="contact.js"></script>
</body>
</html>