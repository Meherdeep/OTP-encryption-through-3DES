var app = new Vue({
  el: '.container',
  data: {
    message: ''
  },
  watch: {
    message: {
      handler: function(after,before){
        if (after.length > before.length) {
         setTimeout(function(){
            document.querySelector('.nice-input').classList.add('shake');
           setTimeout(function(){
            document.querySelector('.nice-input').classList.remove('shake'); 
           },300); 
          },200);
        }
      }
    }
  },
  computed: {
    message2: function(){
      return this.message.split('');
    }
  }
});


$(function() {
$('.pop-up').hide();
$('.pop-up').fadeIn(1000);
$('.close-button').click(function (e) {
$('.pop-up').fadeOut(700);
$('#overlay').removeClass('blur-in');
$('#overlay').addClass('blur-out');
e.stopPropagation();
});
});