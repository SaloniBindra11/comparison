import pandas as pd

a=pd.read_csv("old.csv")
b=pd.read_csv("new.csv")

df1=pd.DataFrame(a)
df2=pd.DataFrame(b)

for i in range(len(df1)):
  sr1 = df1.iloc[i]
  sr2 = df2.iloc[i]
  if (sr1==sr2).all():
    print(" \n This is same -_- \n",sr1)
  else:
     print("\n SR1 \n",sr1)
     print("\n SR2 \n",sr2)
     if(sr1==sr2).any():
       print("there is a difference")
     else:
       print("there is not difference")
        