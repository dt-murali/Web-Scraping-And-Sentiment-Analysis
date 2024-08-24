# Web-Scraping-And-Sentiment-Analysis

## Problem overview
The "ScrapeSense" project automates the extraction and sentiment analysis of Amazon product reviews. Using Flask for the interface and BeautifulSoup for web scraping, the app collects reviews from a product page and analyzes them with NLTK's VADER sentiment tool. It then displays the results in both a table format, showing individual review ratings and sentiments, and a plot of overall sentiment distribution. The goal is to simplify the process of understanding customer feedback through automated scraping and analysis.
___
## Requriments
### **1. Software and Libraries:**
- **Python**: The primary programming language.
- **Flask**: For creating the web interface.
- **BeautifulSoup (bs4)**: For scraping Amazon product reviews.
- **Requests**: To handle HTTP requests to the Amazon product pages.
- **NLTK (VADER Sentiment Analyzer)**: For performing sentiment analysis on the reviews.
- **Matplotlib and Seaborn**: For visualizing sentiment analysis in the form of graphs.
- **Pandas**: For handling and structuring the review data in tabular form.

### **2. External Resources:**
- **Amazon Product URL**: The user inputs the product page URL from Amazon for review scraping.
- **Bootstrap**: For frontend styling and responsive design via CDN.

### **3. Development Tools:**
- **Python Environment**: Properly set up with necessary libraries installed via pip.
- **HTML/CSS/JavaScript**: For the frontend to display and switch between views.
- **Web Browser**: To interact with the web interface.
  
### **4. Hosting Environment:**
- Localhost or server to run the Flask application and serve the website (e.g., running via a development server with Flask).

### **5. System Requirements:**
- Python 3.x installed on the system.
- Internet connection for accessing Amazon pages and external CDNs for Bootstrap and Google Fonts.
___
## Workflow
1. **User Input:** The user enters an Amazon product URL in the web interface and clicks submit.
2. **Web Scraping:** The Flask backend takes the URL, fetches the product's reviews from Amazon using BeautifulSoup, and processes the review data (ratings and text).
3. **Sentiment Analysis:** Each review is analyzed using the NLTK VADER tool to determine if it’s positive, negative, or neutral.
4. **Visualization:** The results are displayed on the webpage, either as a table with individual review sentiments or as a plot showing the overall sentiment distribution.
5. **Results Display:** The user can switch between the table and plot views to understand the reviews' sentiments for the product.

This process helps the user quickly analyze and visualize sentiments from Amazon product reviews.
___
## Reference
- For more details, vist web scraping and sentiment analysis project : [ScrapeSense-Web Scraping And Sentiment Analysis](

