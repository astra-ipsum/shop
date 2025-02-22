(function() {
    // Check if there is a stored redirect path
    var redirectPath = sessionStorage.getItem("redirectPath");

    if (redirectPath) {
        sessionStorage.removeItem("redirectPath"); // Prevent looping

        // Use history.replaceState to restore the correct URL without a full reload
        window.history.replaceState({}, "", redirectPath);
    }
})();
