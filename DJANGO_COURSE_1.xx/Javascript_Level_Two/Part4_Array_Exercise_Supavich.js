startApp = prompt("Would you like to start the roster web app?Supavich version y/n");
nameArray = []
if (startApp == "y"){
  while(true){
    option = prompt("Please select an action:add, remove, display, or quit");

    if (option =="add"){
      name = prompt("What name would you like to add?");
      nameArray.push(name);
    }
    else if(option == "remove"){
      name = prompt("What name would you like to remove?")
      for(var i=0;i< nameArray.length;i++){
        if(nameArray[i]===name){
          nameArray.splice(i,1);
        }
      }
    }
    else if(option == "display"){
      nameArray.forEach(console.log())
      for(var i =0;i<nameArray.length;i++){
        console.log(nameArray[i])
      }
    }
    else{
      break;
    }


  }
}
else{
  console.log("Thanks for using the Web App! Please refresh the page to start again");
}
