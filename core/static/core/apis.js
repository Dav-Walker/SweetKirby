function getusuarios(){
    fetch('https://api.escuelajs.co/api/v1/users?limit=3')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        for(let i = 0; i < 3; i++){
            document.querySelector("#review"+(i+1)).src=data[i].avatar;
            document.querySelector("#name"+(i+1)).innerHTML=data[i].name;
        }
    }).catch(function(error) {
        console.log('Requestfailed', error);
    });

    fetch('https://official-joke-api.appspot.com/jokes/ten')
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        for(let i = 0; i < 3; i++){
            document.querySelector("#joke"+(i+1)).innerHTML=data[i].setup;
            document.querySelector("#punchline"+(i+1)).innerHTML=data[i].punchline;
        }
        document.querySelector("#reviews").style.display = 'block';
    }).catch(function(error) {
        console.log('Requestfailed', error);
    });
}


