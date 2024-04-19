import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

def regression():
    np.random.seed(0)

    #Read python-cleaned-data-file
    imdb_data=pd.read_csv('Data_Files\\Python-cleaned-file.csv',index_col=0)

    #Remove movies with less than 5000 votes
    relevant_imdb_data=imdb_data[(imdb_data['Votes']>5000)]

    print(relevant_imdb_data)
    #Convert Genre Column to Category for ease
    relevant_imdb_data["Genre"] = relevant_imdb_data["Genre"].astype("category")

    #Label Encode Genre Column
    relevant_imdb_data["Genre"] = relevant_imdb_data["Genre"].cat.codes

    #Convert Sub Genre 1 Column to Category for ease
    relevant_imdb_data["Sub Genre 1"] = relevant_imdb_data["Sub Genre 1"].astype("category")

    #Label Encode Sub Genre 1 Column
    relevant_imdb_data["Sub Genre 1"] = relevant_imdb_data["Sub Genre 1"].cat.codes

    #Convert Sub Genre 2 Column to Category for ease
    relevant_imdb_data["Sub Genre 2"] = relevant_imdb_data["Sub Genre 2"].astype("category")

    #Label Encode Sub Genre 2 Column
    relevant_imdb_data["Sub Genre 2"] = relevant_imdb_data["Sub Genre 2"].cat.codes

    #Convert Director Column to Category for ease
    relevant_imdb_data["Director"] = relevant_imdb_data["Director"].astype("category")

    #Label Encode Director Column
    relevant_imdb_data["Director"] = relevant_imdb_data["Director"].cat.codes

    #Convert Actor #1 Column to Category for ease
    relevant_imdb_data["Actor #1"] = relevant_imdb_data["Actor #1"].astype("category")

    #Label Encode Actor #1 Column
    relevant_imdb_data["Actor #1"] = relevant_imdb_data["Actor #1"].cat.codes

    #Convert Actor #2 Column to Category for ease
    relevant_imdb_data["Actor #2"] = relevant_imdb_data["Actor #2"].astype("category")

    #Label Encode Actor #2 Column
    relevant_imdb_data["Actor #2"] = relevant_imdb_data["Actor #2"].cat.codes

    #Convert Actor #3 Column to Category for ease
    relevant_imdb_data["Actor #3"] = relevant_imdb_data["Actor #3"].astype("category")

    #Label Encode Actor #3 Column
    relevant_imdb_data["Actor #3"] = relevant_imdb_data["Actor #3"].cat.codes

    #Convert Actor #4 Column to Category for ease
    relevant_imdb_data["Actor #4"] = relevant_imdb_data["Actor #4"].astype("category")

    #Label Encode Actor #4 Column
    relevant_imdb_data["Actor #4"] = relevant_imdb_data["Actor #4"].cat.codes

    #Save to be used in R
    relevant_imdb_data.to_csv('Label-Encoded-data.csv',index_label=None)

    #Get and plot correlation matrix
    corr=relevant_imdb_data.corr()
    sns.heatmap(corr,xticklabels=corr.columns.values,yticklabels=corr.columns.values,annot=True)
    plt.show()

    #Dataset for modeling
    relevant_imdb_data_modelling=relevant_imdb_data

    relevant_imdb_data_modelling=relevant_imdb_data_modelling.fillna(0)

    #Delete the least correlated features with User Rating
    del relevant_imdb_data_modelling['Director']
    del relevant_imdb_data_modelling['Genre']
    del relevant_imdb_data_modelling['Sub Genre 1']
    del relevant_imdb_data_modelling['Actor #1']
    del relevant_imdb_data_modelling['Actor #2']
    del relevant_imdb_data_modelling['Actor #3']
    del relevant_imdb_data_modelling['Actor #4']
    del relevant_imdb_data_modelling['Title']
    del relevant_imdb_data_modelling['Sub Genre 2']

    ###First Model-KNN-Works best with least no. of features###

    #Combine all the features
    features = list(zip(relevant_imdb_data_modelling['Ranking'],relevant_imdb_data_modelling['Release Year'],relevant_imdb_data_modelling['Duration(Min.)'],relevant_imdb_data_modelling['Votes']))

    #Get labels for respective features
    labels = list(relevant_imdb_data_modelling['User Rating'])

    #Divide into training and test datasets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    #Decide hyperparameter for the model(12 best found by manual testing at time of creating code)
    knn=KNeighborsRegressor(n_neighbors=12)

    #Fit the training data
    knn.fit(X_train,y_train)

    #Get the predicted data
    y_pred_knn = knn.predict(X_test)

    #Get r2 score of the model
    knn_r2=metrics.r2_score(y_test,y_pred_knn)

    #Get MAE score of the model
    #print("MAE Score:", metrics.mean_absolute_error(y_test,y_pred))

    #Get MSE score of the model
    knn_mse=metrics.mean_squared_error(y_test,y_pred_knn)

    #Get RMSE score of the model
    #print("RMSE Score:", np.sqrt(metrics.mean_absolute_error(y_test,y_pred)))

    #Get overall model score
    knn_score=knn.score(X_train,y_train)

    #Create vector of metrics for knn
    knn_metrics=[knn_r2*100,knn_mse*100,knn_score*100]

    #Get Adjusted R2 Score
    #k2= r2_score(y_test, y_pred)
    #print("Adjusted R2 Score",1-(1-r2_score(y_test, y_pred))*((len(X_test)-1)/(len(X_test)-len(X_test[0])-1)))


    ###Multiple Linear Regression###

    #Create an instance of Linear Regression
    multiple_linear_regression=LinearRegression()

    #Fit the model
    multiple_linear_regression.fit(X_train,y_train)

    #Get predicted values
    y_pred_mlr=multiple_linear_regression.predict(X_test)

    #Get r2 score of the model
    mlr_r2=metrics.r2_score(y_test,y_pred_mlr)

    #Get MSE score of the model
    mlr_mse=metrics.mean_squared_error(y_test,y_pred_mlr)

    #Get overall model score
    mlr_score=multiple_linear_regression.score(X_train,y_train)

    #Create vector of metrics for multiple linear regression
    mlr_metrics=[mlr_r2*100,mlr_mse*100,mlr_score*100]


    ###Lasso Regression###

    #Create an instance of Lasso Regression
    lasso_reg = Lasso()

    #Fit the data
    lasso_reg.fit(X_train,y_train)

    #Predict user rating
    y_pred_lass =lasso_reg.predict(X_test)

    #Get r2 score of the model
    lasso_r2=metrics.r2_score(y_test,y_pred_lass)

    #Get MSE score of the model
    lasso_mse=metrics.mean_squared_error(y_test,y_pred_lass)

    #Get Model Score
    lasso_score=lasso_reg.score(X_train,y_train)

    #Create vector of metrics for lasso regression
    lasso_metrics=[lasso_r2*100,lasso_mse*100,lasso_score*100]



    ###Random Forest Regressor###

    #Create an instance of Random Forest Regressor
    random_forest_regress = RandomForestRegressor(n_estimators = 100, random_state = 0)

    #Fit the data
    random_forest_regress.fit(X_train,y_train)

    #Predict user rating
    y_pred_r_regress =random_forest_regress.predict(X_test)

    #Get r2 score of the model
    rfr_r2=metrics.r2_score(y_test,y_pred_r_regress)

    #Get MSE score of the model
    rfr_mse=metrics.mean_squared_error(y_test,y_pred_r_regress)

    #Get Model Score
    rfr_score=random_forest_regress.score(X_train,y_train)

    #Create vector of metrics for random forest regression
    rfr_metrics=[rfr_r2*100,rfr_mse*100,rfr_score*100]

    #Create dataframe with all models and its metrics
    metrics_df=pd.DataFrame(zip(knn_metrics,mlr_metrics,lasso_metrics,rfr_metrics),index=['R2 Score','Mean Square Error','Model Score'],columns=['K-Nearest Neighbors','Lasso Regression','Multiple Linear Regression','Random Forest Regression'])

    pd.set_option('display.max_columns', None)
    print(metrics_df)





