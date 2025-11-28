import pandas as pd
data = {
  "Maths":{"Suman":60,"John":40,"Cathy":80},
  "Science":{"Suman":30,"John":70,"Cathy":20},
  "English":{"Suman":50,"John":90,"Cathy":10}
}
df = pd.DataFrame(data)
print(df) 
df.to_csv("./part8/student.csv")