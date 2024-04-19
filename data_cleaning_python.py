import pandas as pd

def data_cleaning():
    #Read in the finished csv file
    k_initial=pd.read_csv('Data_Files\\Pre-cleaned-file.csv')
    #Convert it to dataframe just to be on the safe side
    k=pd.DataFrame(k_initial)

    #Remove ',' from Ranking column
    for i in range(0,len(k['Ranking'])):
        k['Ranking'][i]=str(k['Ranking'][i]).replace(',','')

    #Remove ')', '(', 'I','V','X' from Release Year column
    for i in range(0,len(k['Release Year'])):
        k['Release Year'][i]=str(k['Release Year'][i]).replace(')','')
        k['Release Year'][i]=str(k['Release Year'][i]).replace('(','')
        k['Release Year'][i] = str(k['Release Year'][i]).replace('I', '')
        k['Release Year'][i] = str(k['Release Year'][i]).replace('V', '')
        k['Release Year'][i] = str(k['Release Year'][i]).replace('X', '')

    #Remove 'min' from Duration column
    for i in range(0,len(k['Duration(Min.)'])):
        k['Duration(Min.)'][i]=str(k['Duration(Min.)'][i]).replace('min','')

    #Remove ',' from Votes column
    for i in range(0,len(k['Votes'])):
        k['Votes'][i]=str(k['Votes'][i]).replace(',','')

    #Remove white spaces from Sub Genres column
    for i in range(0,len(k['Sub Genres'])):
        k['Sub Genres'][i]=str(k['Sub Genres'][i]).strip()

    #Remove white spaces from Directors & Actors column
    for i in range(0,len(k['Directors & Actors'])):
        k['Directors & Actors'][i]=str(k['Directors & Actors'][i]).strip()

    #Split sub genres column into three columns using ',' as delimiter
    k[['Sub Genre 1','Sub Genre 2','Sub Genre 3']]=k['Sub Genres'].str.split(",", expand=True)
    #k.drop('Sub Genre3',inplace=True,axis=1)

    #Split Directors & Actors column into three columns using ':' as delimiter
    k[['Excess','Director','Actors']]=k['Directors & Actors'].str.split(":", expand=True)

    #Remove unwanted symbols and characters from Director column
    for i in range(0,len(k['Director'])):
        k['Director'][i]=str(k['Director'][i]).strip()
        k['Director'][i] = str(k['Director'][i]).replace(',', '')
        k['Director'][i] = str(k['Director'][i]).replace('|', '')
        k['Director'][i] = str(k['Director'][i]).replace('Stars', '')
        k['Director'][i] = str(k['Director'][i]).strip()

    #Remove whitspaces from Actors Column
    for i in range(0,len(k['Actors'])):
        k['Actors'][i]=str(k['Actors'][i]).strip()

    #Delete unwanted column which was made due to Director & Actors Column splitting
    k.drop('Excess',inplace=True,axis=1)

    #Split Actors column into four columns on the basis of order
    k[['Actor #1','Actor #2','Actor #3','Actor #4']]=k['Actors'].str.split(",", expand=True)

    #Remove whitespaces from the splitted column
    for i in range(0,len(k['Actor #2'])):
        k['Actor #2'][i]=str(k['Actor #2'][i]).strip()

    #Remove whitespaces from the splitted column
    for i in range(0,len(k['Actor #3'])):
        k['Actor #3'][i]=str(k['Actor #3'][i]).strip()

    #Remove whitespaces from the splitted column
    for i in range(0,len(k['Actor #4'])):
        k['Actor #4'][i]=str(k['Actor #4'][i]).strip()

    k['Sub Genre 2']=k['Sub Genre 2'].fillna('NA')

    #Remove Sub Genres Column
    k.drop('Sub Genres',inplace=True,axis=1)
    #Remove Sub Genre 3 since it has 25% missing values and it doesn't even contain very important information for the project
    k.drop('Sub Genre 3',inplace=True,axis=1)
    #Remove Directors & Actors Column
    k.drop('Directors & Actors',inplace=True,axis=1)
    #Remove Actors column
    k.drop('Actors',inplace=True,axis=1)

    #Convert data frame columns to appropriate types
    k['Ranking']=pd.to_numeric(k['Ranking'])
    k['Release Year']=pd.to_numeric(k['Release Year'],errors='ignore')
    k['Duration(Min.)']=pd.to_numeric(k['Duration(Min.)'])

    #Remove 20k duplicates
    k=k.drop_duplicates(subset="Title",keep="first")

    #Save the cleaned file to local directory for further use
    k.to_csv('Data_Files\\Python-cleaned-file.csv',index_label=None)




