# The business of scientific misconduct: 


This repository contains a Python script designed to scrape data from a web archive. It fetches and extracts data from a URL, processes the data, and finally saves the results to an Excel file.

## Features

- Web scraping from a specified URL pattern.
- Parsing HTML content to extract specific information.
- Data processing for cleaning and transforming extracted data.
- Backup and storage of the extracted data into Excel format.

## What does the code do?

1. **fetch_data**: Connects to a URL based on the given `contract_number` and `author_position` parameters and fetches the HTML content.

2. **extract_contract_number**: Extracts the contract number from the parsed HTML.

3. **extract_titles_and_scopus**: Extracts Russian and suspected English titles from the parsed HTML content. Additionally, it extracts Scopus data related to the contract.

4. **extract_web_of_science**: Extracts Web of Science data from the parsed HTML content.

5. **extract_price**: Extracts the price data associated with the contract.

6. **main function**: Orchestrates the overall scraping process by iterating over different contract numbers and author positions, extracting data for each combination, and appending the results to a DataFrame. The final DataFrame is saved to an Excel file.

7. **Post-processing**:
    - Removal of punctuation from specified columns.
    - Filtering out entries where the `Base_title` is empty.
    - Filtering out contracts where the `First_title` has a length less than 20 characters.
    - Removing contracts with a price of '0'.
    - Conversion of 'Price_Ruble' to float and calculating its equivalent value in USD.
    - Creation of a separate DataFrame for titles by eliminating duplicates.

## How to run

To run the code, simply execute:

```python
python script_name.py
```

Replace `script_name.py` with the name of the Python file containing the above code.

## Dependencies

Ensure that the following Python libraries are installed:

- `BeautifulSoup`
- `pandas`
- `urllib`

You can install these using `pip`:

```
pip install beautifulsoup4 pandas
```

## Output

After running the script, you will get an Excel file named `raw_df.xlsx` containing the scraped data.

## Notes

- Ensure you have permission to scrape from the specified website.
- The scraping logic is tailored specifically to the structure of the target website. If the website's structure changes, the code may need modifications.
- Always respect `robots.txt` when web scraping.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

If you wish to contribute to this project, kindly send a pull request.

---

© 2023 Your Name, All Rights Reserved.  

