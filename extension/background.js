chrome.webRequest.onBeforeRequest.addListener(
    function(details) { return { cancel: true }}, 
    { urls: ["# Figure out how to send blocked links from AI to here. Also be mindful of special syntax."]},
    ["blocking"]
)
