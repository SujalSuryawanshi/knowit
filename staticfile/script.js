document.addEventListener("DOMContentLoaded", () => {
    let container = document.getElementById("news-container");
    let newsData = [];
    let currentIndex = 0;

    async function fetchNews() {
        let response = await fetch("/api/news/?category=all");
        let data = await response.json();
        newsData = data.news;
        loadNews();
    }

    function loadNews() {
        if (currentIndex >= newsData.length) {
            currentIndex = 0;
        }
        
        let news = newsData[currentIndex];
        let newsCard = document.createElement("div");
        newsCard.className = "news-card";
        newsCard.innerHTML = `
            <video src="${news.video_url}" autoplay loop></video>
            <h2>${news.title}</h2>
            <p>${news.description}</p>
        `;
        
        container.innerHTML = "";
        container.appendChild(newsCard);
    }

    window.addEventListener("wheel", (event) => {
        if (event.deltaY > 0) {
            currentIndex++;
            loadNews();
        }
    });

    fetchNews();
});
