import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_analysis():
    k=pd.read_csv('Data_Files\\Python-cleaned-file.csv')

    ### of Titles starting character according to Alphabets#####

    # #Create a list of alphabets
    alphabet_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # #Create a list to input the respective alphabet counts
    alphabet_count=[]
    # #Iterate through the alphabets
    for i in range(0,len(alphabet_list)):
         sub=k[k['Title'].str.startswith(alphabet_list[i])] #Filter out movie titles starting with respective alphabets
         sub_count=sub['Title'].count()  #Get individual count for each respective alphabet
         alphabet_count.append(sub_count) #Append the counts to the empty count list

    starting_with_numbers=k.shape[0]-sum(alphabet_count) #Get non-alphabet starting titles count
    alphabet_count.append(starting_with_numbers)  #Add non-alphabet starting titles count to count list
    alphabet_list.append('Numerals') #Add 'Numerals' to alphabet list
    #
    title_and_count=pd.DataFrame(list(zip(alphabet_list,alphabet_count)),columns=['Alphabet','Count']) #Create a data frame for future review
    #
    #
    title_proportion=list()
    for i in range(0,len(alphabet_count)):
         title_proportion.append((title_and_count['Count'][i]/sum(title_and_count['Count']))*100)

    title_and_count['Proportion']=title_proportion
    # #Plot a bar plot
    fig, ax=plt.subplots(figsize=(10,10))
    ax.bar(alphabet_list,alphabet_count)
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Count of movies in consecutive years')
    plt.xlabel('Initial Character of Movie Title')
    plt.ylabel('Frequency of Usage')
    plt.show() #Show the bar plot
    #
    #
    #
    # #Select movies with more than 7500 user votes and more than 6 user rating
    movies_with_more_than_10k_votes=k[(k['Votes']>7500) & (k['User Rating']>6)]
    movies_for_best=k[(k['Votes']>5000)]
    #
    # ###Year Wise count of movies###
    #
    #
    # #Get the counts of the movies year wise
    groups=movies_with_more_than_10k_votes.groupby(['Release Year']).size()
    #
    # #Remove the initial index for simplification
    year_wise_movie_count_data_frame=groups.to_frame(name='size').reset_index()
    #
    # #Plot the graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.bar(year_wise_movie_count_data_frame['Release Year'],year_wise_movie_count_data_frame['size'])
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Count of movies in consecutive years')
    plt.xlabel('Year')
    plt.ylabel('Movie Count')
    # #Show the graph
    plt.show()
    #
    #
    #
    # ###Year Wise average runtime of movies###
    #
    # #Get the average runtime of movies year wise
    groups=movies_with_more_than_10k_votes.groupby(['Release Year']).mean()
    #
    # #Remove the initial index for simplification
    year_wise_movie_runtime_data_frame=groups.reset_index()
    #
    # #Plot the graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.bar(year_wise_movie_runtime_data_frame['Release Year'],year_wise_movie_runtime_data_frame['Duration(Min.)'])
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Average runtime of movies by consecutive years')
    plt.xlabel('Year')
    plt.ylabel('Average runtime(in minutes)')
    # #Show the graph
    plt.show()
    #
    #
    # ###Year & Primary Genre Wise top movies in proportion###
    #
    # #Get the groups on basis of Year & Primary Genre
    groups=movies_with_more_than_10k_votes.groupby(['Release Year','Genre']).count()
    #
    #
    # #Remove the initial indexes for simplification
    year_and_genre_wise_movie_proportion_data_frame=groups.reset_index()
    #
    # #Create a pivot table so visualization is easier
    pivot_year_and_genre_wise_movie_proportion_data_frame=year_and_genre_wise_movie_proportion_data_frame.pivot(index='Release Year',columns='Genre',values='Actor #2')
    #
    # #Plot the stacked bar graph
    pivot_year_and_genre_wise_movie_proportion_data_frame.loc[:,:].plot.bar(stacked=True)
    #
    # #Show the graph
    plt.show()
    #
    #
    # ###Votes increase/decrease by consecutive years###
    #
    # #Group by release year
    groups=movies_with_more_than_10k_votes.groupby(by='Release Year').sum()
    #
    # #Remove the index for simplication
    year_wise_votes_data_frame=groups.reset_index()
    #
    # #Plot bar graph for Release Year Vs. No. of votes
    fig, ax=plt.subplots(figsize=(10,10))
    ax.bar(year_wise_votes_data_frame['Release Year'],year_wise_votes_data_frame['Votes'])
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('User Votes increase/decrease per year on basis of release year of movies')
    plt.xlabel('Year')
    plt.ylabel('Total User Votes')
    #
    # #Show the graph
    plt.show()
    #
    #
    #
    # ###Year Wise Top Rated Movie###
    #
    #Get the groups on basis of Year & Primary Genre
    groups=movies_with_more_than_10k_votes.groupby(['Release Year','User Rating','Title']).sum()
    #
    # #Remove the initial indexes for simplification
    year_wise_top_movies_data_frame=groups.reset_index()

    #Sort by Release Year and User Rating
    year_wise_top_movies_data_frame=year_wise_top_movies_data_frame.sort_values(["Release Year","User Rating"],ascending=(False,False))

    #Get highest rated movie per year
    groups=year_wise_top_movies_data_frame.groupby(['Release Year']).max()

    #Remove initial index for simplification
    year_wise_top_movies_data_frame=groups.reset_index()

    #Plot the bar graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.bar(year_wise_top_movies_data_frame['Release Year'],year_wise_top_movies_data_frame['User Rating'])
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Highest User rated movie per year')
    plt.xlabel('Year')
    plt.ylabel('User Rating')

    #Show the graph
    plt.show()


    #
    # ###Top movies proportion according to genre###
    #
    # #Get counts of top movies by genre
    groups=movies_with_more_than_10k_votes.groupby(['Genre']).count()

    #Remove initial index for simplification
    genre_wise_top_movies_data_frame=groups.reset_index()

    #Get sum of all the movie counts
    total_count=sum(genre_wise_top_movies_data_frame['Ranking'])

    #Get individuals counts of movie genre wise
    individual_counts=genre_wise_top_movies_data_frame['Ranking']

    #List to store individual proportion of movies genre wise
    individual_proportion=[]

    #Append inidvidual proportions to above made list genre wise
    for i in range(0,len(individual_counts)):
        individual_proportion.append((individual_counts[i]/total_count)*100)

    #Get genre names
    labels=genre_wise_top_movies_data_frame['Genre']

    #Plot the pie graph
    fig, ax=plt.subplots()
    ax.pie(x=individual_proportion,labels=labels,autopct='%1.1f%%')
    ax.axis('square')

    #Show the plot
    plt.show()



    ###Most Successful Primary Actor overall###

    #Get count of movies for each individual primary actor
    groups=movies_for_best.groupby(['Actor #1']).count()

    #Filter out actors with less than 30 movies
    groups=groups[groups['Ranking']>30]

    #Reset index for simplification
    groups=groups.reset_index()

    #Get actors and their movie counts
    actors=groups['Actor #1']
    actors_movie_count=groups['Ranking']

    #Get average user rating for each individual actor
    groups=movies_for_best.groupby(['Actor #1']).mean()

    #Remove initial index for simplification
    groups=groups.reset_index()

    #Filter out actors which have more than 30 movies
    groups=groups[groups['Actor #1'].isin(actors)]

    #Sort by descending average user rating
    groups=groups.sort_values(['User Rating'],ascending=(False))

    #Plot the graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.barh(groups['Actor #1'],groups['User Rating'],color='crimson')
    ax.invert_yaxis()
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Most Successfull Actor with at least 30 movies')
    plt.xlabel('Average User Rating')

    #Show the graph
    plt.show()


    ###Add a decade column for decade wise aggregations###
    Decade=[]
    movies_with_more_than_10k_votes=pd.DataFrame(movies_with_more_than_10k_votes)
    movies_with_more_than_10k_votes=movies_with_more_than_10k_votes[movies_with_more_than_10k_votes['Release Year'].notna()]

    #Set different values of Decade column on basis of value present in Release Year column
    movies_with_more_than_10k_votes['Decade']='Release Year Not Available'
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1920) & (movies_with_more_than_10k_votes['Release Year']>1910)]="1910-1920"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1930) & (movies_with_more_than_10k_votes['Release Year']>1920)]="1920-1930"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1940) & (movies_with_more_than_10k_votes['Release Year']>1930)]="1930-1940"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1950) & (movies_with_more_than_10k_votes['Release Year']>1940)]="1940-1950"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1960) & (movies_with_more_than_10k_votes['Release Year']>1950)]="1950-1960"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1970) & (movies_with_more_than_10k_votes['Release Year']>1960)]="1960-1970"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1980) & (movies_with_more_than_10k_votes['Release Year']>1970)]="1970-1980"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=1990) & (movies_with_more_than_10k_votes['Release Year']>1980)]="1980-1990"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=2000) & (movies_with_more_than_10k_votes['Release Year']>1990)]="1990-2000"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=2010) & (movies_with_more_than_10k_votes['Release Year']>2000)]="2000-2010"
    movies_with_more_than_10k_votes['Decade'][(movies_with_more_than_10k_votes['Release Year']<=2020) & (movies_with_more_than_10k_votes['Release Year']>2010)]="2010-2020"


    ###Decade Wise movie count###

    #Get count of movies for each individual primary actor
    groups=movies_with_more_than_10k_votes.groupby(['Decade']).count()

    #Reset index for simplification
    groups=groups.reset_index()

    #Plot the graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.bar(groups['Decade'],groups['User Rating'])
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Decade Wise Movie Count')
    plt.xlabel('Decade')
    plt.ylabel('Movie Count')

    #Show the graph
    plt.show()



    ###Most Successful Supporting Actor overall###

    #Get count of movies for each individual supporting actor
    groups=movies_for_best.groupby(['Actor #2']).count()


    #Filter out actors with less than 15 movies
    groups=groups[groups['Ranking']>15]

    #Reset index for simplification
    groups=groups.reset_index()


    #Get actors and their movie counts
    actors=groups['Actor #2']
    actors_movie_count=groups['Ranking']

    #Get average user rating for each individual actor
    groups=movies_for_best.groupby(['Actor #2']).mean()

    #Remove initial index for simplification
    groups=groups.reset_index()

    #Filter out actors which have more than 15 movies
    groups=groups[groups['Actor #2'].isin(actors)]

    #Sort by descending average user rating
    groups=groups.sort_values(['User Rating'],ascending=(False))

    #Plot the graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.barh(groups['Actor #2'],groups['User Rating'],color='crimson')
    ax.invert_yaxis()
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Most Successfull Supporting Actor with at least 30 movies')
    plt.xlabel('Average User Rating')

    #Show the graph
    plt.show()



    ###Most Successful Secondary Supporting Actor overall###

    #Get count of movies for each secondary supporting actor
    groups=k.groupby(['Actor #3']).count()

    #Filter out actors with less than 10 movies
    groups=groups[groups['Ranking']>10]

    #Reset index for simplification
    groups=groups.reset_index()


    #Get actors and their movie counts
    actors=groups['Actor #3']
    actors_movie_count=groups['Ranking']

    #Get average user rating for each individual actor
    groups=k.groupby(['Actor #3']).mean()

    #Remove initial index for simplification
    groups=groups.reset_index()

    #Filter out actors which have more than 15 movies
    groups=groups[groups['Actor #3'].isin(actors)]

    #Sort by descending average user rating
    groups=groups.sort_values(['User Rating'],ascending=(False))

    #Plot the graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.barh(groups['Actor #3'],groups['User Rating'],color='crimson')
    ax.invert_yaxis()
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Most Successfull Secondary Supporting Actor with at least 10 movies')
    plt.xlabel('Average User Rating')
    #Show the graph
    plt.show()



    ###Most Successful Director overall###

    #Get count of movies for each individual director
    groups=k.groupby(['Director']).count()


    #Filter out directors with less than 20 movies
    groups=groups[groups['Ranking']>20]

    #Reset index for simplification
    groups=groups.reset_index()


    #Get directors and their movie counts
    directors=groups['Director']
    directors_movie_count=groups['Ranking']

    #Get average user rating for each individual director
    groups=k.groupby(['Director']).mean()

    #Remove initial index for simplification
    groups=groups.reset_index()

    #Filter out directors which have more than 20 movies
    groups=groups[groups['Director'].isin(directors)]

    #Sort by descending average user rating
    groups=groups.sort_values(['User Rating'],ascending=(False))

    #Plot the graph
    fig, ax=plt.subplots(figsize=(10,10))
    ax.barh(groups['Director'],groups['User Rating'],color='crimson')
    ax.invert_yaxis()
    ax.grid(b=True,color='grey',linestyle='-',linewidth=0.3)
    ax.set_title('Most Succesfull Directors with at least 35 movies')
    plt.xlabel('Average User Rating')
    #Show the graph
    plt.show()


    ###All Genres Popularity over time###

    #Get count of movies for each individual year and genre
    groups=k.groupby(['Genre','Release Year']).count()

    #Remove initial index for simplification
    groups=groups.reset_index()

    #Get action genre rows
    action_groups=groups[groups['Genre']=='Action']

    #Get animation genre rows
    animation_groups=groups[groups['Genre']=='Animation']

    #Get biography genre rows
    biography_groups=groups[groups['Genre']=='Biography']

    #Get comedy genre rows
    comedy_groups=groups[groups['Genre']=='Comedy']

    #Get crime genre rows
    crime_groups=groups[groups['Genre']=='Crime']

    #Get drama genre rows
    drama_groups=groups[groups['Genre']=='Drama']

    #Get fantasy genre rows
    fantasy_groups=groups[groups['Genre']=='Fantasy']

    #Get horror genre rows
    horror_groups=groups[groups['Genre']=='Horror']

    #Get mystery genre rows
    mystery_groups=groups[groups['Genre']=='Mystery']

    #Get scifi genre rows
    scifi_groups=groups[groups['Genre']=='Sci-fi']

    #Get thriller genre rows
    thriller_groups=groups[groups['Genre']=='Thriller']

    #Get war genre rows
    war_groups=groups[groups['Genre']=='War']

    #Plot all subplots in a single plot
    fig, axs=plt.subplots(3,4)
    fig.suptitle('Popularity of Different Genres from 1915 to 2020')
    axs[0,0].stem(action_groups['Release Year'],action_groups['Actor #2'])
    axs[0,0].set_title('Action Genre')
    axs[0,1].stem(animation_groups['Release Year'],animation_groups['Actor #2'])
    axs[0,1].set_title('Animation Genre')
    axs[0,2].stem(biography_groups['Release Year'],biography_groups['Actor #2'])
    axs[0,2].set_title('Biography Genre')
    axs[0,3].stem(comedy_groups['Release Year'],comedy_groups['Actor #2'])
    axs[0,3].set_title('Comedy Genre')
    axs[1,0].stem(crime_groups['Release Year'],crime_groups['Actor #2'])
    axs[1,0].set_title('Crime Genre')
    axs[1,1].stem(drama_groups['Release Year'],drama_groups['Actor #2'])
    axs[1,1].set_title('Drama Genre')
    axs[1,2].stem(fantasy_groups['Release Year'],fantasy_groups['Actor #2'])
    axs[1,2].set_title('Fantasy Genre')
    axs[1,3].stem(horror_groups['Release Year'],horror_groups['Actor #2'])
    axs[1,3].set_title('Horror Genre')
    axs[2,0].stem(mystery_groups['Release Year'],mystery_groups['Actor #2'])
    axs[2,0].set_title('Mystery Genre')
    axs[2,1].stem(war_groups['Release Year'],war_groups['Actor #2'])
    axs[2,1].set_title('War Genre')
    axs[2,2].stem(scifi_groups['Release Year'],scifi_groups['Actor #2'])
    axs[2,2].set_title('Sci-fi Genre')
    axs[2,3].stem(thriller_groups['Release Year'],thriller_groups['Actor #2'])
    axs[2,3].set_title('Thriller Genre')
    plt.show()















