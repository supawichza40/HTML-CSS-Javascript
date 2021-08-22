var firstName = prompt("What is your first name?")
var lastName = prompt("What is your surname?")
var age = prompt("What is your age?")
var height = prompt("What is your height in cm?")
var petName = prompt("What is your pet name?")

if (firstName[0] ===lastName[0] && age>=20 && age<=30 &&height>=170 && petName[petName.length-1] ==="y"){
  console.log("You are a spy, please read the message and follow the instruction!")

}
