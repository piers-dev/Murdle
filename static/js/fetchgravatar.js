function updateAvatar(email) {
    var hash = md5(email.trim().toLowerCase())
    document.getElementById("avatar").src=`https://www.gravatar.com/avatar/${hash}?s=200&d=https://i.imgur.com/epuDxJh.png`;
}