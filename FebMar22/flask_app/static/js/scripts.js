var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
    });
}

var imdb = keys.IMDB
var url = `https://imdb-api.com/en/API/MostPopularMovies/${imdb}`

async function getImdb() {
    var res = await fetch(url)
    var data = await res.json()
    console.log(data.items)
    for( var i = 0; i < 21; i++) {
        var node = document.createElement('div')
        node.setAttribute('class', 'column')
        var h1 = document.createElement('h1')
        var yearul = document.createElement('ul')
        var yearli = document.createElement('li')
        var year = document.createTextNode(data.items[i].year)
        yearli.appendChild(year)
        yearul.appendChild(yearli)
        var title = document.createTextNode(data.items[i].title)
        h1.appendChild(title)
        node.appendChild(h1)
        node.appendChild(yearul)
        document.getElementById('imdb').appendChild(node)
    }
}
getImdb()