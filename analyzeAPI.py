
import requests
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://www.chrisouboter.com/api/all/movie"
response = requests.get(url)
data = response.json()['data']

title = [item['title'] for item in data]
length = [item['genre'] for item in data]


plt.figure(figsize=(10,6))
sns.lineplot(x=title, y=length)
plt.title('Data Visualization')
plt.xlabel('Movie title')
plt.ylabel('Length')
plt.show()

