#!/usr/bin/env python
# coding: utf-8

# NETTOYAGES DES FICHIERS CSV

from google.colab import drive
#drive.mount('/drive')


# 1. FICHIERS TRIPADVISOR :
import pandas as pd
from datetime import date, datetime
from datetime import datetime
from dateutil.relativedelta import *
import re
import googletrans
#from googletrans import Translator

#cette fonction est generique pour tous les fichiers 
#MAIS a faire pour chaque fichier de chaque langue en precisant : 

def traitement_pays(langue, df) :
    
    #spliter le pays et les contributions 
    df['Pays'] = df['Pays'].str.split().str.get(0)
    df['Pays'] = df['Pays'].astype(str)
    df['Pays'] = df['Pays'].str.findall("[^0-9.]", re.IGNORECASE).apply(''.join)

    #traduire le pays
    trans = Translator()
    
    
    translations = {}
    unique_elements = df["Pays"].unique()
    for element in unique_elements:
        if element is np.nan :
            translations[element] = np.nan
        else :
            translations[element] = trans.translate(element).text
    df.replace(translations, inplace = True)
    


# 1.1. FRANCAIS
#Fonction de changement du type et du format de Date
def changeDate_fr(data):
  for i in range(len(data)):
    if (type(data.Date[i]) == datetime):
      data.Date[i] = data.Date[i].date()
    elif (type(data.Date[i]) == str):
      an = data.Date[i].split()[1]
      mois = data.Date[i].split()[0]
      if (mois == 'janv.'):
        ms = 1
      elif (mois == 'févr.'):
        ms = 2
      elif (mois == 'avr.'):
        ms = 4
      elif (mois == 'juil.'):
        ms = 7
      elif (mois == 'sept.'):
        ms = 9
      elif (mois == 'oct.'):
        ms = 10
      elif (mois == 'nov.'):
        ms = 11
      elif (mois == 'déc.'):
        ms = 12
      data.Date[i] = date(int(an), ms, 1)

#COLISEE
data_colisee = pd.read_excel("fr_colisee.xlsx")
print(data_colisee.info())
print(data_colisee)

#FONTAINE DE TREVI
data_trevi = pd.read_excel("fr_fontaine_trevi.xlsx")
print(data_trevi.info())
print(data_trevi)

#PALAIS DES DOGES
data_doges = pd.read_excel("fr_palais_des_doges.xlsx")
print(data_doges.info())
print(data_doges)

#PANTHEON
data_pantheon = pd.read_excel("fr_pantheon.xlsx")
print(data_pantheon.info())
print(data_pantheon)

#PLACE SAINT MARC
data_stmarc = pd.read_excel("fr_place_saint_marc.xlsx")
print(data_stmarc.info())
print(data_stmarc)

#PONT RALTIO
data_raltio = pd.read_excel("fr_pont_rialto.xlsx")
print(data_raltio.info())
print(data_raltio)

#Applications de la fonction pour changer les dates
changeDate_fr(data_colisee)
changeDate_fr(data_doges)
changeDate_fr(data_pantheon)
changeDate_fr(data_raltio)
changeDate_fr(data_stmarc)
changeDate_fr(data_trevi)

#Ajout d'un identificateur du sites touristes sur chaque ligne
data_colisee = data_colisee.assign(Label = "colisee")
data_doges = data_doges.assign(Label = "doges")
data_pantheon = data_pantheon.assign(Label = "pantheon")
data_raltio = data_raltio.assign(Label = "pont_du_raltio")
data_stmarc = data_stmarc.assign(Label = "piazza_san_marco")
data_trevi = data_trevi.assign(Label = "fontaine_de_trevi")

#Création d'un fichier 'all'
data_all_fr = pd.concat([data_colisee,
                      data_pantheon,
                      data_trevi,
                      data_raltio,
                      data_stmarc,
                      data_doges])

#Ajout d'un identificateur de langue sur chaque ligne
data_all_fr = data_all_fr.assign(Langue = "francais")

print(data_all_fr.info())
print(data_all_fr)


# 1.2. ESPAGNOL
#Fonction de changement du type et du format de Date
def changeDate_es(data):
    for i in range(len(data)):
        if (type(data.Date[i]) == datetime):
            data.Date[i] = data.Date[i].date()
        elif (type(data.Date[i]) == str):
            an = data.Date[i].split()[2]
            mois = data.Date[i].split()[0]
            if (mois == 'ene.'):
                ms = 1
            elif (mois == 'feb.'):
                ms = 2
            elif (mois == 'mar.'):
                ms = 3
            elif (mois == 'abr.'):
                ms = 4
            elif (mois == 'may.'):
                ms = 5
            elif (mois == 'jun.'):
                ms = 6
            elif (mois == 'jul.'):
                ms = 7
            elif (mois == 'ago.'):
                ms = 8
            elif (mois == 'sept.'):
                ms = 9
            elif (mois == 'oct.'):
                ms = 10
            elif (mois == 'nov.'):
                ms = 11
            elif (mois == 'dic.'):
                ms = 12
            data.Date[i] = date(int(an), ms, 1)


#COLISEE
data_colisee = pd.read_excel("es_colisee.xlsx")
print(data_colisee.info())
print(data_colisee)

#FONTAINE DE TREVI
data_trevi = pd.read_excel("es_fontaine_trevi.xlsx")
print(data_trevi.info())
print(data_trevi)

#PALAIS DES DOGES
data_doges = pd.read_excel("es_palais_des_doges.xlsx")
print(data_doges.info())
print(data_doges)

#PANTHEON
data_pantheon = pd.read_excel("es_pantheon.xlsx")
print(data_pantheon.info())
print(data_pantheon)

#PLACE SAINT MARC
data_stmarc = pd.read_excel("es_place_saint_marc.xlsx")
print(data_stmarc.info())
print(data_stmarc)

#PONT RALTIO
data_raltio = pd.read_excel("es_pont_rialto.xlsx")
print(data_raltio.info())
print(data_raltio)


#Applications de la fonction pour changer les dates
changeDate_es(data_colisee)
changeDate_es(data_doges)
changeDate_es(data_pantheon)
changeDate_es(data_raltio)
changeDate_es(data_stmarc)
changeDate_es(data_trevi)


#Ajout d'un identificateur du sites touristes sur chaque ligne
data_colisee = data_colisee.assign(Label = "colisee")
data_doges = data_doges.assign(Label = "doges")
data_pantheon = data_pantheon.assign(Label = "pantheon")
data_raltio = data_raltio.assign(Label = "pont_du_raltio")
data_stmarc = data_stmarc.assign(Label = "piazza_san_marco")
data_trevi = data_trevi.assign(Label = "fontaine_de_trevi")

#Création d'un fichier 'all'
data_all_es = pd.concat([data_colisee,
                      data_pantheon,
                      data_trevi,
                      data_raltio,
                      data_stmarc,
                      data_doges])

#Ajout d'un identificateur de langue sur chaque ligne
data_all_es = data_all_es.assign(Langue = "espagnol")

print(data_all_es.info())
print(data_all_es)


# 1.3. Italien
#Fonction de changement du type et du format de Date
def changeDate_it(data):
    for i in range(len(data)):
        if (type(data.Date[i]) == datetime):
            data.Date[i] = data.Date[i].date()
        elif (type(data.Date[i]) == str):
            an = data.Date[i].split()[1]
            mois = data.Date[i].split()[0]
            if (mois == 'gen'):
                ms = 1
            elif (mois == 'feb'):
                ms = 2
            elif (mois == 'mar'):
                ms = 3
            elif (mois == 'apr'):
                ms = 4
            elif (mois == 'mag'):
                ms = 5
            elif (mois == 'giu'):
                ms = 6
            elif (mois == 'lug'):
                ms = 7
            elif (mois == 'ago'):
                ms = 8
            elif (mois == 'set'):
                ms = 9
            elif (mois == 'ott'):
                ms = 10
            elif (mois == 'nov'):
                ms = 11
            elif (mois == 'dic'):
                ms = 12
            data.Date[i] = date(int(an), ms, 1)


#COLISEE
data_colisee = pd.read_excel("it_colisee.xlsx")
print(data_colisee.info())
print(data_colisee)

#FONTAINE DE TREVI
data_trevi = pd.read_excel("it_fontaine_trevi.xlsx")
print(data_trevi.info())
print(data_trevi)

#PALAIS DES DOGES
data_doges = pd.read_excel("it_palais_des_doges.xlsx")
print(data_doges.info())
print(data_doges)

#PANTHEON
data_pantheon = pd.read_excel("it_pantheon.xlsx")
print(data_pantheon.info())
print(data_pantheon)

#PLACE SAINT MARC
data_stmarc = pd.read_excel("it_place_saint_marc.xlsx")
print(data_stmarc.info())
print(data_stmarc)

#PONT RALTIO
data_raltio = pd.read_excel("it_pont_rialto.xlsx")
print(data_raltio.info())
print(data_raltio)



#Applications de la fonction pour changer les dates
changeDate_it(data_colisee)
changeDate_it(data_doges)
changeDate_it(data_pantheon)
changeDate_it(data_raltio)
changeDate_it(data_stmarc)
changeDate_it(data_trevi)


#Ajout d'un identificateur du sites touristes sur chaque ligne
data_colisee = data_colisee.assign(Label = "colisee")
data_doges = data_doges.assign(Label = "doges")
data_pantheon = data_pantheon.assign(Label = "pantheon")
data_raltio = data_raltio.assign(Label = "pont_du_raltio")
data_stmarc = data_stmarc.assign(Label = "piazza_san_marco")
data_trevi = data_trevi.assign(Label = "fontaine_de_trevi")

#Création d'un fichier 'all'
data_all_it = pd.concat([data_colisee,
                      data_pantheon,
                      data_trevi,
                      data_raltio,
                      data_stmarc,
                      data_doges])

#Ajout d'un identificateur de langue sur chaque ligne
data_all_it = data_all_it.assign(Langue = "italien")

print(data_all_it.info())
print(data_all_it)


# 1.4. Portugais

#Fonction de changement du type et du format de Date
def changeDate_pt(data):
  for i in range(len(data)):
    if (type(data.Date[i]) == datetime):
      data.Date[i] = data.Date[i].date()
    elif (type(data.Date[i]) == str):
      an = data.Date[i].split()[2]
      mois = data.Date[i].split()[0]
      if (mois == 'jan'):
        ms = 1
      elif (mois == 'fev'):
        ms = 2
      elif (mois == 'mar'):
        ms = 3
      elif (mois == 'abr'):
        ms = 4
      elif (mois == 'mai'):
        ms = 5
      elif (mois == 'jun'):
        ms = 6
      elif (mois == 'jul'):
        ms = 7
      elif (mois == 'ago'):
        ms = 8
      elif (mois == 'set'):
        ms = 9
      elif (mois == 'out'):
        ms = 10
      elif (mois == 'nov'):
        ms = 11
      elif (mois == 'dez'):
        ms = 12
      data.Date[i] = date(int(an), ms, 1)


#
#COLISEE
data_colisee = pd.read_excel("pt_colisee.xlsx")
print(data_colisee.info())
print(data_colisee)

#FONTAINE DE TREVI
data_trevi = pd.read_excel("pt_fontaine_de_trevi.xlsx")
print(data_trevi.info())
print(data_trevi)

#PALAIS DES DOGES
data_doges = pd.read_excel("pt_palais_des_doges.xlsx")
print(data_doges.info())
print(data_doges)

#PANTHEON
data_pantheon = pd.read_excel("pt_pantheon.xlsx")
print(data_pantheon.info())
print(data_pantheon)

#PLACE SAINT MARC
data_stmarc = pd.read_excel("pt_place_saint_marc.xlsx")
print(data_stmarc.info())
print(data_stmarc)

#PONT RALTIO
data_raltio = pd.read_excel("pt_pont_raltio.xlsx")
print(data_raltio.info())
print(data_raltio)


#Applications de la fonction pour changer les dates
changeDate_pt(data_colisee)
changeDate_pt(data_doges)
changeDate_pt(data_pantheon)
changeDate_pt(data_raltio)
changeDate_pt(data_stmarc)
changeDate_pt(data_trevi)


#Ajout d'un identificateur du sites touristes sur chaque ligne
data_colisee = data_colisee.assign(Label = "colisee")
data_doges = data_doges.assign(Label = "doges")
data_pantheon = data_pantheon.assign(Label = "pantheon")
data_raltio = data_raltio.assign(Label = "pont_du_raltio")
data_stmarc = data_stmarc.assign(Label = "piazza_san_marco")
data_trevi = data_trevi.assign(Label = "fontaine_de_trevi")

#Création d'un fichier 'all'
data_all_pt = pd.concat([data_colisee,
                      data_pantheon,
                      data_trevi,
                      data_raltio,
                      data_stmarc,
                      data_doges])

#Ajout d'un identificateur de langue sur chaque ligne
data_all_pt = data_all_pt.assign(Langue = "portugais")

print(data_all_pt.info())
print(data_all_pt)


# 1.5. Anglais

# 
def changeDate_uk(data):
  for i in range(len(data)):
    if (type(data.Date[i]) == datetime):
      data.Date[i] = data.Date[i].date()
    elif (type(data.Date[i]) == str):
      an = data.Date[i].split()[1]
      mois = data.Date[i].split()[0]
      if (mois == 'Jan'):
        ms = 1
      elif (mois == 'Feb'):
        ms = 2
      elif (mois == 'Mar'):
        ms = 3
      elif (mois == 'Apr'):
        ms = 4
      elif (mois == 'May'):
        ms = 5
      elif (mois == 'Jun'):
        ms = 6
      elif (mois == 'Jul'):
        ms = 7
      elif (mois == 'Aug'):
        ms = 8
      elif (mois == 'Sep'):
        ms = 9
      elif (mois == 'Oct'):
        ms = 10
      elif (mois == 'Nov'):
        ms = 11
      elif (mois == 'Dec'):
        ms = 12
      data.Date[i] = date(int(an), ms, 1)



#COLISEE
data_colisee = pd.read_excel("uk_colisee.xlsx")
print(data_colisee.info())
print(data_colisee)

#FONTAINE DE TREVI
data_trevi = pd.read_excel("uk_fontaine_de_trevi.xlsx")
print(data_trevi.info())
print(data_trevi)

#PALAIS DES DOGES
data_doges = pd.read_excel("uk_palais_des_doges.xlsx")
print(data_doges.info())
print(data_doges)

#PANTHEON
data_pantheon = pd.read_excel("uk_pantheon.xlsx")
print(data_pantheon.info())
print(data_pantheon)

#PLACE SAINT MARC
data_stmarc = pd.read_excel("uk_place_saint_marc.xlsx")
print(data_stmarc.info())
print(data_stmarc)

#PONT RALTIO
data_raltio = pd.read_excel("uk_pont_raltio.xlsx")
print(data_raltio.info())
print(data_raltio)


#Applications de la fonction pour changer les dates
changeDate_uk(data_colisee)
changeDate_uk(data_doges)
changeDate_uk(data_pantheon)
changeDate_uk(data_raltio)
changeDate_uk(data_stmarc)
changeDate_uk(data_trevi)


#Ajout d'un identificateur du sites touristes sur chaque ligne
data_colisee = data_colisee.assign(Label = "colisee")
data_doges = data_doges.assign(Label = "doges")
data_pantheon = data_pantheon.assign(Label = "pantheon")
data_raltio = data_raltio.assign(Label = "pont_du_raltio")
data_stmarc = data_stmarc.assign(Label = "piazza_san_marco")
data_trevi = data_trevi.assign(Label = "fontaine_de_trevi")

#Création d'un fichier 'all'
data_all_uk = pd.concat([data_colisee,
                      data_pantheon,
                      data_trevi,
                      data_raltio,
                      data_stmarc,
                      data_doges])

#Ajout d'un identificateur de langue sur chaque ligne
data_all_uk = data_all_uk.assign(Langue = "anglais")

print(data_all_uk.info())
print(data_all_uk)


# 1.6. Argentin
#Fonction de changement du type et du format de Date
def changeDate_ar(data):
    for i in range(len(data)):
        if (type(data.Date[i]) == datetime):
            data.Date[i] = data.Date[i].date()
        elif (type(data.Date[i]) == str):
            #print(data_colisee.Date[1].split()[len(data_colisee.Date[1].split())-1])
            an = data.Date[i].split()[len(data_colisee.Date[i].split())-1]
            mois = data.Date[i].split()[0]
            if (mois == 'ene.'):
                ms = 1
            elif (mois == 'feb.'):
                ms = 2
            elif (mois == 'mar.'):
                ms = 3
            elif (mois == 'abr.'):
                ms = 4
            elif (mois == 'may.'):
                ms = 5
            elif (mois == 'jun.'):
                ms = 6
            elif (mois == 'jul.'):
                ms = 7
            elif (mois == 'ago.'):
                ms = 8
            elif (mois == 'sept.'):
                ms = 9
            elif (mois == 'oct.'):
                ms = 10
            elif (mois == 'nov.'):
                ms = 11
            elif (mois == 'dic.'):
                ms = 12
            data.Date[i] = date(int(an), ms, 1)



#COLISEE
data_colisee = pd.read_excel("ar_colisee.xlsx")
print(data_colisee.info())
print(data_colisee)

#FONTAINE DE TREVI
data_trevi = pd.read_excel("ar_fontaine_trevi.xlsx")
print(data_trevi.info())
print(data_trevi)

#PALAIS DES DOGES
data_doges = pd.read_excel("ar_palais_des_doges.xlsx")
print(data_doges.info())
print(data_doges)

#PANTHEON
data_pantheon = pd.read_excel("ar_pantheon.xlsx")
print(data_pantheon.info())
print(data_pantheon)

#PLACE SAINT MARC
data_stmarc = pd.read_excel("ar_place_saint_marc.xlsx")
print(data_stmarc.info())
print(data_stmarc)

#PONT RALTIO
data_raltio = pd.read_excel("ar_pont_rialto.xlsx")
print(data_raltio.info())
print(data_raltio)



#Applications de la fonction pour changer les dates
#changeDate_ar(data_colisee)
#changeDate_ar(data_doges)
#changeDate_ar(data_pantheon)
#changeDate_ar(data_raltio)
#changeDate_ar(data_stmarc)
#changeDate_ar(data_trevi)


# 2. FICHIERS GOOGLE_MAPS :
#import des csv 
fichiers = ["colisee_google_maps.csv",
            "fontaine_de_trevi_google_maps.csv",
            "pantheon_google_maps.csv",
            "piazza_san_marco_google_maps.csv",
            "pont_du_rialto_google_maps.csv",
            "doges_google_maps.csv"]


df = pd.DataFrame()
for i in fichiers :
    df_new = pd.read_csv(i)
    df_new["place"]=i[:-16]
    df = pd.concat([df, df_new]).reset_index(drop=True)
df.columns = ['nb','Commentaire', 'Pseudo', 'Date', 'Review Role', 'Contributions', 'Note', 'Labels']
print(df.info())



n = len(df)
vide = [None for i in range(n)] #Liste remplie de vide

# Récupération des colonnes cibles
dt = {'Pseudo' : pd.Series(df["Pseudo"]),
      'Ville' : pd.Series(vide),
      'Pays' : pd.Series(vide),
      'Date' : pd.Series(df["Date"]),
      'Titre' : pd.Series(vide),
      'Commentaire' : pd.Series(df["Commentaire"]),
      'Labels' : pd.Series(df["Labels"])
       }
data_all2 = pd.DataFrame(dt)
print(data_all2.info())




#Traitement de la date
new_date = [] # on enregistra dans un  prmier temps les dates dans une liste et on mettre par la suite la liste dans la colonne correspondante
for time in data_all2["Date"] :
    if time[:7] == "il y a " :
        #capter le numero et l'unite de temps
        if (time[7:8].isnumeric() == True | time[7:9].isnumeric() == True) :
            if time[7:9].isnumeric() == True :
                num = int(time[7:9])
                unit = time[10:]
            else : 
                num = int(time[7:8])
                unit = time[9:]
            if unit in "jours" :
                new_date.append(date((datetime.now()-relativedelta(days=num)).year,                                      (datetime.now()-relativedelta(days=num)).month,                                      (datetime.now()-relativedelta(days=num)).day))
                #new_date.append(date(2021,datetime.now().month,1))
            elif unit[1:] in "mois" :
                new_date.append(date((datetime.now()-relativedelta(months=num)).year,                                      (datetime.now()-relativedelta(months=num)).month,                                      (datetime.now()-relativedelta(months=num)).day))
                #if (mois <= int(num)):
                    #n = int(num)-mois
                    #an = an-1
                    #mois = 12-n
                #else:
                    #mois = mois-int(num)
                #new_date.append(date(an,mois,1))
            elif unit in "semaines" :
                new_date.append(date((datetime.now()-relativedelta(weeks=num)).year,                                      (datetime.now()-relativedelta(weeks=num)).month,                                      (datetime.now()-relativedelta(weeks=num)).day))
                #new_date.append(date(2021,datetime.now().month,1))
            elif unit in "ans" :
                new_date.append(date((datetime.now()-relativedelta(years=num)).year,                                      (datetime.now()-relativedelta(years=num)).month,                                      (datetime.now()-relativedelta(years=num)).day))
                #new_date.append(date(datetime.now().year-int(num),datetime.now().month,1))
        elif time[7:10] == "une": 
            num = 1
            unit = time[11:]
            if unit in "jours" :
                new_date.append(date((datetime.now()-relativedelta(days=num)).year,                                      (datetime.now()-relativedelta(days=num)).month,                                      (datetime.now()-relativedelta(days=num)).day))
                #new_date.append(date(2021,datetime.now().month,1))
            elif unit in "mois" :
                new_date.append(date((datetime.now()-relativedelta(months=num)).year,                                      (datetime.now()-relativedelta(months=num)).month,                                      (datetime.now()-relativedelta(months=num)).day))
                #new_date.append(date(2021,datetime.now().month-num,1))
            elif unit in "semaines" :
                new_date.append(date((datetime.now()-relativedelta(weeks=num)).year,                                      (datetime.now()-relativedelta(weeks=num)).month,                                      (datetime.now()-relativedelta(weeks=num)).day))
                #new_date.append(date(2021,datetime.now().month,1))
            elif unit in "ans" :
                new_date.append(date((datetime.now()-relativedelta(years=num)).year,                                      (datetime.now()-relativedelta(years=num)).month,                                      (datetime.now()-relativedelta(years=num)).day))
                #new_date.append(date(datetime.now().year-num,datetime.now().month,1))
        elif time[7:9] == "un": 
            num = 1
            unit = time[10:]
            if unit in "jours" :
                new_date.append(date((datetime.now()-relativedelta(days=num)).year,                                      (datetime.now()-relativedelta(days=num)).month,                                      (datetime.now()-relativedelta(days=num)).day))
                #new_date.append(date(2021,datetime.now().month,1))
            elif unit[1:] in "mois" :
                new_date.append(date((datetime.now()-relativedelta(months=num)).year,                                      (datetime.now()-relativedelta(months=num)).month,                                      (datetime.now()-relativedelta(months=num)).day))
                #new_date.append(date(2021,datetime.now().month-num,1))
            elif unit in "semaines" :
                new_date.append(date((datetime.now()-relativedelta(weeks=num)).year,                                      (datetime.now()-relativedelta(weeks=num)).month,                                      (datetime.now()-relativedelta(weeks=num)).day))
                #new_date.append(date(2021,datetime.now().month,1))
            elif unit in "ans" :
                new_date.append(date((datetime.now()-relativedelta(years=num)).year,                                      (datetime.now()-relativedelta(years=num)).month,                                      (datetime.now()-relativedelta(years=num)).day))
                #new_date.append(date(datetime.now().year-num,datetime.now().month,1))

data_all2["Date"] = new_date
#data_all2=data_all2.drop(['Date'], axis=1)


data_all_gm = data_all2

#Ajout d'un identificateur de langue sur chaque ligne
data_all_gm = data_trevi.assign(Langue = "francais")

print(data_all_gm.info())
print(data_all_gm)


# 3. CREATION DE LA DATAFRAME GLOBALE

data_final = pd.concat([data_all_fr,
                      data_all_es,
                      data_all_it,
                      data_all_uk,
                      data_all_pt,
                      #data_all_ar,
                      data_all_gm])

#Checking des limites des dates
#data_final.loc[(data_final.Date.year>=2017), data_final.columns].head()


print(data_final.info())
print(data_final)

#Checking des limites des dates
data_final = data_final.loc[(data_final.Date >= date(2016, 12, 31)), data_final.columns]



#Sauvergarde dans un fichier CSV
data_final.to_csv("database.csv",index = False, header=True, sep=';')


# BONUS : COVID

#Filtre Covid :
#2019-11-19 --> début
#2017-01-01 : 2019-11-18 --> avant covid
#2019-11-19 : now --> pendant covid

data_pre = data_final.loc[(data_final.Date >= date(2017, 1, 1)) & (data_final.Date <= date(2019, 11, 18)), data_final.columns]
data_pre = data_pre.assign(Covid = "avant")

data_post = data_final.loc[(data_final.Date >= date(2019, 11, 19)), data_final.columns]
data_post = data_post.assign(Covid = "apres")

data_covid = pd.concat([data_pre,data_post])
print(data_covid.info())                  
print(data_covid)


#Table de contingence Label~Covid
#Etude de l'influence du covid sur les flux touristiques
table = pd.crosstab(data_covid['Label'], 
                    data_covid['Covid'],  
                    margins = True) 
print(table)

