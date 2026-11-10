from pyscript import document, when

non_metals = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "atomic_mass": 1.008},
    "He": {"name": "Helium", "atomic_number": 2, "atomic_mass": 4.0026},
    "C": {"name": "Carbon", "atomic_number": 6, "atomic_mass": 12.011},
    "N": {"name": "Nitrogen", "atomic_number": 7, "atomic_mass": 14.007},
    "O": {"name": "Oxygen", "atomic_number": 8, "atomic_mass": 15.999},
    "F": {"name": "Fluorine", "atomic_number": 9, "atomic_mass": 18.998},
    "Ne": {"name": "Neon", "atomic_number": 10, "atomic_mass": 20.180},
    "P": {"name": "Phosphorus", "atomic_number": 15, "atomic_mass": 30.974},
    "S": {"name": "Sulfur", "atomic_number": 16, "atomic_mass": 32.06},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "atomic_mass": 35.45},
    "Ar": {"name": "Argon", "atomic_number": 18, "atomic_mass": 39.948},
    "Se": {"name": "Selenium", "atomic_number": 34, "atomic_mass": 78.971},
    "Br": {"name": "Bromine", "atomic_number": 35, "atomic_mass": 79.904},
    "Kr": {"name": "Krypton", "atomic_number": 36, "atomic_mass": 83.798},
    "I": {"name": "Iodine", "atomic_number": 53, "atomic_mass": 126.90},
    "Xe": {"name": "Xenon", "atomic_number": 54, "atomic_mass": 131.29},
    "Rn": {"name": "Radon", "atomic_number": 86, "atomic_mass": 222},
    "Og": {"name": "Oganesson", "atomic_number": 118, "atomic_mass": 294}
}

def make_success_html(symbol, data):
    return f"""
        <p><strong>Element Symbol:</strong> {symbol}</p>
        <p><strong>Element Name:</strong> {data['name']}</p>
        <p><strong>Atomic Number:</strong> {data['atomic_number']}</p>
        <p><strong>Atomic Mass:</strong> {data['atomic_mass']} u</p>
    """

def make_error_html(symbol, data):
    return f"<p>Element <strong>'{symbol}'</strong> does not exist in the non-metals list.</p>"

@when("click", "#searchBtn")
def search_element(event):
    s = document.querySelector("#symbolInput").value.strip().capitalize()
    box = document.querySelector("#resultContainer")

    found = s in non_metals
    info = non_metals.get(s, {"name": "", "atomic_number": "", "atomic_mass": ""})

    funcs = {True: make_success_html, False: make_error_html}
    styles = {True: "result-card show success", False: "result-card show error"}

    box.className = styles[found]
    box.innerHTML = funcs[found](s, info)