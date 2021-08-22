var header = document.querySelector("h1");
var para = document.querySelector("p");
function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];
  }
  return color
}
function changeHeaderColor(){
  colorInput = getRandomColor()
  header.style.color = colorInput;

}
function changeParagraphColor(){
  colorInput = getRandomColor()
  para.style.color = colorInput;
}
setInterval(changeHeaderColor, 1000);
setInterval(changeParagraphColor,500);
