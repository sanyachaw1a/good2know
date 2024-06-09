# Good2Know

## Overview

Good2Know is a personal application that scrapes various news websites, clusters related articles, identifies key topics, and presents the top five most important news topics of the day. It consists of a backend written in Python and a frontend built using React Native.

## Backend Features

- **Web Scraping**: Utilizes Beautiful Soup to scrape multiple news websites for articles.
- **Article Clustering**: Uses BertModel - a pre-trained language model - to cluster related articles together.
- **Topic Identification**: Extracts keywords from each article cluster and uses the Groq API to categorize topics topics.
- **Sorting Algorithm**: Selects the top five most important news topics based on relevance and significance.
- **Database Integration**: Uploads news topics and related articles to Firestore in Firebase for storage and retrieval.

## Frontend Features

- **Mobile App**: Developed using React Native for cross-platform compatibility.
- **Data Fetching**: Fetches information about news topics and related articles from the backend.
- **User Interface**: Provides an intuitive and user-friendly interface for navigating news topics and articles.

## Technologies Used

### Backend

- **Python**: Backend scripting language.
- **Beautiful Soup**: Python library for web scraping.
- **Pre-trained Language Model: BertTokenizer**: Used for article clustering.
- **Groq API**: Generates topics based on keywords.
- **Firestore**: Firebase database for storing news topics and articles.

### Frontend

- **React Native**: Frontend framework for building mobile apps.
- **JavaScript/TypeScript**: Frontend scripting languages.
- **Firebase SDK**: Integrates with Firebase for data fetching and storage.
