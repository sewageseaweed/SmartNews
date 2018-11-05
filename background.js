//window.onload = function () {
    //console.log("In Onload");
    //assign_click_handler();
    
//}

function hello_world() {
    console.log("Hello");
}

var tabURL = "";

function get_url() {
    chrome.tabs.query({ active: true, currentWindow: true },
        function (arrayOfTabs) {
            var activeTab = arrayOfTabs[0];
            tabURL = activeTab.url;

        });
}

function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {

    }
};


function pass_values() {
   var pass_to_python = get_url()
                $.ajax(
                {
                    type:'POST',
                    contentType:'application/json;charset-utf-08',
                    dataType:'json',
                    url:'http://127.0.0.1:5000/pass_val?value='+pass_to_python ,
                    success:function (data) {
                        var reply=data.reply;
                        if (reply=="success")
                        {
                            return;
                    }
                }
            );
}




/*chrome.runtime.onMessage.addListener(
    function (message, sender, sendResponse) {

        chrome.tabs.query({ active: true, currentWindow: true },
            function (arrayOfTabs) {
                var activeTab = arrayOfTabs[0];
                tabURL = activeTab.url;
               
            });
    }
);*/

//document.getElementById('action', function () {
   // document.querySelector('#action').addEventListener('click', hello_world);
//});
//function assign_click_handler() {
  //  console.log()
    //document.querySelector('#action').addEventListener('click', hello_world);
//}





