INCLUDED_LOCATIONS = [
    {
        "name": "Park",
        "google_type": "park"
    },
    {
        "name": "Store",
        "google_type": "store"
    },
    {
        "name": "Restaurant",
        "google_type": "restaurant"
    },
    {
        "name": "Tourist Attracion",
        "google_type": "tourist_attraction"
    },
]

def types_to_form():
    res = ""
    for type in INCLUDED_LOCATIONS:
        # https://stackoverflow.com/questions/24322599/why-cannot-change-checkbox-color-whatever-i-do accent color
        res += "<div class=\"form-check\">"
        res += f"<input style=\"appearance: auto; accent-color: oklch(0.65 0.1 270)\"class=\"form-check-input\" name=\"{type["google_type"]}\" type=\"checkbox\" id=\"{type["google_type"]}\">"
        res += f"<label class=\"form-check-label\" for=\"{type["google_type"]}\">"
        res += type["name"]
        res += "</label>"
        res += "<br>"
        res += "</div>"
    return res

