

window.onload = function() {
    setTimeout(function() {
      document.getElementById("preloader").style.display = "none";
  }, 1000); // 5000 milliseconds = 5 seconds
}
  function animateAlert(){
      var inp= document.getElementsByClassName("inp")[0].value.trim();
      const alertElement= document.getElementsByClassName("meg")[0].style.display='block';
      const meg= document.getElementsByClassName("meg")[0].innerText= 'hi ' + inp +' nice to see you.';
      // window.location.assign("{ url_for( 'profile' )  }}");
      

      setTimeout(() =>{
          document.getElementsByClassName("meg")[0].style.display='none';

      },1000);
  }
