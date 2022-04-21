function constructPlayer(data) {
    //data is name, email, word, index
    var container = document.createElement(`player${data.index}`);
    container.setAttribute("id", "player");
    hash = md5(data.email)
    container.innerHTML = `
    <div id="pfp">
    <img src="https://www.gravatar.com/avatar/${hash}?s=200&d=https://i.imgur.com/epuDxJh.png" style="width: 76px; height: 76px; border-radius: 50%;" id="avatar" ></div>
    <div id="playername"><h1>${data.name}</h1></div>
    
    `;
    return container;
}

function rendergame(state) {
    var game = document.getElementById("Game")
    var teststate = [{name:"Chad Broski",email:"piersmbaker@icloud.com",word:"pingu",index:1},{name:"Jimongus",email:"jim@ongus.com",word:"among",index:2}]
    teststate.forEach(player => {
        
        game.appendChild(constructPlayer(player));
    });
}