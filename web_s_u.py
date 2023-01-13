import pandas
from selenium import webdriver
from bs4 import BeautifulSoup
#("/opt/google/chrome")#("/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Firefox("usr/lib/firefox")
names = []
rankings = []
tuitions = []
enrollments = []
locations = []
#driver.get("<a href='https://www.usnews.com/>https://www.usnews.com/best-colleges/rankings/national-universities'")
driver.get("<a href='https://www.usnews.com/best-colleges/rankings/national-universities'")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': "Box-w0dun1-0 Card__TextContainer-sc-1ra20i5-6 dWWnRo itaHJf"}):
    name = a.find('h3', attrs={'class': 'Heading-sc-1w5xk2o-0 fOQLJm'})
    ranking = a.find('div', attrs={'class': 'RankList__Rank-sc-2xewen-2 fxzjOx ranked has-badge'})
    tuition = a.find('div', attrs={'class': 'Box-w0dun1-0 QuickStatHug__Container-hb1bl8-0 dWWnRo fkvuin QuickStatHug-hb1bl8-2 fyaies QuickStatHug-hb1bl8-2 fyaies'})
    enrollment = a.find('div', attrs={'class': 'Box-w0dun1-0 QuickStatHug__Container-hb1bl8-0 dWWnRo fkvuin QuickStatHug-hb1bl8-2 fyaies QuickStatHug-hb1bl8-2 fyaies'})
    location = a.find('p', attrs={'class': "Paragraph-sc-1iyax29-0 pyUjv"})

    names.append(name.text)
    rankings.append(ranking.text)
    tuitions.append(tuition.text)
    enrollments.append(enrollment.text)
    locations.append(location.text)


df = pandas.DataFrame({'University Name': names, 'Ranking': rankings, 'Tuition': tuitions, 'Enrollment': enrollments, 'Location': locations})
df.to_csv('Universities.csv', index=False, encoding='utf-8')