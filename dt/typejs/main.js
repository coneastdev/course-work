let txt = {
    0:["e","u"],
    1:["x","u"],
    2:["a","u"],
    3:["m","u"],
    4:["p","u"],
    5:["l","u"],
    6:["e","u"]
};

let score = 0;

let keys = {};
let ingame = false;
let errors = 0;
let targetwds = 0;
let wds = 0;
let time = 0;
let counting = false;

function countTime() {
    if (ingame == true) {
        counting = true
        time ++;
        document.getElementById("timeout").innerText = time
        document.getElementById("wpmout").innerText = Math.floor(wds / (time / 60))
        document.getElementById("errorout").innerText = 100 - Math.floor((errors/Object.keys(keys).length) * 100)
        setTimeout(() => {
            countTime()
        }, 1000);
    } else {counting = false}
}

function start() {
    if (ingame == false) {
        ingame = true;
        txt = {};
        for (let index = 0; index < 15; index++) {
            let split = words[Math.floor(Math.random() * words.length)].split("");
            targetwds ++;
            for (let i = 0; i < split.length; i++) {
                txt[Object.keys(txt).length] = [split[i],"u"];
            }
            txt[Object.keys(txt).length] = [" ","u"];
        };
        document.getElementById("txtbox").innerHTML = "";
        for (let index = 0; index < Object.keys(txt).length; index++) {
            let ele = document.createElement("span");
            ele.innerText = txt[index][0];
            ele.id = "s-" + index;
            document.getElementById("txtbox").append(ele);
        };
        txt[Object.keys(txt).length] = ["", "fin"]
    };
};

function restart(act) {
    let txt = {
        0:["e","u"],
        1:["x","u"],
        2:["a","u"],
        3:["m","u"],
        4:["p","u"],
        5:["l","u"],
        6:["e","u"]
    };
    
    keys = {};
    ingame = false;
    errors = 0;
    targetwds = 0;
    wds = 0;
    time = 0;

    if (act == "start") {
        start();
    }
}

addEventListener("keydown", (event) => {
    let curunt = Object.keys(keys).length;
    if (txt[curunt][0] == event.key.toString()) {
        if ((curunt + 2) != Object.keys(txt).length) {
            document.getElementById("s-" + (curunt + 1)).style.textDecoration = "underline";
        };
        if (txt[curunt][1] == "u") {
            document.getElementById("s-" + curunt).style.color = "#8c8";
            txt[curunt][1] = "t";
        };
        if (event.key == " ") {
            wds ++;;
        };
        document.getElementById("s-" + curunt).style.textDecoration = "none";
        keys[curunt] = curunt;
    } else {
        errors ++;
        document.getElementById("s-" + curunt).style.color = "#c88";
        txt[curunt][1] = "f";
    };
    if (wds == targetwds) {
        ingame = false
        restart();
    };
    if (counting == false && event.keys != "M1") {
        countTime();
    };
    if (ingame == false && event.key == "r") {
        restart("start");
    };
});

addEventListener("click", (Event) => {
    start();
});