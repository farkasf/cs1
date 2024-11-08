function addPost() {
    var name = prompt("Your name:", "guest");
    var message = prompt("Your complaint:", "");

    if (name && message) {
        var timestamp = new Date().toLocaleString();
        var postContent = timestamp + " <strong>[" + name + "]</strong>: " + message;

        fetch("/add_post", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ content: postContent })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const postDiv = document.createElement("div");
                postDiv.classList.add("post");
                postDiv.innerHTML = postContent;
                document.getElementById("posts").appendChild(postDiv);
            }
        });
    }
}
