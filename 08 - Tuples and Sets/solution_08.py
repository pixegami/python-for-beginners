"""
You are creating an application that helps your user find a restaurant according to their food preferences.
You have a set of your user's preferred foods, and sets of food being served at each restaurant.

Find the restaurant that best matches your user's food preferences.
"""

food_preference = {"🍔", "🍕", "🍤"}

restaurants = {
    "seafood_cove": {"🍤", "🍣", "🐟", "🦀"},
    "hungry_jacks": {"🍔", "🍟", "🍦", "🍕"},
    "potting_shed": {"🥦", "🥕", "🍞", "🥑"},
}

# The best match is the restaurant with the most common foods.
# Start with an empty set of best match foods and no best match restaurant.
best_match_foods = set()
best_match_restaurant = None

# Loop through each restaurant and find the best match
for restaurant_name, menu in restaurants.items():
    # Find the common foods between the restaurant's menu and the user's food preference
    common_foods = food_preference.intersection(menu)

    # If the number of common foods is greater than the current best match, update the best match
    if len(common_foods) > len(best_match_foods):
        best_match_foods = common_foods
        best_match_restaurant = restaurant_name

print(f"The best match is {best_match_restaurant} with {best_match_foods} matched foods.")




