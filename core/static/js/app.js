function windowScroll() {
    const e = document.getElementById("navbar");
    e && (document.body.scrollTop >= 50 || document.documentElement.scrollTop >= 50 ? e.classList.add("nav-sticky") : e.classList.remove("nav-sticky"))
}

function validateForm() {
    var e = document.forms.myForm.name.value,
        t = document.forms.myForm.email.value,
        r = document.forms.myForm.subject.value,
        n = document.forms.myForm.number.value,
        m = document.forms.myForm.comments.value;
    if (document.getElementById("error-msg").style.opacity = 0, document.getElementById("error-msg").innerHTML = "", "" == e || null == e) return document.getElementById("error-msg").innerHTML = "<div class='alert alert-danger error_message'>*Please enter a Name*</div>", fadeIn(), !1;
    if ("" == t || null == t) return document.getElementById("error-msg").innerHTML = "<div class='alert alert-danger error_message'>*Please enter a Email*</div>", fadeIn(), !1;
    if ("" == r || null == r) return document.getElementById("error-msg").innerHTML = "<div class='alert alert-danger error_message'>*Please enter a Subject*</div>", fadeIn(), !1;
    if ("" == n || null == n) return document.getElementById("error-msg").innerHTML = "<div class='alert alert-danger error_message'>*Please enter a number*</div>", fadeIn(), !1;
    if ("" == m || null == m) return document.getElementById("error-msg").innerHTML = "<div class='alert alert-danger error_message'>*Please enter a Comments*</div>", fadeIn(), !1;
    var o = new XMLHttpRequest;
    return o.onreadystatechange = function() {
        4 == this.readyState && 200 == this.status && (document.getElementById("simple-msg").innerHTML = this.responseText, document.forms.myForm.name.value = "", document.forms.myForm.email.value = "", document.forms.myForm.subject.value = "", document.forms.myForm.number.value = "", document.forms.myForm.comments.value = "")
    }, o.open("POST", "php/contact.php", !0), o.setRequestHeader("Content-type", "application/x-www-form-urlencoded"), o.send("name=" + e + "&email=" + t + "&subject=" + r + "&number=" + n + "&comments=" + m), !1
}

function fadeIn() {
    var e = document.getElementById("error-msg"),
        t = 0,
        r = setInterval(function() {
            t < 1 ? (t += .5, e.style.opacity = t) : clearInterval(r)
        }, 200)
}

function toggleSwitcher() {
    var e = document.getElementById("style-switcher");
    "-189px" === e.style.left ? e.style.left = "-0px" : e.style.left = "-189px"
}

function setColor(e) {
    document.getElementById("color-opt").href = "./css/colors/" + e + ".css", toggleSwitcher(!1)
}
window.addEventListener("scroll", e => {
    e.preventDefault(), windowScroll()
}), feather.replace();