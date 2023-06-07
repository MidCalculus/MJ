var user1="MeGa_X2)2)";
var username=prompt('Please Log in. Username:',' ');
if (username==user1){
   var pass1="Yissyiss2010";
   password=prompt('If you are suppose to be here you have a password. Please type it now:',' ');
    if (password==pass1){
        alert("correct!")
     }
    else {
        window.location="wrongpassword.html";
    }
}
else {
  window.location="wrongpassword.html";
}