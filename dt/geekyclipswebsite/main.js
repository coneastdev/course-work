const product_id =  new URLSearchParams(window.location.search).get('product');
console.log(product_id);
if (product_id != null && product_id != "") {
    console.log(product_id)
    setTimeout(() => {
        document.getElementById("hidbtn3").style.display = ""
        document.getElementById("shop").style.display = ""
        document.getElementById("featured-carousel").style.display = "none"
        document.getElementById("hidbtn").style.display = document.getElementById("hidbtn3").style.display
        document.getElementById("hidbtn2").style.display = document.getElementById("hidbtn3").style.display
        document.getElementById("productname").innerText = product_id
        document.getElementById("close-btn").style.display = "inline"
        document.getElementById("name-nav").style.display = "none"
        // document.getElementById("main").style.display = "none"
        document.getElementById(product_id + "-opt").selected = "true"
        document.getElementById("product-img").src = "./media/" + product_id + ".png" 
        document.getElementById("stock").innerText = Math.round(Math.random() * 17) + 5
        document.getElementById("buybtn").style.display = "none"
    }, 100);
} else {
    const toastLiveExample = document.getElementById('liveToast')
}

function selectfunc() {
    window.location.href = "https://coneastdev.github.io/course-work/dt/geekyclipswebsite/?product=" + document.getElementById("pro-select").value
}

function selectdealfunc() {
    document.getElementById("mysterybundlediscalimer").innerText = ""
    if (document.getElementById("deal-select").value == "mysterybundle") {
        document.getElementById("price").innerText = "£9.99"
        document.getElementById("mysterybundlediscalimer").innerText = "*DISCALIMER the mystery bundle is not random, it depends on what stock we have so the one we have the most of is sent, we try to avoid sending mutiples but it may turn out like that. No refund is eligible for these unless coverd by warenty."
        document.getElementById("stock").innerText = Math.round(Math.random() * 9) + 2
    } else if (document.getElementById("deal-select").value == "threepack") {
        document.getElementById("price").innerText = "£10.99"
        document.getElementById("stock").innerText = Math.round(Math.random() * 13) + 2
    } else if (document.getElementById("deal-select").value == "onepack") {
        document.getElementById("price").innerText = "£3.99"
        document.getElementById("stock").innerText = Math.round(Math.random() * 17) + 5
    }
    
}

setTimeout(() => {
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    toastBootstrap.show()
}, Math.round(Math.random(3000) * 10000));
