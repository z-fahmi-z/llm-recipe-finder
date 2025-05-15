js = """
async () => {
    const script = document.createElement("script");
    script.onload = () =>  console.log("d3 loaded") ;
    script.src = "https://cdn.jsdelivr.net/npm/d3@7";
    document.head.appendChild(script)

    globalThis.callPopUp = () => {
        const popupOverlay = document.getElementById('popupOverlay');
        const closeButton = document.getElementById('closePopup');
        const cards = document.querySelectorAll('.recipe-card');

        cards.forEach(card => {
            card.addEventListener('click', function () {
                const title = card.querySelector('.recipe-title')?.innerText;
                const ingredients = card.querySelector('.recipe-ingredients')?.innerHTML ;
                const steps = card.querySelector('.recipe-steps')?.innerHTML;

                document.querySelector('.popup-left').innerHTML = `
                    <img alt="Image of recipe" src=""/>
                `;

                document.querySelector('.popup-right').innerHTML = `
                    <h2>${title}</h2>
                    <p style="font-weight: 500;">
                    <b>Ingredients</b><br/>
                    ${ingredients}
                    </p>
                    <p style="font-size: 14px; color: #555;">
                    <b>Steps</b><br/>
                    ${steps}
                    </p>
                `;

                popupOverlay.classList.add('active');
            });
        });

        closeButton.addEventListener('click', function () {
            popupOverlay.classList.remove('active');
        });

        popupOverlay.addEventListener('click', function (e) {
            if (e.target === popupOverlay) {
                popupOverlay.classList.remove('active');
            }
        });
    }
}
"""