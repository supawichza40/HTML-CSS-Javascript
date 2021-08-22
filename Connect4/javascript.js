var list_tr = $("tr");

var column_1 = list_tr.eq("0");
var column_2 = list_tr.eq("1");
var column_3 = list_tr.eq("2");
var column_4 = list_tr.eq("3");
var column_5 = list_tr.eq("4");
var column_6 = list_tr.eq("5");

// column_1.find("button").eq("1").css("background-color","red");
// column_1.find("button").eq("2").css("background-color","red");
// //change specific button to red color
// column_1.find("button").css("background-color","red");
// change all the column to red color
var counter1 = 6;
var counter2 = 6;
var counter3 = 6;
var counter4 = 6;
var counter5 = 6;
var counter6 = 6;
var player = 0;


column_1.click(function(){
    if(player ==0)
    {
        player = 1;
        column_1.find("button").eq(counter1).css("background-color","red");
        column_1.find("button").eq(counter1).text("0")
        counter1 = counter1 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
    else if(player == 1){
        player = 0;
        column_1.find("button").eq(counter1).css("background-color","blue");
        column_1.find("button").eq(counter1).text("1")
        counter1 = counter1 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
})
column_2.click(function(){
    if(player ==0)
    {
        player = 1;
        column_2.find("button").eq(counter2).css("background-color","red");
        column_2.find("button").eq(counter2).text("0")
        counter2 = counter2 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
    else if(player == 1){
        player = 0;
        column_2.find("button").eq(counter2).css("background-color","blue");
        column_2.find("button").eq(counter2).text("1")
        counter2 = counter2 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
})
column_3.click(function(){
    if(player ==0)
    {
        player = 1;
        column_3.find("button").eq(counter3).css("background-color","red");
        column_3.find("button").eq(counter3).text("0")
        counter3 = counter3 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
    else if(player == 1){
        player = 0;
        column_3.find("button").eq(counter3).css("background-color","blue");
        column_3.find("button").eq(counter3).text("1")
        counter3 = counter3 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
})
column_4.click(function(){
    if(player ==0)
    {
        player = 1;
        column_4.find("button").eq(counter4).css("background-color","red");
        column_4.find("button").eq(counter4).text("0")
        counter4 = counter4 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
    else if(player == 1){
        player = 0;
        column_4.find("button").eq(counter4).css("background-color","blue");
        column_4.find("button").eq(counter4).text("1")
        counter4 = counter4 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
})
column_5.click(function(){
    if(player ==0)
    {
        player = 1;
        column_5.find("button").eq(counter5).css("background-color","red");
        column_5.find("button").eq(counter5).text("0")
        counter5 = counter5 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
    else if(player == 1){
        player = 0;
        column_5.find("button").eq(counter5).css("background-color","blue");
        column_5.find("button").eq(counter5).text("1")
        counter5 = counter5 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
})
column_6.click(function(){
    if(player ==0)
    {
        player = 1;
        column_6.find("button").eq(counter6).css("background-color","red");
        column_6.find("button").eq(counter6).text("0")
        counter6 = counter6 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
    else if(player == 1){
        player = 0;
        column_6.find("button").eq(counter6).css("background-color","blue");
        column_6.find("button").eq(counter6).text("1")
        counter6 = counter6 -1;
        checkConnect4Horizontal();
        checkVertical();
        checkSide();
        checkSideReverse();
    }
})

function checkConnect4Horizontal() {


    var c1 = -1;
    var c2 = -1;
    var c3 = -1;
    var c4 = -2;
    for(var column = 0;column<3;column++){
        for(var row =6;row>=0;row--){
            // debugger;
            c1 = window.list_tr.eq(column).find("button").eq(row).text();
            c2 = window.list_tr.eq(column+1).find("button").eq(row).text();
            c3 = window.list_tr.eq(column+2).find("button").eq(row).text();
            c4 = window.list_tr.eq(column+3).find("button").eq(row).text();
            if(c1 == c2 &&c1 == c3&&c1==c4 &&c1!==""){
                // debugger;
                if(c1 == 0){
                    console.log("Player one win")
                     alert("Player one win")
                    break;
                }
                else if(c1 == 1){
                    console.log("Player two win")
                    
                    break;
                }

            }
        }
        
    }

    //check left

    //check top left

    //check top

    //check top right

    //check right

    // check bottom right

    // check bottom

    //check bottom left
}

function checkVertical(){
    var c1 = -1;
    var c2 = -1;
    var c3 = -1;
    var c4 = -2;
    for(var column = 0;column<6;column++){
        for(var row =6;row>=3;row--){
            // debugger;
            c1 = window.list_tr.eq(column).find("button").eq(row).text();
            c2 = window.list_tr.eq(column).find("button").eq(row-1).text();
            c3 = window.list_tr.eq(column).find("button").eq(row-2).text();
            c4 = window.list_tr.eq(column).find("button").eq(row-3).text();
            if(c1 == c2 &&c1 == c3&&c1==c4 &&c1!==""){
                // debugger;
                if(c1 == 0){
                    console.log("Player one win")
                     alert("Player one win")
                    break;
                }
                else if(c1 == 1){
                    console.log("Player two win")
                    
                    break;
                }

            }
        }
        
    }
}
function checkSide(){
    var c1 = -1;
    var c2 = -1;
    var c3 = -1;
    var c4 = -2;
    for(var column = 0;column<3;column++){
        for(var row =6;row>=0;row--){
            // debugger;
            if(row<0||column>5){
                break;
            }
            c1 = window.list_tr.eq(column).find("button").eq(row).text();
            c2 = window.list_tr.eq(column+1).find("button").eq(row-1).text();
            c3 = window.list_tr.eq(column+2).find("button").eq(row-2).text();
            c4 = window.list_tr.eq(column+3).find("button").eq(row-3).text();
            if(c1 == c2 &&c1 == c3&&c1==c4 &&c1!==""){
                // debugger;
                if(c1 == 0){
                    console.log("Player one win")
                     alert("Player one win")
                    break;
                }
                else if(c1 == 1){
                    console.log("Player two win")
                    
                    break;
                }

            }
        }
        
    }
}
function checkSideReverse(){
    var c1 = -1;
    var c2 = -1;
    var c3 = -1;
    var c4 = -2;
    for(var column = 5;column>=3;column--){
        for(var row =6;row>=0;row--){
            // debugger;
            if(row<0||column<0){
                break;
            }
            c1 = window.list_tr.eq(column).find("button").eq(row).text();
            c2 = window.list_tr.eq(column-1).find("button").eq(row-1).text();
            c3 = window.list_tr.eq(column-2).find("button").eq(row-2).text();
            c4 = window.list_tr.eq(column-3).find("button").eq(row-3).text();
            if(c1 == c2 &&c1 == c3&&c1==c4 &&c1!==""){
                // debugger;
                if(c1 == 0){
                    console.log("Player one win")
                     alert("Player one win")
                    break;
                }
                else if(c1 == 1){
                    console.log("Player two win")
                    
                    break;
                }

            }
        }
        
    }
}



// column_2.click(function(){
//     column_2.find("button").eq(counter2).css("background-color","red");
//     counter2 = counter2 -1;
// })
// column_3.click(function(){
//     column_3.find("button").eq(counter3).css("background-color","red");
//     counter3 = counter3 -1;
// })
// column_4.click(function(){
//     column_4.find("button").eq(counter4).css("background-color","red");
//     counter4 = counter4 -1;
// })
// column_5.click(function(){
//     column_5.find("button").eq(counter5).css("background-color","red");
//     counter5 = counter5 -1;
// })
// column_6.click(function(){
//     column_6.find("button").eq(counter6).css("background-color","red");
//     counter6 = counter6 -1;
// })