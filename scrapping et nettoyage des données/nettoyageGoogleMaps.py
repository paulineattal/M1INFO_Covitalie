#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from datetime import date, datetime
from dateutil.relativedelta import *


#import des csv 
fichiers = ["colisee_google_maps.csv",            "fontaine_de_trevi_google_maps.csv",             "pantheon_google_maps.csv",             "piazza_san_marco_google_maps.csv",            "pont_du_rialto_google_maps.csv",             "doges_google_maps.csv"]

df=pd.DataFrame()
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

data_all2["new_date"] = new_date
data_all2=data_all2.drop(['Date'], axis=1)

print(data_all2)

