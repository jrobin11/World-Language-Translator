
# World Language Translator

This project is designed to facilitate translation and language information retrieval. It allows users to find languages spoken in specific countries, countries where a certain language is spoken, perform translations, and list available languages and countries. The project is structured as a Python application with multiple components handling different aspects of data management and user interaction.

## Components

1. **Abrevs.py** - Contains a class `Abrevs` that holds a dictionary of language names and their corresponding abbreviations.
2. **Interface.py** - The main script for user interaction through the command line. It handles menu-driven inputs for various functionalities like language and country lookup, translation, etc.
3. **Tree.py** - Handles the logic for finding languages by country, countries by language, and translating phrases. It interacts with external translation services via API.
4. **X2D.py** - Manages the data extracted from Excel sheets that map languages to countries and vice versa.
5. **countries.py** - A simple dictionary mapping of country codes to their full names.

## Features

- Lookup languages spoken in a given country
- Find all countries where a particular language is spoken
- Translate phrases from English to a target language
- List all available languages and countries

## Setup

### Prerequisites

- Python 3.x
- pip for Python package management
- Access to the internet for translation API

### Installation Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:jrobin11/World-Language-Translator.git
   ```
2. Navigate into the project directory:
   ```bash
   cd World-Language-Translator
   ```
3. Install required Python packages:
   ```bash
   pip install requests xlrd
   ```
4. Run the interface:
   ```bash
   python Interface.py
   ```

### Configuration

Ensure that you have the necessary API keys configured for accessing the translation service. The key should be placed in the `Tree.py` file.

## Usage

After running `Interface.py`, follow the on-screen prompts to select from the available options:
- **1**: Find languages of a country
- **2**: Find all countries that speak a language
- **3**: Translate
- **4**: List all available countries
- **5**: List all available languages
- **6**: Exit

