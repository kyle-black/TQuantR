from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, brier_score_loss
import pandas as pd
# assuming crossvalidation and bootstrap are custom modules
import crossvalidation
#import bootstrap
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib
import numpy as np
#import tensorflow as tf

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import brier_score_loss
#from sklearn.externals import joblib
# Import necessary keras modules
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import log_loss

#from keras.models import Sequential
#from keras.layers import Dense, Dropout
#from keras.scikit_learn import KerasClassifier
#from scikeras.wrappers import KerasClassifier
#from keras.utils import to_categorical

'''
def support_vector_classifier(df):
    
    # Data Preprocessing
    start_date = pd.to_datetime('2003-02-02')
    end_date = pd.to_datetime('2016-01-02')
    threshold = 0.7 
    
    df = df.drop(columns=['touch_lower', 'touch_upper'])
    df = df.dropna(how='all')
    df = df[60:]
    
    # Splitting data
    train_datasets, test_datasets, weights = crossvalidation.run_split_process(df)
    # train_datasets = bootstrap.sequential_bootstrap_with_rebalance(train_datasets)    
    
    feature_cols = ['Daily_Returns', 'Middle_Band', 'Upper_Band', 'Lower_Band', 'Log_Returns', 'MACD', 'Signal_Line_MACD', 'RSI', 'SpreadOC', 'SpreadLH']
    target_col = "label"
    
    all_predictions = []
    all_actuals = []
    all_preds = []
    n_components = 6
    scaler = StandardScaler()
    
    # Define a parameter grid for GridSearchCV
    
    param_grid = {
        'C': [ 50], 
        'gamma': [ 'auto'], 
        'kernel': ['linear']  
    }
    
    param_grid = {'C': [0.1, 1, 10, 100, 1000],  
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
              'kernel': ['rbf']} 

    # Training and Predicting for each split
    for train, test, weights in zip(train_datasets, test_datasets, weights):
        train = train_datasets
        test = test_datasets
        #weight = weights[-1] 
        
        
        
        X_train = train[feature_cols]
        y_train = train[target_col]
        X_test = test[feature_cols]
        y_test = test[target_col]

        # Standardize the data
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Apply PCA
        pca = PCA(n_components=n_components)
        X_train = pca.fit_transform(X_train)
        X_test = pca.transform(X_test)

        # Initialize GridSearchCV
        clf = SVC(probability=True, C=50)
        #grid_search = GridSearchCV(clf, param_grid,refit=True, verbose=3, n_jobs=-1)
        clf.fit(X_train, y_train)

        # Use the best estimator to predict
        #best_svm = grid_search.best_estimator_
        #print('best svm:',best_svm)
        probas = clf.predict_proba(X_test)

        #y_pred = (probas[:, 1] >= threshold).astype(int)

        max_proba_indices = np.argmax(probas, axis=1)

        predicted_classes = clf.classes_[max_proba_indices]
        y_pred = predicted_classes

        # Print and store results
        print('######################')
        print('probas:', probas)
        print(classification_report(y_test, y_pred, zero_division=1))
        print('Confusion Matrix:', confusion_matrix(y_test, y_pred))
        predicted_probabilities = probas[:, 1]
        print('predicted_probs:', predicted_probabilities)
        print('y_test:', y_test)
        brier_score = brier_score_loss(y_test, predicted_probabilities)
        print('Brier Score:', brier_score)

        predictions_df = pd.DataFrame({
            'Actual': y_test,
            'Predictions': y_pred
        })
        all_predictions.append(predictions_df)

        all_actuals.extend(y_test.tolist())
        all_preds.extend(y_pred.tolist())
        print('###########################')

        print('classes---> ',clf.classes_)


    # After processing all splits, compute overall metrics
    '''
   # joblib.dump(clf, 'models/EURUSD/random_forest_model_up_SPY.pkl')
   # joblib.dump(pca, 'models/EURUSD/pca_transformation_up_SPY.pkl')
    #joblib.dump(scaler, 'models/EURUSD/scaler_SPY.pkl')

#    file_input = "/mnt/volume_nyc1_02"
'''
    #joblib.dump(clf, f'{file_input}/models/EURUSD/support_vector_classifier_up_EURUSD.pkl')
    #joblib.dump(pca, f'{file_input}/models/EURUSD/pca_transformation_up_EURUSD.pkl')
    #joblib.dump(scaler, f'{file_input}/models/EURUSD/scaler_EURUSD.pkl')
    
    print(predictions_df)
    print("\nOverall Classification Report:")
    print(classification_report(all_actuals, all_preds, zero_division=1))
    print('Overall Confusion Matrix:', confusion_matrix(all_actuals, all_preds))

    
    # Combining all predictions and saving
    final_predictions_df = pd.concat(all_predictions)
    final_predictions_df.to_csv('predictions.csv', index=False)
'''
'''
def support_vector_classifier(df):
    
    # Data Preprocessing
    start_date = pd.to_datetime('2003-02-02')
    end_date = pd.to_datetime('2016-01-02')
    
    df = df.drop(columns=['touch_lower', 'touch_upper'])
    df = df.dropna(how='all')
    df = df[60:]
    
    # Assuming crossvalidation is a custom module you've defined
    train_datasets, test_datasets, weights = crossvalidation.run_split_process(df)
    
    feature_cols = ['Daily_Returns', 'Middle_Band', 'Upper_Band', 'Lower_Band', 'Log_Returns', 'MACD', 'Signal_Line_MACD', 'RSI', 'SpreadOC', 'SpreadLH']
    target_col = "label"
    
    all_predictions = []
    all_actuals = []
    all_preds = []
    
    n_components = 6
    scaler = StandardScaler()
    
    # Define a parameter grid for GridSearchCV
    param_grid = {'C': [0.1, 1, 10, 100, 1000],  
                  'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
                  'kernel': ['rbf']} 

    # Training and Predicting for each split
    for train_data, test_data, weight_data in zip(train_datasets[-1], test_datasets[-1], weights[-1]):
        
        X_train = train_data[feature_cols]
        y_train = train_data[target_col]
        X_test = test_data[feature_cols]
        y_test = test_data[target_col]

        # Standardize the data
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Apply PCA
        pca = PCA(n_components=n_components)
        X_train_pca = pca.fit_transform(X_train_scaled)
        X_test_pca = pca.transform(X_test_scaled)

        # Initialize the SVC model and GridSearchCV
        clf = SVC(probability=True, C=0.1,gamma=1, kernel='rbf')
        #clf = GridSearchCV(svc, param_grid, refit=True, verbose=3, n_jobs=-1)
        
        # Fit the model
        clf.fit(X_train_pca, y_train)

        # Get the best estimator
        #best_svc = clf.best_estimator_
        
        # Predictions
        #probas = clf.predict_proba(X_test_pca)
        #y_pred = clf.predict(X_test_pca)

        probas = clf.predict_proba(X_test_pca)

        #y_pred = (probas[:, 1] >= threshold).astype(int)

        
        max_proba_indices = np.argmax(probas, axis=1)
        predicted_classes = clf.classes_[max_proba_indices]
        y_pred = predicted_classes

        # Print and store results
        print('######################')
        print('probas:', probas)
        print(classification_report(y_test, y_pred, zero_division=1))
        print('Confusion Matrix:', confusion_matrix(y_test, y_pred))
        #predicted_probabilities = probas[:, 2]
        #print('predicted_probs:', predicted_probabilities)
        #print('y_test:', y_test)
        print(f'Y_true:{y_test} Y_pred:{y_pred}' )

        comparison_df = pd.DataFrame({'Y_true': y_test, 'Y_pred': y_pred})

        print(comparison_df)

       # brier_score = brier_score_loss(y_test, predicted_probabilities)
       # print('Brier Score:', brier_score)

        predictions_df = pd.DataFrame({
            'Actual': y_test,
            'Predictions': y_pred
        })
        all_predictions.append(predictions_df)

        all_actuals.extend(y_test.tolist())
        all_preds.extend(y_pred.tolist())
        print('###########################')
        print('classes---> ',clf.classes_)


    # After processing all splits, compute overall metrics
    
    joblib.dump(clf, 'models/EURUSD/random_forest_model_up_SPY.pkl')
    joblib.dump(pca, 'models/EURUSD/pca_transformation_up_SPY.pkl')
    joblib.dump(scaler, 'models/EURUSD/scaler_SPY.pkl')
    
    file_input = "/mnt/volume_nyc1_02"
    
    joblib.dump(clf, f'{file_input}/models/EURUSD/random_forest_classifier_up_EURUSD.pkl')
    joblib.dump(pca, f'{file_input}/models/EURUSD/pca_transformation_up_EURUSD.pkl')
    joblib.dump(scaler, f'{file_input}/models/EURUSD/scaler_EURUSD.pkl')
    
    print(predictions_df)
    print("\nOverall Classification Report:")
    #print(classification_report(all_actuals, all_preds, zero_division=1))
    print('Overall Confusion Matrix:', confusion_matrix(all_actuals, all_preds))

    
    # Combining all predictions and saving
    final_predictions_df = pd.concat(all_predictions)
    final_predictions_df.to_csv('predictions.csv', index=False)
'''
    
    # You might want to return something from this function, like t
  

def random_forest_classifier(df, asset):
    
    
    if asset is not None:
        asset =asset
    

    # Data Preprocessing
    start_date = pd.to_datetime('2003-02-02')
    end_date = pd.to_datetime('2016-01-02')
    threshold = 0.7 
    
    df = df.drop(columns=['touch_lower', 'touch_upper'])
    df = df.dropna(how='all')
    df = df[60:]
    
    # Splitting data

    print('input dataframe:',df.columns)
    train_datasets, test_datasets, weights = crossvalidation.run_split_process(df)
    # train_datasets = bootstrap.sequential_bootstrap_with_rebalance(train_datasets)
    # 
    #     
    
   # dropcols =df.filter(like=asset)
    #print(dropcols.columns)
    
    
    #feature_cols = ['Daily_Returns', 'Middle_Band', 'Upper_Band', 'Lower_Band', 'Log_Returns', 'MACD', 'Signal_Line_MACD', 'RSI', 'SpreadOC', 'SpreadLH', 'SMI']
    df =df.drop(['weekday', 'hour', 'upper_barrier', 'lower_barrier', 't1'], axis =1)
   # print('dropcols:',dropcols)
    df = df.drop('Date',axis=1)
    #feature_cols = df.drop(dropcols, axis=1)
    
    feature_cols = df.drop('label',axis=1).columns
    #fearture_cols = df.drop('EURUSD', axis=1).columns

    #target_col = f'{asset}_Close'

    target_col = 'label'


   # print(feature_cols.columns)
    
    #target_col = ""
    
    print('featurecols:',feature_cols)
    

    all_predictions = []
    all_actuals = []
    all_preds = []
    n_components = 4
    scaler = StandardScaler()
    
    # Define a parameter grid for GridSearchCV
    '''

    '''
    
    param_grid = {
        'n_estimators': [200,500,1000],
        'max_features': [4],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
       # 'bootstrap': [True, False]
    }

    # Training and Predicting for each split
   # for train_data, test_data, weight_data in zip(train_datasets[-1], test_datasets[-1], weights[-1]):
        #train = train_datasets
        #test = test_datasets
        #weight = weights[-1] 
        
    train_data =   train_datasets[-1]

    test_data = test_datasets[-1]

    weight_data =  weights[-1]
        
    X_train = train_data[feature_cols]
    y_train = train_data[target_col]
    X_test = test_data[feature_cols]
    y_test = test_data[target_col]

    # Get the names of the columns with datetime dtype
    datetime_columns = X_train.select_dtypes(include=[np.datetime64]).columns

# Drop the datetime columns
    X_train = X_train.drop(datetime_columns, axis=1)

# Now you can fit the scaler
   # X_train = scaler.fit_transform(X_train)

    # Standardize the data
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Apply PCA
    pca = PCA(n_components=n_components)
    X_train = pca.fit_transform(X_train)
    X_test = pca.transform(X_test)

    # Initialize GridSearchCV
    #clf = SVC(probability=True, C=50)
    clf =RandomForestClassifier( random_state=42, n_estimators=200)

    grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train, sample_weight=weight_data)

    #best_params = grid_search.best_params_
    # print(f"Best parameters found: {best_params}")

    #best_rf = grid_search.best_estimator_
    #grid_search = GridSearchCV(clf, param_grid,refit=True, verbose=3, n_jobs=-1)
    #clf.fit(X_train, y_train, sample_weight=weight_data)

    # Use the best estimator to predict
    #best_svm = grid_search.best_estimator_
    #print('best svm:',best_svm)
    
    probas = grid_search.predict_proba(X_test)

    encoder = OneHotEncoder(sparse=False)

    

    
    #y_pred = (probas[:, 1] >= threshold).astype(int)

   # selected_columns= probas[:,[0,2]]
    max_proba_indices = np.argmax(probas, axis=1)
   # max_proba_indices= np.where(max_proba_indices==1,2,max_proba_indices)
    predicted_classes = grid_search.classes_[max_proba_indices]
    y_pred = predicted_classes

    


    # Print and store results
    print('######################')
    print('probas:', probas)
    print(classification_report(y_test, y_pred, zero_division=1))
    print('Confusion Matrix:', confusion_matrix(y_test, y_pred))
    #predicted_probabilities = probas[:, 2]
    #print('predicted_probs:', predicted_probabilities)
    #print('y_test:', y_test)
    print(f'Y_true:{y_test} Y_pred:{y_pred}' )

    comparison_df = pd.DataFrame({'Y_true': y_test, 'Y_pred': y_pred})

    print(comparison_df)

    # Assume y_test is your test data
#    y_test = y_test.reshape(-1, 1)

    # Fit and transform the data
   # y_test_encoded = encoder.fit_transform(y_test)

   # logloss = log_loss(y_test_encoded, probas)



   # print('logloss:', logloss)

    # brier_score = brier_score_loss(y_test, predicted_probabilities)
    # print('Brier Score:', brier_score)

    print(len(y_test))
    print(len(y_pred))
    print(len(probas[0]))
    print(len(probas[1]))
    print(len(probas[2]))
    print(probas.shape)


    predictions_df = pd.DataFrame({
        'Actual': y_test,
        'Predictions': y_pred,
        'down proba': probas[:,0],
        'neutral proba': probas[:,1],
        'up proba': probas[:,2] 
    })
    all_predictions.append(predictions_df)

    all_actuals.extend(y_test.tolist())
    all_preds.extend(y_pred.tolist())
    print('###########################')

    predictions_df.to_csv('predictions_df.csv')
    #print('classes---> ',clf.classes_)


    # After processing all splits, compute overall metrics
    
    joblib.dump(clf, 'models/random_forest_model_up_EURUSD_60.pkl')
    joblib.dump(pca, 'models/pca_transformation_up_EURUSD_60.pkl')
    joblib.dump(scaler, 'models/scaler_EURUSD.pkl')



'''    
    file_input = "/mnt/volume_nyc1_02"
   
    print(predictions_df)

    predictions_df.to_csv('predictions_final.csv', index=False)
    print("\nOverall Classification Report:")
    #print(classification_report(all_actuals, all_preds, zero_division=1))
    print('Overall Confusion Matrix:', confusion_matrix(all_actuals, all_preds))

    
    # Combining all predictions and saving
    final_predictions_df = pd.concat(all_predictions)
    final_predictions_df.to_csv('predictions.csv', index=False)
  
'''

