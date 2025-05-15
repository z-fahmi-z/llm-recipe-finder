from helpers.db_vector_search import load_db
from pathlib import Path
from frontend.components import card_container, card

import gradio as gr
import pandas as pd

db_path = "./vector-db"
document_path = f"{db_path}/recipe_document.txt"
separator = "\n"

csv_path = "./csv/final/indonesian_recipes.csv"

model_name = "sentence-transformers/all-MiniLM-L6-v2"
db = load_db(
    hf_embedding_model_name=model_name,
    document_path=document_path,
    separator=separator,
)

indonesian_recipes = pd.read_csv(csv_path)
indonesian_recipes.drop("FlavorProfile", inplace=True, axis=1)

def find_recipe(query, top_k=10) -> pd.DataFrame:
    recommendations = db.similarity_search(query, k=50)
    found_recipes = []
    for recipe in recommendations:
        found_recipes += [recipe.page_content.split(" x$x ")[0]]
    return indonesian_recipes[indonesian_recipes["Title"].isin(found_recipes)].head(top_k)

def get_recipe(query):
    if query.strip() == "" or query is None:
        return gr.update(value="")
    recipes = find_recipe(query, 12)
    recipe_details = []
    for index, recipe in recipes.iterrows():
        title = recipe["Title"].title()
        ingredients = recipe["Ingredients"].replace("--", "<br/>")
        steps = recipe["Steps"].replace("--", "<br/>")
        descriptions = [index, title, ingredients, steps]
        recipe_details.append(descriptions)
    return html_recipe_cards(recipe_details)

def html_recipe_cards(descriptions):
    html_card_container = card_container
    html_cards = ""
    for description in descriptions:
        html_cards += card.format(
            id = description[0],
            title = description[1],
            ingredients = description[2],
            steps = description[3]
        )
    html_card_container = html_card_container.format(cards=html_cards)
    return gr.update(value=html_card_container)

css = Path("./frontend/css/main.css").read_text()

with gr.Blocks(
    title="Dashboard",
    theme="soft",
    css=css
) as dashboard:
    with gr.Column():
        with gr.Column():
            user_input = gr.Textbox(
                label="Find Recipes",
                placeholder="A simple chicken recipe ...")
            search_button = gr.Button("Search")
        with gr.Row():
            outputs = gr.HTML("", elem_id="card-box")

    search_button.click(
        fn=get_recipe,
        inputs=user_input,
        outputs=outputs,
    )

if __name__ == "__main__":
    dashboard.launch()