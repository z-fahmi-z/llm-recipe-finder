card_container = """
<div id="main-card-container">
    {cards}
</div>
<div id="popupOverlay" class="popup-overlay">
    <div class="popup-content">
        <button id="closePopup" class="close-button">&times;</button>
        <div class="popup-columns">
            <div class="popup-left">
            </div>
            <div class="popup-right">
            </div>
        </div>
    </div>
</div>
"""

card = """
<div class="recipe-card">
    <div class="recipe-image">
        Image
    </div>
    <div class="recipe-content">
        <div class="recipe-title">{title}</div>
    </div>
</div>
"""