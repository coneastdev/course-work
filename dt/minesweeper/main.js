let map = {
    "1":{
        "1":"#"
    }
};

let toOpen = [];

let width = 33;
let height = 15;
let tiles = 64;
let bombsPer = 25;
let bombs = 16;
let tilesOpend = 0;

function temp() {
    let rngRow = Math.floor((Math.random() * height) + 1);
    let rngCol = Math.floor((Math.random() * width) + 1);
    console.log(rngRow.toString() + rngCol.toString())
}

function openTile(row, col, deleateToOpen) {
    if (deleateToOpen == true) {toOpen.pop()};
    if (map[row.toString()][col.toString()] == "#" && document.getElementById(row + "-" + col).innerText != "🚩") {
        document.getElementById(row + "-" + col).style.backgroundColor = "#444";
        // look for bombs
        let bombsFound = 0;
        // top
        if (row > 1) {
            try {if (map[(Number(row) - 1).toString()][(Number(col) - 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("top left " + row + "-" + col + " " + error)};
            try {if (map[(Number(row) - 1).toString()][col] == "*") {bombsFound ++}} catch (error) {console.error("top middle " + row + "-" + col + " " + error)};
            try {if (map[(Number(row) - 1).toString()][(Number(col) + 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("top right " + row + "-" + col + " " + error)};
        }
        //middle
        try {if (map[row][(Number(col) - 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("middle left " + row + "-" + col + " " + error)};
        try {if (map[row][(Number(col) + 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("middle left " + row + "-" + col + " " + error)};
        // bottom
        if (row < (height)) {
            try {if (map[(Number(row) + 1).toString()][(Number(col) - 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error(row + 1 + "-" + col + 1 + " bottom left " + row + "-" + col + " " + error)};
            try {if (map[(Number(row) + 1).toString()][col] == "*") {bombsFound ++}} catch (error) {console.error(row + 1 + "-" + col + 1 + " botttom middle " + row + "-" + col + " " + error)};
            try {if (map[(Number(row) + 1).toString()][(Number(col) + 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error(row + 1 + "-" + col + 1 + " bottom right " + row + "-" + col + " " + error)};
        }
        // set bombs count
        document.getElementById(row + "-" + col).innerText = bombsFound;
        map[row][col] = bombsFound.toString();
        // check if plr has won
        tilesOpend ++;
        // open up nearby #
        if (bombsFound == 0) {
            document.getElementById(row + "-" + col).style.color = "#444";
            if (row > 1) {
                try {if (map[(Number(row) - 1).toString()][(Number(col) - 1).toString()] == "#") {toOpen.push([(Number(row) - 1).toString(), (Number(col) - 1).toString()])}} catch (error) {console.error("top left " + row + "-" + col + " " + error)};
                try {if (map[(Number(row) - 1).toString()][col] == "#") {toOpen.push([(Number(row) - 1).toString(), col])}} catch (error) {console.error("top middle " + row + "-" + col + " " + error)};
                try {if (map[(Number(row) - 1).toString()][(Number(col) + 1).toString()] == "#") {toOpen.push([(Number(row) - 1).toString(), (Number(col) + 1).toString()])}} catch (error) {console.error("top right " + row + "-" + col + " " + error)};
            }//middle
            try {if (map[row][(Number(col) - 1).toString()] == "#") {toOpen.push([row, (Number(col) - 1).toString()])}} catch (error) {console.error("middle left " + row + "-" + col + " " + error)};
            try {if (map[row][(Number(col) + 1).toString()] == "#") {toOpen.push([row, (Number(col) + 1).toString()])}} catch (error) {console.error("middle left " + row + "-" + col + " " + error)};
            // bottom
            if (row < (height)) {
                try {if (map[(Number(row) + 1).toString()][(Number(col) - 1).toString()] == "#") {toOpen.push([(Number(row) + 1).toString(), (Number(col) - 1).toString()])}} catch (error) {console.error(row + 1 + "-" + col + 1 + " bottom left " + row + "-" + col + " " + error)};
                try {if (map[(Number(row) + 1).toString()][col] == "#") {toOpen.push([(Number(row) + 1).toString(), col])}} catch (error) {console.error(row + 1 + "-" + col + 1 + " botttom middle " + row + "-" + col + " " + error)};
                try {if (map[(Number(row) + 1).toString()][(Number(col) + 1).toString()] == "#") {toOpen.push([(Number(row) + 1).toString(), (Number(col) + 1).toString()])}} catch (error) {console.error(row + 1 + "-" + col + 1 + " bottom right " + row + "-" + col + " " + error)};
            }    
        } else if (bombsFound == 1) {
            document.getElementById(row + "-" + col).style.color = "#00FF00"; // 1 = green
        } else if (bombsFound == 2) {
            document.getElementById(row + "-" + col).style.color = "#0077ff"; // 2 = blue
        } else if (bombsFound == 3) {
            document.getElementById(row + "-" + col).style.color = "#FFA500"; // 3 = orange
        } else if (bombsFound == 4) {
            document.getElementById(row + "-" + col).style.color = "#ff2323"; // 4 = red
        } else if (bombsFound == 5) {
            document.getElementById(row + "-" + col).style.color = "#bd3cbd"; // 5 = purple
        } else if (bombsFound == 6) {
            document.getElementById(row + "-" + col).style.color = "#f59a3e"; // 6 = orange
        } else if (bombsFound == 7) {
            document.getElementById(row + "-" + col).style.color = "#ffff38"; // 7 = yelow
        } else if (bombsFound == 8) {
            document.getElementById(row + "-" + col).style.color = "#ffacdd"; // 8 = pink
        }
    } else if (map[row.toString()][col.toString()] == "*" && document.getElementById(row + "-" + col).innerText != "🚩") {
        document.getElementById(row + "-" + col).style.backgroundColor = "#a55";
        document.getElementById(row + "-" + col).innerText = "💣";
    }
    // open # tiles
    if (toOpen.length > 0) {openTile(Number(toOpen[toOpen.length - 1][0]), Number(toOpen[toOpen.length - 1][1]), true)};
    // check if plr has won
    if (tilesOpend >= tiles - bombs) {alert("You win!")};
}

// make sure it does not crash browser
let openZeroLoops = 0;

function openZero() {
    openZeroLoops ++;
    // find tiles with no bombs
    let row = Math.floor((Math.random() * height) + 1);
    let col = Math.floor((Math.random() * width) + 1);
    // find bombs
    let bombsFound = 0;
    // top
    if (row > 1) {
        try {if (map[(Number(row) - 1).toString()][(Number(col) - 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("top left " + row + "-" + col + " " + error)};
        try {if (map[(Number(row) - 1).toString()][col] == "*") {bombsFound ++}} catch (error) {console.error("top middle " + row + "-" + col + " " + error)};
        try {if (map[(Number(row) - 1).toString()][(Number(col) + 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("top right " + row + "-" + col + " " + error)};
    }
    //middle
    try {if (map[row][(Number(col) - 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("middle left " + row + "-" + col + " " + error)};
    try {if (map[row][(Number(col) + 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error("middle left " + row + "-" + col + " " + error)};
    try {if (map[row][col] == "*") {bombsFound ++}} catch (error) {console.error("middle middle" + row + "-" + col + " " + error)};
    // bottom
    if (row < (height)) {
        try {if (map[(Number(row) + 1).toString()][(Number(col) - 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error(row + 1 + "-" + col + 1 + " bottom left " + row + "-" + col + " " + error)};
        try {if (map[(Number(row) + 1).toString()][col] == "*") {bombsFound ++}} catch (error) {console.error(row + 1 + "-" + col + 1 + " botttom middle " + row + "-" + col + " " + error)};
        try {if (map[(Number(row) + 1).toString()][(Number(col) + 1).toString()] == "*") {bombsFound ++}} catch (error) {console.error(row + 1 + "-" + col + 1 + " bottom right " + row + "-" + col + " " + error)};
    }
    // check it is not already open
    try {if (map[row][col] != "#") {bombsFound ++}} catch (error) {console.error("middle left " + row + "-" + col + " " + error)};
    if (bombsFound == 0) {
        openZeroLoops = 0;
        openTile(row, col);
    } else if (openZeroLoops < (tiles * 5)) {
        setTimeout(() => {
            openZero();
        }, 0.1);
    } else {
        console.log("can't find a zero")
        openZeroLoops = 0;
    }
}

function generateMap() {
    // defualt vars
    width = 8;
    height = 8;
    tiles = 64;
    bombsPer = 25;
    bombs = 16;
    tilesOpend = 0;
    // get the settings
    try {
        width = Number(document.getElementById("widthInput").value);
        height = Number(document.getElementById("heightInput").value);
        bombsPer = Number(document.getElementById("bombsInput").value);
    } catch (error) {
        console.error(error);
    }

    // check it is a valid persent
    if (bombsPer > 100) {bombsPer = 100};
    if (bombsPer < 0) {bombsPer = 0};

    // calculate the totals
    tiles = width * height;
    bombs = Math.round((tiles / 100) * bombsPer);

    // stop plr from crashing browser
    if (tiles > 2500) {
        if (prompt("Warning! A map of this size may crash your browser, please type yes to prcead and close to shrink.") == "yes") {
            alert("You have been warned...");
        } else {
            width = 50;
            height = 50;
            tiles = width * height;
            bombs = Math.round((tiles / 100) * bombsPer);
        }
    }

    // prepeare the game div
    document.getElementById("game").innerHTML = ""

    // generate buttons
    for (let row = 0; row < height; row++) {
        let newSpan = document.createElement("span");
        map[(row + 1).toString()] = {}
        for (let col = 0; col < width; col++) {
            map[(row + 1).toString()][(col + 1).toString()] = "#";
            let newBtn = document.createElement("button");
            newBtn.innerHTML = "#";
            newBtn.id = (row + 1).toString() + "-" + (col + 1).toString();
            newBtn.onclick = function() {
                openTile((row + 1).toString(), (col + 1).toString());
            }
            newBtn.addEventListener('contextmenu', function(e) {
                if (newBtn.innerText == "#") {
                    newBtn.innerText = "🚩";
                    newBtn.style.color = "#a55";
                } else if (newBtn.innerText == "🚩") {
                    newBtn.innerText = "#"
                    newBtn.style.color = "#555";
                }
                e.preventDefault();
                return false;
            }, false);
            newBtn.addEventListener('mouseenter', function() {
                // top
                document.getElementById((row) + "-" + (col)).style.borderColor = "#111";
                document.getElementById((row) + "-" + (col + 1)).style.borderColor = "#111";
                document.getElementById((row) + "-" + (col + 2)).style.borderColor = "#111";
                // middle
                document.getElementById((row  + 1) + "-" + (col)).style.borderColor = "#111";
                document.getElementById((row + 1) + "-" + (col + 1)).style.borderColor = "#111";
                document.getElementById((row + 1) + "-" + (col + 2)).style.borderColor = "#111";
                //bottom)
                document.getElementById((row + 2) + "-" + (col)).style.borderColor = "#111";
                document.getElementById((row + 2) + "-" + (col + 1)).style.borderColor = "#111";
                document.getElementById((row + 2) + "-" + (col + 2)).style.borderColor = "#111";
                return false;
            }, false);
            newBtn.addEventListener('mouseleave', function() {
                // top
                document.getElementById((row) + "-" + (col)).style.borderColor = "#333";
                document.getElementById((row) + "-" + (col + 1)).style.borderColor = "#333";
                document.getElementById((row) + "-" + (col + 2)).style.borderColor = "#333";
                // middle
                document.getElementById((row  + 1) + "-" + (col)).style.borderColor = "#333";
                document.getElementById((row + 1) + "-" + (col + 1)).style.borderColor = "#333";
                document.getElementById((row + 1) + "-" + (col + 2)).style.borderColor = "#333";
                //bottom)
                document.getElementById((row + 2) + "-" + (col)).style.borderColor = "#333";
                document.getElementById((row + 2) + "-" + (col + 1)).style.borderColor = "#333";
                document.getElementById((row + 2) + "-" + (col + 2)).style.borderColor = "#333";
                return false;
            }, false);
            newSpan.append(newBtn)
        }
        document.getElementById("game").append(newSpan)
    }

    // generate bombs
    for (let bms = 0; bms < bombs;) {
        let rngRow = Math.floor((Math.random() * height) + 1);
        let rngCol = Math.floor((Math.random() * width) + 1);
        if (map[rngRow.toString()][rngCol.toString()] == "#") {
            map[rngRow.toString()][rngCol.toString()] = "*"
            bms ++;
        }
    }
};