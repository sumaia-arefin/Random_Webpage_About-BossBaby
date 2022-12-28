<!doctype html>
<html>
<head>
	<title>Information Form</title>
	<meta charset="utf-8"/>
	<style type="text/css">
	body{ 
		background-color:#EEF1FF;
		font-family:"Montserrat Bold";
		
	}
	div{
		width: 600px;
		margin: 5em auto;
		padding: 50px;
		background-color:#B1E1FF;
		border-radius: 1em;
    </style>
</head>

<body>
<div>
	<h1><strong><ins>Information Form</ins></strong></h1>
	<p><h3>Please fill up the form</h3></p>
	<form action="https://formspree.io/f/mbjbodjz" method="POST">
		<p><label for="message"><strong>Name:</strong></label>
        <textarea name="message" id="message" cols="25" rows="1" placeholder="Enter your name"></textarea></p>

        <p><label for="message"><strong>Age:</strong></label>
        <textarea name="message" id="message" cols="25" rows="1" placeholder="Enter your age"></textarea></p>
		
		
		<p><strong><em>Gender:</em></strong></p>
		<p>Male<input type="radio" name="Gender"></p>
		<p>Female<input type="radio" name="Gender"></p>
        
		<p><strong><em>Your favourite go to place:</em></strong></p>
		<p>Sea-beach<input type="radio" name="place"></p>
		<p>Mountains<input type="radio" name="place"></p>
		<p>Cities<input type="radio" name="place"></p>

		<p><strong><em>Your favourite pastime:</em></strong></p>
		<p>Watching Series<input type="checkbox" name="hobby"></p>
		<p>Playing games<input type="checkbox" name="hobby"></p>
		<p>Sleeping<input type="checkbox" name="hobby"></p>
		<p>Cooking<input type="checkbox" name="hobby"></p>

		<p> <strong><em>Your favourite Colour:</em></strong>
				<select>
					<option>Black</option>
					<option>Pink</option>
					<option>White</option>
					<option>Yellow</option>
					<option>Blue</option>
				</select>
			</p>

		<p><strong><em>Did you watch the Boss Baby?</em></strong></p>
		<p>No<input type="radio" name="watch"></p>
		<p>Yes<input type="radio" name="watch"></p>
		
		<p><label for="message"><strong>Give a Message:</strong></label>
		<textarea name="message" id="message" cols="100" rows="8"></textarea></p>
        <p><input type="submit" value="Submit your form"</p>
	</form>


</div>
</body>
</html>