companies_ai_models_name = {
    "OpenAI": ["ChatGPT", "DALL-E", "Whisper", "GPT-4"],
    "Google": ["Alphago", "DeepMind"],
    "Meta": ["MetaGPT", "MetaGPT-4"],
    "DeepSeek": ["DeepSeek-1", "DeepSeek-2"],
}

find_model_with_name_length = {
    m_name for m_name in companies_ai_models_name if len(m_name) > 5
}

find_model_with_name = {j for i in companies_ai_models_name.values() for j in i}

# print(find_model_with_name_length)
print(find_model_with_name)


hotel_menus = {
    "Breakfast": ["Egg", "Bread", "Milk"],
    "Lunch": ["Sandwich", "Bread", "Milk"],
    "Dinner": ["Steak", "Bread", "Milk"],
    "Dessert": ["Ice Cream", "Bread", "Milk"],
}

find_item_with_name = {y for x in hotel_menus.values() for y in x}

print(find_item_with_name)
