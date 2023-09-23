# The business of scientific fraud

## About this project

During the challenges posed by COVID, I pursued and successfully completed the 'Python for Everyone Specialization' by the University of Michigan via Coursera. Leveraging these newfound skills, I played a pivotal role in an investigation into an _academic paper mill_ based in Russia, known as International Publishers. This clandestine organization specializes in the unethical practice of selling academic papers and orchestrating manipulative peer reviews.

In this project, my responsibilities involved web scraping the entire library of papers available for sale from the organization's website as well as archived versions on the Internet Archive. I was instrumental in translating paper titles and performing currency conversions. The entirety of my robust code and the comprehensive dataset derived from this investigation is readily accessible both in this repository and on Data.World for transparency and wider community benefit.

Our investigation was featured by the scientific news organization [Retraction Watch](https://retractionwatch.com/author/perronetal/). Our work led to dozens of retractions, [including 30 retractions from a single journal](https://retractionwatch.com/2022/07/05/our-deepest-apology-journal-retracts-30-likely-paper-mill-articles-after-investigation-published-by-retraction-watch/). We met with staff of the [U.S. House of Representatives Science Committee](https://docs.house.gov/Committee/Calendar/ByEvent.aspx?EventID=115022) to provide guidance on a briefing regarding scientific fraud.  

<img width="400" alt="Screenshot 2023-09-23 at 11 51 51 AM" src="https://github.com/Soul-Jacker/Retraction_Watch/assets/2854746/1882591f-e8b2-4aab-996d-0895ec56e4d1">

Our work has been cited in dozens of reports, including (but not limited to):
- [Science](https://www.science.org/content/article/russian-website-peddles-authorships-linked-reputable-journals#:~:text=In%20December%202021%2C%20he%20co%2Dauthored%20a%20separate%20analysis%20of%20www.123mi.ru%20on%20Retraction%20Watch%2C%20which%20described%20nearly%20200%20papers%20that%20may%20match%20authorships%20advertised%20there%3B%20subsequently%2C%20he%20and%20a%20colleague%20posted%20a%20catalog%20of%20contracts%20displayed%20on%20the%20site%2C%20which%20together%20refer%20to%20about%201500%20articles.)
- [The Scientist](https://www.the-scientist.com/news-opinion/the-top-retractions-of-2022-70852#:~:text=Oliver%20Hiltz%2DPerron%2C%20a%20high%20school%20student%2C)
- [The Guardian](https://www.theguardian.com/commentisfree/2023/aug/09/scientific-misconduct-retraction-watch#:~:text=to%20paper%20mills%20%E2%80%93%20scientific%20chop)

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

## Contributing

If you wish to contribute to this project, kindly send a pull request.

