function constructPlayer(data) {
    //data is name, email, word, index
    var container = document.createElement(`player${data.index}`);
    container.setAttribute("id", "player");
    hash = md5(data.email)
    container.innerHTML = `
    <div id="pfp">
    <img src="https://www.gravatar.com/avatar/${hash}?s=200&d=https://i.imgur.com/epuDxJh.png" style="width: 50px; height: 50px; border-radius: 50%;" id="avatar" ></div>
    <div id="playername" style="text-align: center;"><h3>${data.name}</h3></div>
    
    `;
    return container;
}

function rendergame(state) {
    var game = document.getElementById("Game")
    game.innerHTML = "";
    state.forEach(player => {
        
        game.appendChild(constructPlayer(player));
    });
}