import requests
from bs4 import BeautifulSoup
import xlsxwriter



# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook("best_movies.xlsx")   
worksheet = workbook.add_worksheet("Best Movies")

worksheet.set_column("A:A",50)  # Widen the first column to make the text clearer.
bold = workbook.add_format({'bold': True})  # Add a bold format to use to highlight cells.

# Write some data headers.
worksheet.write('A1', 'Movie', bold)
worksheet.write('B1', 'Rating', bold)

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Enter rating: "))


movie_name = soup.find_all("td", {"class":"titleColumn"})
ratings = soup.find_all("td",{"class":"ratingColumn imdbRating"})

# Start from the first cell below the headers.
row = 1
col = 0


for moviename,rating in zip(movie_name,ratings):
    moviename = moviename.text.strip()
    moviename = moviename.replace("\n","")
    rating = rating.text.strip()
    rating = rating.replace("\n","")

    if float(rating) > a:
        worksheet.write(row,col,moviename)
        worksheet.write(row,col+1,rating)
        row +=1


workbook.close()