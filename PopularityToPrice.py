__author__ = 'python'

from PopularityScrapers import popularityToDB

# Retrieve lists of unique categories
catList = [];

categories = popularityToDB.show();

for cat in categories:
    catList.append(cat[2]);

uniqCats = [];

for i in catList:
  if i not in uniqCats:
    uniqCats.append(i)

print(uniqCats);

popularityToDB.query("SELECT * FROM popularity WHERE name", + )