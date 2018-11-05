// JavaScript source code
var url_pass;
function hello_world() {
    console.log("Hello");
        chrome.runtime.getBackgroundPage(function (backgroundPage) {
            var currentUrl = backgroundPage.tabURL;
            url_pass = backgroundPage.tabURL;
            //Use the url ........
            console.log(currentUrl);

        })
}

let buttonPress = document.getElementById('action')
buttonPress.addEventListener("click", hello_world);

var bgPage = chrome.extension.getBackgroundPage();

bgPage.get_url();
