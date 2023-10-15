nbArticles = int(input("Saisir le nombre des articles : "))
articles = []
for i in range(0, nbArticles):
    nomArticle = input(f"Article {i+1}: Nom => ")
    qte = int(input(f"Article {i+1}: Quantité => "))
    prix = float(input(f"Article {i+1}: Prix Unitaire => "))
    montantHT = (prix*qte)
    articles.insert(i, {"nom": nomArticle, "prix" : prix, "qte" : qte, "montantHT" : montantHT})

totalFacture = 0
for article in articles:
    print(f"Totale pour l'article",article["nom"],":",article["montantHT"],"DH (HT)")
    totalFacture += article["montantHT"]

totalFacture += totalFacture*0.2

print(f"Le totale de votre facture est : {totalFacture}DH (TTC)")