#!/usr/bin/env python
# coding: utf-8


get_ipython().system('conda env list')


import csv # Permet de créer le fichier csv et d'y enregistrer les données
from selenium import webdriver # Permet le scraping des données
import pandas # Pour la création de la DataFrame des données
import time # Permet d'endormir le programme durant la récupération des données

\
# FRANCAIS


# =========================================== ROME ===========================================
#Panthéon
#URL = "https://www.tripadvisor.fr/Attraction_Review-g187791-d197714-Reviews-Pantheon-Rome_Lazio.html"

#Trevi fountain
#URL = "https://www.tripadvisor.fr/Attraction_Review-g187791-d190131-Reviews-Trevi_Fountain-Rome_Lazio.html"

#Coliseum
#URL = "https://www.tripadvisor.fr/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"


# =========================================== VENISE ===========================================
#Doges palace
#URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194251-Reviews-Doge_s_Palace-Venice_Veneto.html"

#Ponte di Rialto
#URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194252-Reviews-Ponte_di_Rialto-Venice_Veneto.html"

#Piazza san marco
#URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d191175-Reviews-Piazza_San_Marco-Venice_Veneto.html"


# ANGLAIS

# =========================================== ROME ===========================================
#Panthéon
#URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187791-d197714-Reviews-Pantheon-Rome_Lazio.html"

#Trevi fountain
#URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187791-d190131-Reviews-Trevi_Fountain-Rome_Lazio.html"

#Coliseum
#URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"


# =========================================== VENISE ===========================================
#Doges palace
#URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187870-d194251-Reviews-Doge_s_Palace-Venice_Veneto.html"

#Ponte di Rialto
#URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187870-d194252-Reviews-Ponte_di_Rialto-Venice_Veneto.html"

#Piazza san marco
#URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187870-d191175-Reviews-Piazza_San_Marco-Venice_Veneto.html"


# ARGENTIN


# =========================================== ROME ===========================================
#Panthéon
#URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187791-d197714-Reviews-Pantheon-Rome_Lazio.html"

#Trevi fountain
#URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187791-d190131-Reviews-Trevi_Fountain-Rome_Lazio.html"

#Coliseum
#URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"

# =========================================== VENISE ===========================================
#Doges palace
#URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187870-d194251-Reviews-Doge_s_Palace-Venice_Veneto.html"

#Ponte di Rialto
#URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187870-d194252-Reviews-Ponte_di_Rialto-Venice_Veneto.html"

#Piazza san marco
#URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187870-d191175-Reviews-Piazza_San_Marco-Venice_Veneto.html"


# ITALIEN


# =========================================== ROME ===========================================
#Panthéon
#URL = "https://www.tripadvisor.com.it/Attraction_Review-g187791-d197714-Reviews-Pantheon-Rome_Lazio.html"

#Trevi fountain
#URL = "https://www.tripadvisor.com.it/Attraction_Review-g187791-d190131-Reviews-Trevi_Fountain-Rome_Lazio.html"

#Coliseum
#URL = "https://www.tripadvisor.com.it/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"

# =========================================== VENISE ===========================================
#Doges palace
#URL = "https://www.tripadvisor.com.it/Attraction_Review-g187870-d194251-Reviews-Doge_s_Palace-Venice_Veneto.html"

#Ponte di Rialto
#URL = "https://www.tripadvisor.com.it/Attraction_Review-g187870-d194252-Reviews-Ponte_di_Rialto-Venice_Veneto.html"

#Piazza san marco
#URL = "https://www.tripadvisor.com.it/Attraction_Review-g187870-d191175-Reviews-Piazza_San_Marco-Venice_Veneto.html"

# ESPAGNOL


# =========================================== ROME ===========================================
#Panthéon
#URL = "https://www.tripadvisor.com.es/Attraction_Review-g187791-d197714-Reviews-Pantheon-Rome_Lazio.html"

#Trevi fountain
#URL = "https://www.tripadvisor.com.es/Attraction_Review-g187791-d190131-Reviews-Trevi_Fountain-Rome_Lazio.html"

#Coliseum
#URL = "https://www.tripadvisor.com.es/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"

# =========================================== VENISE ===========================================
#Doges palace
#URL = "https://www.tripadvisor.com.es/Attraction_Review-g187870-d194251-Reviews-Doge_s_Palace-Venice_Veneto.html"

#Ponte di Rialto
#URL = "https://www.tripadvisor.com.es/Attraction_Review-g187870-d194252-Reviews-Ponte_di_Rialto-Venice_Veneto.html"

#Piazza san marco
#URL = "https://www.tripadvisor.com.es/Attraction_Review-g187870-d191175-Reviews-Piazza_San_Marco-Venice_Veneto.html"


# PORTUGAIS


# =========================================== ROME ===========================================
#Panthéon
#URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187791-d197714-Reviews-Pantheon-Rome_Lazio.html"

#Trevi fountain
#URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187791-d190131-Reviews-Trevi_Fountain-Rome_Lazio.html"

#Coliseum
#URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"

# =========================================== VENISE ===========================================
#Doges palace
#URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187870-d194251-Reviews-Doge_s_Palace-Venice_Veneto.html"

#Ponte di Rialto
#URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187870-d194252-Reviews-Ponte_di_Rialto-Venice_Veneto.html"

#Piazza san marco
#URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187870-d191175-Reviews-Piazza_San_Marco-Venice_Veneto.html"



driver = webdriver.Chrome("./chromedriver.exe") # Driver Chrome
driver.get(URL) # Récupération de la page web

# Création des listes vides
ps = [] #pseudo ou nom
vl = [] #ville
py = [] #pays
dt = [] #date
tt = [] #titre
tx = [] #texte ou contenu



# Récupération des attributs des balises des avis Tripadvisor
reviews = driver.find_elements_by_xpath("//div[@class='dDwZb f M k']") # Avis entier
reviews_titre = driver.find_elements_by_xpath(".//div[@class='WlYyy cPsXC bLFSo cspKb dTqpp']") # Titre de l'avis
reviews_content = driver.find_elements_by_xpath(".//div[@class='pIRBV _T KRIav']") # Commentaire de l'avis
reviews_date = driver.find_elements_by_xpath(".//div[@class='fEDvV']") # Date de l'avis
num_page_items = min(len(reviews), 10) # Nombre d'avis sur la page
time.sleep(5) # Endormir le programme le temps de tout récupérer



# Boucle qui récupère tous les avis de la 1ère page
for i in range(num_page_items):
    # Récupère les éléments
    nom = reviews[i].find_element_by_xpath(".//span[@class='WlYyy cPsXC dTqpp']").text # Nom de l'utilisateur de l'avis i
    lieu = reviews[i].find_element_by_xpath(".//div[@class='WlYyy diXIH bQCoY']").text # Ville, pays et nombre de contributions de l'avis i
    titre = reviews_titre[i].find_element_by_xpath(".//span[@class='NejBf']").text # Titre de l'avis i
    content = reviews_content[i].find_element_by_xpath(".//div[@class='WlYyy diXIH dDKKM']").text # Commentaire de l'avis i
    date = reviews_date[i].text # Date de l'avis i
        
    # Séparation du champ lieu : récupération de la ville, du pays et du nombre de contributions
    contrib = str(''.join(filter(str.isdigit, lieu))) # Récupération du nombre dans la chaîne de caractère lieu
    lieu = lieu.rstrip(' contributions') # Suppression du mot "contributions" du lieu
    lieu = lieu.rstrip(contrib) # Suppression du nombre de contributions du lieu
    lieu = lieu.split(",") # Séparation du lieu

    if len(lieu) >= 2: # Si lieu contient ville et pays, alors récupération des variables
        if lieu[1] == '':
            ville = ""
            pays = lieu[0]
        else:
            ville = lieu[0] # Récupération de la ville
            pays = lieu[1] # Récupération du pays
            pays = pays[1:] # Suppression d'un espace
    elif len(lieu) == 1: # Si lieu contient juste le pays, alors récupération de la variable
        ville = ""
        pays = lieu[0] # Récupération du pays
    else:
        ville = ""
        pays = ""
        
    # Si nombre de contributions entre 999 et 9999, on supprime le dernier chiffre du pays
    if (int(contrib)>999 and int(contrib)<10000):
        pays = pays[:-1]
    elif (int(contrib)>9999): # Si nombre de contributions supérieur, on supprime les 2 derniers chiffres du pays
        pays = pays[:-1]
        pays = pays[:-1]
    
    # Séparation du champ date et récupération de la date seule
    date = date.split("•")
    date = date[0]
    
    # Ajout des données dans les listes
    ps.append(nom)
    vl.append(ville)
    py.append(pays)
    tt.append(titre)
    tx.append(content)
    dt.append(date)
    
# Fermeture du driver
driver.close()



# Boucle pour les pages j + 1 : mettre la dernière page +1


# FRANCAIS

# =========================== COLISEE ===========================
#for j in range(1,629): #on a 2307 pages en plus de la première car, int(23074/10)+1=2308 pages mais on ne s'intéressera qu'aux commentaires post à 2017 
    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187791-d192285-Reviews-or"+str(j)+"0-Colosseum-Rome_Lazio.html"

# ======================= PONT DU RIALTO =========================
#for j in range(1,313):
    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194252-Reviews-or"+str(j)+"0-Ponte_di_Rialto-Venice_Veneto.html"

# ====================== PLACE SAINT MARC ========================
#for j in range(1,375):
    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d191175-Reviews-or"+str(j)+"0-Piazza_San_Marco-Venice_Veneto.html"

# ===================== FONTAINE DE TREVI ========================
#for j in range(1,530): 
    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187791-d190131-Reviews-or"+str(j)+"0-Trevi_Fountain-Rome_Lazio.html"

# ========================== PANTHEON =============================
#for j in range(1,685): 
    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187791-d197714-Reviews-or"+str(j)+"0-Pantheon-Rome_Lazio.html"    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"

# ======================= PALAIS DES DOGES ========================
#for j in range(1,155): 
    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"    

    
    
    

# ANGLAIS
    
# =========================== COLISEE ===========================
#for j in range(1,2500): #on a 2307 pages en plus de la première car, int(23074/10)+1=2308 pages mais on ne s'intéressera qu'aux commentaires post à 2017 
    #URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187791-d192285-Reviews-or"+str(j)+"0-Colosseum-Rome_Lazio.html"

# ======================= PONT DU RIALTO =========================
#for j in range(1,600):
    #URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187870-d194252-Reviews-or"+str(j)+"0-Ponte_di_Rialto-Venice_Veneto.html"

# ====================== PLACE SAINT MARC ========================
#for j in range(1,600):
    #URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187870-d191175-Reviews-or"+str(j)+"0-Piazza_San_Marco-Venice_Veneto.html"

# ===================== FONTAINE DE TREVI ========================
#for j in range(470,2400): 
    #URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187791-d190131-Reviews-or"+str(j)+"0-Trevi_Fountain-Rome_Lazio.html"

# ========================== PANTHEON =============================
#for j in range(5,700): 
    #URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187791-d197714-Reviews-or"+str(j)+"0-Pantheon-Rome_Lazio.html"    

# ======================= PALAIS DES DOGES ========================
#for j in range(1,700): 
    #URL = "https://www.tripadvisor.co.uk/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"     
    
    
    
    
    
# ARGENTIN

# =========================== COLISEE ===========================
#for j in range(1,690): 
    #URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187791-d192285-Reviews-or"+str(j)+"0-Colosseum-Rome_Lazio.html"

# ======================= PONT DU RIALTO =========================
#for j in range(1,85):
    #URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187870-d194252-Reviews-or"+str(j)+"0-Ponte_di_Rialto-Venice_Veneto.html"

# ====================== PLACE SAINT MARC ========================
#for j in range(1,500):
    #URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187870-d191175-Reviews-or"+str(j)+"0-Piazza_San_Marco-Venice_Veneto.html"

# ===================== FONTAINE DE TREVI ========================
#for j in range(1,650): 
    #URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187791-d190131-Reviews-or"+str(j)+"0-Trevi_Fountain-Rome_Lazio.html"

# ========================== PANTHEON =============================
#for j in range(1,320): 
    #URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187791-d197714-Reviews-or"+str(j)+"0-Pantheon-Rome_Lazio.html"    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"

# ======================= PALAIS DES DOGES ========================
#for j in range(1,340): 
    #URL = "https://www.tripadvisor.com.ar/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"    
    




    
    
# ITALIEN

# =========================== COLISEE ===========================
#for j in range(1,700): 
    #URL = "https://www.tripadvisor.com.it/Attraction_Review-g187791-d192285-Reviews-or"+str(j)+"0-Colosseum-Rome_Lazio.html"

# ======================= PONT DU RIALTO =========================
#for j in range(1,150): #OK
    #URL = "https://www.tripadvisor.com.it/Attraction_Review-g187870-d194252-Reviews-or"+str(j)+"0-Ponte_di_Rialto-Venice_Veneto.html"

# ====================== PLACE SAINT MARC ========================
#for j in range(1,300): #OK
    #URL = "https://www.tripadvisor.com.it/Attraction_Review-g187870-d191175-Reviews-or"+str(j)+"0-Piazza_San_Marco-Venice_Veneto.html"

# ===================== FONTAINE DE TREVI ========================
#for j in range(1,450): #OK
    #URL = "https://www.tripadvisor.com.it/Attraction_Review-g187791-d190131-Reviews-or"+str(j)+"0-Trevi_Fountain-Rome_Lazio.html"

# ========================== PANTHEON =============================
#for j in range(1,400): 
    #URL = "https://www.tripadvisor.com.it/Attraction_Review-g187791-d197714-Reviews-or"+str(j)+"0-Pantheon-Rome_Lazio.html"    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"

# ======================= PALAIS DES DOGES ========================
#for j in range(1,150): #OK
    #URL = "https://www.tripadvisor.com.it/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"    
    

    
    
    
    
# ESPAGNOL

# =========================== COLISEE ===========================
#for j in range(1,700): 
    #URL = "https://www.tripadvisor.com.es/Attraction_Review-g187791-d192285-Reviews-or"+str(j)+"0-Colosseum-Rome_Lazio.html"

# ======================= PONT DU RIALTO =========================
#for j in range(1,110):
    #URL = "https://www.tripadvisor.com.es/Attraction_Review-g187870-d194252-Reviews-or"+str(j)+"0-Ponte_di_Rialto-Venice_Veneto.html"

# ====================== PLACE SAINT MARC ========================
#for j in range(1,140):
    #URL = "https://www.tripadvisor.com.es/Attraction_Review-g187870-d191175-Reviews-or"+str(j)+"0-Piazza_San_Marco-Venice_Veneto.html"

# ===================== FONTAINE DE TREVI ========================
#for j in range(1,500): 
    #URL = "https://www.tripadvisor.com.es/Attraction_Review-g187791-d190131-Reviews-or"+str(j)+"0-Trevi_Fountain-Rome_Lazio.html"

# ========================== PANTHEON =============================
#for j in range(1,400): 
    #URL = "https://www.tripadvisor.com.es/Attraction_Review-g187791-d197714-Reviews-or"+str(j)+"0-Pantheon-Rome_Lazio.html"    #URL = "https://www.tripadvisor.fr/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"

# ======================= PALAIS DES DOGES ========================
#for j in range(1,100): 
    #URL = "https://www.tripadvisor.com.es/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"    
    
    
    
    
    
    
# PORTUGAIS

# =========================== COLISEE ===========================
#for j in range(1,500): 
    #URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187791-d192285-Reviews-or"+str(j)+"0-Colosseum-Rome_Lazio.html"

# ======================= PONT DU RIALTO =========================
#for j in range(1,210):
    #URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187870-d194252-Reviews-or"+str(j)+"0-Ponte_di_Rialto-Venice_Veneto.html"

# ====================== PLACE SAINT MARC ========================
#for j in range(1,300):
    #URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187870-d191175-Reviews-or"+str(j)+"0-Piazza_San_Marco-Venice_Veneto.html"

# ===================== FONTAINE DE TREVI ========================
#for j in range(1,300): 
    #URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187791-d190131-Reviews-or"+str(j)+"0-Trevi_Fountain-Rome_Lazio.html"

# ========================== PANTHEON =============================
#for j in range(1,475): 
    #URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187791-d197714-Reviews-or"+str(j)+"0-Pantheon-Rome_Lazio.html"    

# ======================= PALAIS DES DOGES ========================
#for j in range(1,330): 
    #URL = "https://www.tripadvisor.com.pt/Attraction_Review-g187870-d194251-Reviews-or"+str(j)+"0-Doge_s_Palace-Venice_Veneto.html"    
    
    
    
    
    
    
    
    driver = webdriver.Chrome("./chromedriver.exe") # Driver Chrome
    driver.get(URL) # Récupération de la page web
    
    # Récupération des attributs des balises des avis Tripadvisor
    reviews = driver.find_elements_by_xpath("//div[@class='dDwZb f M k']") # Avis entier
    reviews_titre = driver.find_elements_by_xpath(".//div[@class='WlYyy cPsXC bLFSo cspKb dTqpp']") # Titre de l'avis
    reviews_content = driver.find_elements_by_xpath(".//div[@class='pIRBV _T KRIav']") # Commentaire de l'avis
    reviews_date = driver.find_elements_by_xpath(".//div[@class='fEDvV']") # Date de l'avis
    num_page_items = min(len(reviews), 10) # Nombre d'avis sur la page
    time.sleep(5) # Wait for reviews to load

    # Boucle qui récupère tous les avis de la jème page
    #for i in range(num_page_items):
    for i in range(len(reviews_date)):
        # Récupère les éléments
        nom = reviews[i].find_element_by_xpath(".//span[@class='WlYyy cPsXC dTqpp']").text # Nom de l'utilisateur de l'avis i
        lieu = reviews[i].find_element_by_xpath(".//div[@class='WlYyy diXIH bQCoY']").text # Ville, pays et nombre de contributions de l'avis i
        titre = reviews_titre[i].find_element_by_xpath(".//span[@class='NejBf']").text # Titre de l'avis i
        content = reviews_content[i].find_element_by_xpath(".//div[@class='WlYyy diXIH dDKKM']").text # Commentaire de l'avis i
        date = reviews_date[i].text # Date de l'avis i
        
        # Séparation du champ lieu : récupération de la ville, du pays et du nombre de contributions
        contrib = str(''.join(filter(str.isdigit, lieu))) # Récupération du nombre dans la chaîne de caractère lieu
        lieu = lieu.rstrip(' contributions') # Suppression du mot "contributions" du lieu
        lieu = lieu.rstrip(contrib) # Suppression du nombre de contributions du lieu
        lieu = lieu.split(",") # Séparation du lieu
        
        if len(lieu) >= 2: # Si lieu contient ville et pays, alors récupération des variables
            if lieu[1] == '':
                ville = ""
                pays = lieu[0]
            else:
                ville = lieu[0] # Récupération de la ville
                pays = lieu[1] # Récupération du pays
                pays = pays[1:] # Suppression d'un espace
        elif len(lieu) == 1: # Si lieu contient juste le pays, alors récupération de la variable
            ville = ""
            pays = lieu[0] # Récupération du pays
        else:
            ville = ""
            pays = ""
            
        # Si nombre de contributions entre 999 et 9999, on supprime le dernier chiffre du pays
        if int(contrib)>999 and int(contrib)<10000:
            pays = pays[:-1]
        elif int(contrib)>9999: # Si nombre de contributions supérieur, on supprime les 2 derniers chiffres du pays
                pays = pays[:-1]
                pays = pays[:-1]
        
        # Séparation du champ date et récupération de la date seule
        date = date.split("•")
        date = date[0]
        
        # Ajout des données dans les listes
        ps.append(nom)
        vl.append(ville)
        py.append(pays)
        tt.append(titre)
        tx.append(content)
        dt.append(date)
        
    # Fermeture du driver
    driver.close()



# Sauvegarde dans la DataFrame
dt = {'Pseudo' : pandas.Series(ps),
      'Ville' : pandas.Series(vl),
      'Pays' : pandas.Series(py),
      'Date' : pandas.Series(dt),
      'Titre' : pandas.Series(tt),
      'Commentaire' : pandas.Series(tx)
       }
data = pandas.DataFrame(dt)

data



# Ecriture dans le csv


# FRANCAIS

# ========================================== ROME ===========================================
#Panthéon
#data.to_csv("fr_pantheon.csv", index = False, header=True, sep=';')

#Trevi fountain
#data.to_csv("fr_fontaine_trevi.csv", index = False, header=True, sep=';')

#Coliseum
#data.to_csv("fr_colisee.csv", index = False, header=True, sep=';')


# ========================================== VENISE ===========================================
#Doges palace
#data.to_csv("fr_palais_des_doges.csv", index = False, header=True, sep=';')

#Ponte di Rialto
#data.to_csv("fr_pont_rialto.csv", index = False, header=True, sep=';')

#Piazza san marco
#data.to_csv("fr_place_saint_marc.csv", index = False, header=True, sep=';')




# ANGLAIS

# ========================================== ROME ===========================================
#Panthéon
#data.to_csv("uk_pantheon.csv", index = False, header=True, sep=';')

#Trevi fountain
#data.to_csv("uk_fontaine_trevi.csv", index = False, header=True, sep=';')

#Coliseum
#data.to_csv("uk_colisee.csv", index = False, header=True, sep=';')


# ========================================== VENISE ===========================================
#Doges palace
#data.to_csv("uk_palais_des_doges.csv", index = False, header=True, sep=';')

#Ponte di Rialto
#data.to_csv("uk_pont_rialto.csv", index = False, header=True, sep=';')

#Piazza san marco
#data.to_csv("uk_place_saint_marc.csv", index = False, header=True, sep=';')






# ARGENTIN

# ========================================== ROME ===========================================
#Panthéon
#data.to_csv("ar_pantheon.csv", index = False, header=True, sep=';')

#Trevi fountain
#data.to_csv("ar_fontaine_trevi.csv", index = False, header=True, sep=';')

#Coliseum
#data.to_csv("ar_colisee.csv", index = False, header=True, sep=';')


# ========================================== VENISE ===========================================
#Doges palace
#data.to_csv("ar_palais_des_doges.csv", index = False, header=True, sep=';')

#Ponte di Rialto
#data.to_csv("ar_pont_rialto.csv", index = False, header=True, sep=';')

#Piazza san marco
#data.to_csv("ar_place_saint_marc.csv", index = False, header=True, sep=';')






# ITALIEN

# ========================================== ROME ===========================================
#Panthéon
#data.to_csv("it_pantheon.csv", index = False, header=True, sep=';')

#Trevi fountain
#data.to_csv("it_fontaine_trevi.csv", index = False, header=True, sep=';')

#Coliseum
#data.to_csv("it_colisee.csv", index = False, header=True, sep=';')


# ========================================== VENISE ===========================================
#Doges palace
#data.to_csv("it_palais_des_doges.csv", index = False, header=True, sep=';')

#Ponte di Rialto
#data.to_csv("it_pont_rialto.csv", index = False, header=True, sep=';')

#Piazza san marco
#data.to_csv("it_place_saint_marc.csv", index = False, header=True, sep=';')







# ESPAGNOL

# ========================================== ROME ===========================================
#Panthéon
#data.to_csv("es_pantheon.csv", index = False, header=True, sep=';')

#Trevi fountain
#data.to_csv("es_fontaine_trevi.csv", index = False, header=True, sep=';')

#Coliseum
#data.to_csv("es_colisee.csv", index = False, header=True, sep=';')


# ========================================== VENISE ===========================================
#Doges palace
#data.to_csv("es_palais_des_doges.csv", index = False, header=True, sep=';')

#Ponte di Rialto
#data.to_csv("es_pont_rialto.csv", index = False, header=True, sep=';')

#Piazza san marco
#data.to_csv("es_place_saint_marc.csv", index = False, header=True, sep=';')






# PORTUGAIS

# ========================================== ROME ===========================================
#Panthéon
#data.to_csv("pt_pantheon.csv", index = False, header=True, sep=';')

#Trevi fountain
#data.to_csv("pt_fontaine_trevi.csv", index = False, header=True, sep=';')

#Coliseum
#data.to_csv("pt_colisee.csv", index = False, header=True, sep=';')


# ========================================== VENISE ===========================================
#Doges palace
#data.to_csv("pt_palais_des_doges.csv", index = False, header=True, sep=';')

#Ponte di Rialto
#data.to_csv("pt_pont_rialto.csv", index = False, header=True, sep=';')

#Piazza san marco
#data.to_csv("pt_place_saint_marc.csv", index = False, header=True, sep=';')

