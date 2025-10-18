import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    print('Hello world!')
    
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)
    print(f"Scraping: {url}")
    print(response)
    print(response.content)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="comment")

    print(f"Elements: {len(elements)}")
    
    # find all elements with class="ind" and indent level = 0
    elements = soup.find_all(class_="ind" , indent=0)
    # for each of this elements, find the next element
    comments = [e.find_next(class_="comment") for e in elements]

    # Show the number of comments found
    print(f"Comments: {len(comments)}")   

    # show each comment (job post)
    for comment in comments:
        print(comment)

    # show each comment (job post) | Clean up the response text
    for comment in comments:
        comment_text = comment.get_text()
        print(comment_text, end="\n\n")
    
    # Map of technologies keyword to search for
    # and the occurence initialized at 0
    keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0 }

    # show each comment (job post)
    for comment in comments:
        # get the comment text and lower case it
        comment_text = comment.get_text().lower()

        # split comment by space which create an array of words
        words = comment_text.split(" ")

        print(words)

        # Use the string strip function
        # and place all the caracters we want to strip away
        words = [w.strip(".,/:;!@") for w in words]
        print(words)

        # Use the string strip function
        # and place all the caracters we want to strip away
        # Use a set to have unique words
        words = {w.strip(".,/:;!@") for w in words}
        print(words)
    
        # search for k in keywords, this give you the dictionory key
        # if the key is in the words set, we add 1 to the keywords score
        for k in keywords:
            if k in words:
                keywords[k] += 1
        print(keywords)

    # plot a bar graph
    plt.bar(keywords.keys(), keywords.values())
    # Add labels
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.show()
    
if __name__ == "__main__":
    main()