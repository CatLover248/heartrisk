import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

  
class Heart:
  def __init__(self):
    self.init_model()
  def init_model(self, save_cleaned_data=False):
    self.df = pd.read_csv("heart_attack_prediction_dataset.csv")
    self.df = self.df.drop(columns=["Patient ID"])
    systolic = []
    diastolic = []
    for i in self.df["Blood Pressure"]:
      split_data = i.split("/")
      systolic.append(split_data[0])
      diastolic.append(split_data[1])
    self.bp_loc = self.df.columns.get_loc("Blood Pressure")

    self.df.insert(self.bp_loc,"Systolic", systolic)
    self.df.insert(self.bp_loc,"Diastolic", diastolic)

    self.df = self.df.drop(columns=["Blood Pressure"])

    #Converting strings to 0s and 1s
    #Male -> 0
    #Female -> 1
    #unhealthy -> 0
    #healthy -> 1
    #average = 2
    #Also removing other columns
    self.df = self.df.drop(columns=["Hemisphere", "Continent", "Country"])
    self.df = self.df.replace(to_replace=["Male"], value=0)
    self.df = self.df.replace(to_replace=["Female"], value=1)
    self.df = self.df.replace(to_replace=["Unhealthy"], value=0)
    self.df = self.df.replace(to_replace=["Healthy"], value=1)
    self.df = self.df.replace(to_replace=["Average"], value=2)
    if(save_cleaned_data):
      self.df.to_csv("cleaned_data.csv")

    #Splitting into input and output dataset
    X = self.df.drop(columns=["Heart Attack Risk"])
    y = self.df["Heart Attack Risk"]
    #Splitting into test and train datasets
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,y,test_size=0.2)

    #Training model and initalizing it
    self.model = DecisionTreeClassifier()
    self.model.fit(self.X_train, self.y_train)

  def get_accuracy(self):
    #Making predictions
    pred = self.model.predict(self.X_test)
    #Calculating accuracy
    return accuracy_score(self.y_test, pred)

  def predict_risk_at_heartfailure(self, id):
    return self.model.predict([id])

"""
if __name__ == "__main__":
  m = Model()
  m.init_model()
  pred = m.predict_risk_at_heartfailure([77,0,228,72,101,68,1,1,1,1,1,19.633268156072297,0,0,0,9,10.91752425375187,29886,35.10223615396757,590,7,6])
  print(pred)
  print(m.get_accuracy())
"""