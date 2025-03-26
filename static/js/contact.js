document.getElementById("contactForm").addEventListener("submit", function (event) {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    if (!name || !email || !message) {
        alert("יש למלא את כל השדות!");
        event.preventDefault(); // מונע משליחת הטופס
        return;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("כתובת הדוא\"ל שגויה. אנא נסה שוב.");
        event.preventDefault(); // מונע משליחת הטופס
    }
});
