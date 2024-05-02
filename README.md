# Web Page Topic Extractor

The Web Page Topic Extractor is a Python-based tool that fetches content from specified URLs and identifies the most frequent relevant topics from the text on the page. It uses natural language processing techniques to filter and analyze the text, making it an efficient tool for quick content summarization.

## Features

- **Web Scraping**: Fetches web page content using the `requests` library.
- **HTML Parsing**: Parses HTML content to extract text using `BeautifulSoup`.
- **Text Analysis**: Processes text to remove common stopwords and non-alphabetic characters, and identifies common topics using the `nltk` library.

## Requirements

This project requires Python 3.6 or higher, along with several external libraries. Below are the necessary dependencies:
- Python 3.6+
- `requests`
- `beautifulsoup4`
- `nltk`

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository or download the source code.
2. Install the required Python libraries using pip:

    ```bash
    pip install requests beautifulsoup4 nltk
    ```

3. Ensure that the required NLTK resources are downloaded by running the following commands in your Python environment:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

## Usage

### Running as a Standalone Script

To run the script as a standalone application:

1. Open your terminal or command prompt.
2. Navigate to the directory containing the script.
3. Modify the `urls` list in the script to include the URLs you want to analyze.
4. Execute the script by running:

    ```bash
    python topic_extractor.py
    ```

### Importing in Your Project

You can also import the functionality into your own Python projects:

1. Ensure the script `topic_extractor.py` is in your project directory.
2. Import the `common_topics` function:

    ```python
    from topic_extractor import common_topics
    ```

3. Use the `common_topics` function to analyze URLs:

    ```python
    topics = common_topics('http://example.com')
    print("Identified Topics:", topics)
    ```

### Example Output

## Example Output

Below is an example of how the Web Page Topic Extractor processes a given URL and outputs the identified topics:

- **URL**: `http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/
- **Identified Topics**: ['cnn', 'ad', 'video', 'snowden', 'nsa']