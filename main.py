from bs4 import BeautifulSoup

#Lecture des données HTML
f = open("recette.html", 'r')
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")
titre_h1 = soup.find("h1")
description = soup.find("div").find("p", class_="description")
image = soup.find("div", class_="info").find("img", class_="centre info")

print()
print("La source de l'image est : " , image["src"])
print("Paragraphe de description: ", description.text)
print("Titre de la page HTML : ", titre_h1.text)