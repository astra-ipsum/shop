(function() {
    var redirectPath = sessionStorage.getItem("redirectPath");
    if (redirectPath) {
        console.log("Redirecting to saved path: ", redirectPath);
        sessionStorage.removeItem("redirectPath"); // Prevent looping

        // Use history.replaceState to restore the correct URL without a full reload
        window.history.replaceState({}, "", redirectPath);
    } else {
        console.log("No redirect path found.");
    }
})();
