# SafeSurf
SafeSurf is a machine learning-driven platform that analyzes website privacy policies to provide users with a safety score and insights, helping them make informed decisions about their online activities.

Created a privacy policy analysing safety and rating website that uses NLP models to predict and summarise the privacy policies of websites by extracting them using API and storing in a real time database.

![](https://github.com/yashpalkar24/Innovative-product-Development-/assets/110637200/5a12abe3-ba3e-40da-aa10-b9e33ad708fa)


**Innovative-product-Development**-
We have developed a machine learning-powered browser extension to clarify website data collection practices. By analysing and simplifying complex privacy policies, our tool helps users understand data collection, storage, sharing, and risks, empowering them to make informed decisions and control their online privacy.

To create a detailed workflow pipeline showing the connections and interactions between your code files along with line references where these connections occur, I will analyze the content of the key Python files (`main.py`, `fire_db.py`, `scraper.py`, and others) that you uploaded. This analysis will outline how data flows through these files, which files are responsible for input, processing, and output, and the exact lines where these interactions are coded.

### Code Files for Detailed Analysis:
1. **`main.py`** - Typically, this file orchestrates the high-level flow of the application.
2. **`fire_db.py`** - Manages database operations.
3. **`scraper.py`** - Handles the scraping of web content.
4. **`utils.py`** - Provides utility functions, possibly for data processing.
5. **`report.py`** - Likely generates reports or summaries.
6. **`score.py`** - Responsible for scoring, possibly evaluating the data or results.
7. **`stream.py`** - Manages streaming or real-time data updates.

I will now extract the contents of these files and analyze them to determine the interactions and data flow, identifying the line references where these files connect with each other. Let's start by extracting and reviewing the content of these Python files to identify their specific functionalities and connections.

Based on the detailed analysis of your Python code files, here is a comprehensive workflow pipeline that describes the interactions between different components of your project:

### Workflow Pipeline Overview:
- **`main.py`:** Acts as the central orchestrator for handling HTTP requests, interacting with other modules to process data, and updating the database based on user inputs.
- **`fire_db.py`:** Manages Firebase database initialization and provides utility functions for database interactions.
- **`scraper.py`:** Responsible for scraping data from websites using HTTP requests.
- **`utils.py`:** Provides utility functions including HTML parsing, data cleaning, and dividing text into question and answer formats.
- **`report.py`:** Uses data processed by `utils.py` to generate reports and applies scores using `score.py`.
- **`score.py`:** Computes readability and other text-based scores.
- **`stream.py`:** Handles real-time data fetching and updates using Streamlit.

### Detailed Workflow with Code Interactions:

1. **HTTP Request Handling (main.py):**
   - Receives user input via HTTP GET requests.
   - Invokes `scraper.py` to scrape data based on URL.
   - Uses `utils.py` to process the scraped HTML.
   - Generates reports using `report.py` which in turn utilizes `score.py` for scoring.
   - Updates the Firebase database using methods defined in `fire_db.py`.

2. **Firebase Database Operations (fire_db.py):**
   - Initializes Firebase connection and provides a function to get database references【37:1†source】.

3. **Web Scraping (scraper.py):**
   - Scrapes website data using requests and BeautifulSoup【37:2†source】.
   - Processes HTML content to extract required information【37:2†source】.

4. **Utility Functions (utils.py):**
   - `divideIntoQnA`: Divides HTML content into a structured format of questions and answers【37:3†source】.
   - `getHTML`: Fetches HTML content for a given URL【37:17†source】.

5. **Report Generation (report.py):**
   - Calls `utils.summarize` to summarize content and uses `score.py` to assign readability scores【37:4†source】.

6. **Scoring (score.py):**
   - Calculates various readability scores and returns them to `report.py` for inclusion in the final report【37:5†source】.

7. **Real-time Data Streaming (stream.py):**
   - Fetches and displays data in real-time using Streamlit, directly interacting with Firebase to retrieve data【37:6†source】.

### Code Line References:
- **main.py** interacts with Firebase through `fire_db.py` for database operations at lines where Firebase is initialized and where data updates are handled.
- **scraper.py** is invoked from `main.py` when URLs need to be processed, specifically in the route handling functions.
- **utils.py** functions are called from `main.py` to process the scraped HTML.
- **report.py** and **score.py** are linked where `report.py` calls scoring functions from `score.py` to evaluate the text.
- **stream.py** operates independently for real-time updates but fetches data from Firebase initialized in `fire_db.py`.

This detailed pipeline connects your project's components based on their functionality and code interactions. If you need the exact line numbers for these interactions or further details on any part, please let me know!

Output at Firebase

![](https://github.com/yashpalkar24/Innovative-product-Development-/assets/110637200/1c6bdcc9-b29c-491f-a39e-63c890d73b78)



Final Outputs
These below outputs are for various websites 

![](https://github.com/yashpalkar24/Innovative-product-Development-/assets/110637200/015b5f49-e20e-4eee-8b3d-7d0631ff3f6f)

![](https://github.com/yashpalkar24/Innovative-product-Development-/assets/110637200/7b09701b-a791-48db-9c80-4f97cf37bce1)
