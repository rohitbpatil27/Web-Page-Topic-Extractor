import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def get_page_content(url):
    # Try to fetch the content of the URL via HTTP GET request
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        # Print and return None if any error occurs during the request
        print(f"Error in fetching {url}:{str(e)}")
        return None

def extract_content_tokenize(page_content):
    # Parse the HTML content and extract text only
    soup = BeautifulSoup(page_content, 'html.parser')
    text = soup.get_text(separator='\n').lower()  # Convert to lowercase to normalize
    # Tokenize the text and filter out non-alphabetic tokens
    words = [word for word in nltk.word_tokenize(text) if word.isalpha()]
    return words

def topics_identification(words, num_topics=5):
    # Remove stopwords from the list of words and calculate frequency distribution
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    fdist = FreqDist(filtered_words)
    # Return the most common words as topics
    topics = [word for word, count in fdist.most_common(num_topics)]
    return topics

def common_topics(url):
    # Get the page content and process it to identify common topics
    page_content = get_page_content(url)
    if page_content:
        words = extract_content_tokenize(page_content)
        topics = topics_identification(words, 5)
        return topics
    return []

# Example usage of the functions defined above
urls = [
    "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster",
    "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/",
    "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"
]

for url in urls:
    print(f"URL: {url}")
    print("Topics:", common_topics(url))
    print("\n")