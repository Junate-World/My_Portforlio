document.addEventListener("DOMContentLoaded", function(){
  const textElement = document.getElementById("text");

  const message = "Welcome to my portfolio! Explore to know more about me and my works.";

  let index = 0;

  function type(){
    if (index < message.length){
      textElement.textContent += message.charAt(index);
      index++;

      setTimeout(type, 100); //Adjust the speed here (in milliseconds)
    }
  }

  type();
})



document.addEventListener("DOMContentLoaded", function(){
  const textElement_1 = document.getElementById("text_1");

  const message_1 = "Hi, I'm Abel Ogbonna, a Python Developer with a passion for AI and Machine Learning. I have experience in Python, JavaScript, CSS, HTML, SQL and Machine Learning.";

  let index_1 = 0;

  function type_1(){
    if (index_1 < message_1.length){
      textElement_1.textContent += message_1.charAt(index_1);
      index_1++;

      setTimeout(type_1, 100); //Adjust the speed here (in milliseconds)
    }
  }

  type_1();

});