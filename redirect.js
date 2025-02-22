(function() {
    var redirectPath = sessionStorage.getItem("redirectPath");
    if (redirectPath) {
        sessionStorage.removeItem("redirectPath"); // Prevent looping
        window.history.replaceState({}, "", redirectPath); // Restore the original URL fix
    }
})();
