df = pd.DataFrame({'label':y_test_label, 'predict':prediction})

df[(df.label==5)&(df.predict==3)]