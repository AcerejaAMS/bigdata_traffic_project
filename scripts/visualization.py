import pandas as pd
import matplotlib.pyplot as plt
import glob

archivo_list = glob.glob("traffic_predictions/part-*.csv")

df = pd.concat((pd.read_csv(file) for file in archivo_list), ignore_index=True)

plt.scatter(df["speed"], df["vehicle_count"], c=df["prediction"])
plt.xlabel("Velocidad")
plt.ylabel("Cantidad de vehículos")
plt.title("Clustering de Tráfico")
plt.show()

