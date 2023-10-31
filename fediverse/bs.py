from bs4 import BeautifulSoup


def remove_links(input_html):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(input_html, "html.parser")

    # Find all <a> elements
    links = soup.find_all("a")

    # Remove each <a> element from the soup
    for link in links:
        link.extract()

    # Get the cleaned HTML as a string
    cleaned_html = str(soup)

    return cleaned_html


# Example usage:
if __name__ == "__main__":
    input_html = """
        <p>This is a sample HTML with a link: <a href="https://www.example.com">Example</a></p>
        <p>Another link: <a href="http://www.anotherexample.com">Another Example</a></p>
    """

    cleaned_html = remove_links(input_html)
    print(cleaned_html)
