# News-Application<br>
My News Application is a simple Python-based news application that fetches and displays top headlines from various sources using the News API. It provides an intuitive graphical user interface (GUI) built with Tkinter for easy navigation and reading of news articles.<br>
This is a Quick current News Application to stay updated with the current affairs.
<br>

Tech Used:
.__________________________________.
| language | concept | frame       |
| ---------|---------|-------------|
| python   | OOPs    | GUI(python) |
|__________________________________|

Error Handling: catching exceptions when trying to load images.if the image URL is not available, you might want to display a placeholder image or just skip displaying the image.

Button Disabling: Consider disabling the "Prev" button when you're at the first news item and the "Next" button when you're at the last news item. for providing better user experience and prevents unnecessary button clicks.

Code Refactoring: "load_news_item" method is doing a lot of things. Consider breaking it down into smaller, more manageable functions for better code organization and readability.

Requirements<br>
Python 3.x <br>
requests library<br>
PIL (Python Imaging Library)<br>
Tkinter (usually comes pre-installed with Python)
