
import logging
from Author import Author
from Magazine import Magazine
from Article import Article

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_article():
    try:
        author_name = input("Enter author's name: ")
        magazine_name = input("Enter magazine name: ")
        magazine_category = input("Enter magazine category: ")
        article_title = input("Enter article title: ")

        author = next((a for a in Author.all_authors if a.name == author_name), None)
        if not author:
            author = Author(author_name)

        magazine = Magazine.find_by_name(magazine_name)
        if not magazine:
            magazine = Magazine(magazine_name, magazine_category)

        author.add_article(magazine, article_title)

        print(f"Article '{article_title}' added to {magazine_name} by {author_name}.")

    except Exception as e:
        logger.error(f"Error adding article: {e}")
        print("An error occurred. Please try again.")

def get_magazine_info():
    try:
        magazine_name = input("Enter magazine name: ")
        magazine = Magazine.find_by_name(magazine_name)

        if magazine:
            print(f"Magazine Info:\n{magazine}")
            print(f"Contributors: {[author.name for author in magazine.contributors]}")
            print(f"Article Titles: {magazine.article_titles}")
            
            # Print contributing authors (more than 2 articles)
            contributing_authors = magazine.contributing_authors()
            print(f"Contributing Authors (more than 2 articles): {[author.name for author in contributing_authors]}")
        else:
            print(f"Magazine '{magazine_name}' not found.")

    except Exception as e:
        logger.error(f"Error getting magazine info: {e}")
        print("An error occurred. Please try again.")

def update_magazine_info():
    try:
        magazine_name = input("Enter magazine name: ")
        magazine = Magazine.find_by_name(magazine_name)

        if magazine:
            key = input("Enter additional information key: ")
            value = input("Enter additional information value: ")
            magazine.update_info(key, value)
            print(f"Additional information updated for {magazine_name}.")
        else:
            print(f"Magazine '{magazine_name}' not found.")

    except Exception as e:
        logger.error(f"Error updating magazine info: {e}")
        print("An error occurred. Please try again.")

def edit_magazine_name():
    try:
        article_title = input("Enter the title of the article you want to edit: ")
        new_magazine_name = input("Enter the new magazine name: ")

        article = next((a for a in Article.all_articles if a.article_title == article_title), None)

        if article:
            article.magazine.name = new_magazine_name
            print(f"Magazine name for the article '{article_title}' updated to '{new_magazine_name}'.")
        else:
            print(f"Article with title '{article_title}' not found.")

    except Exception as e:
        logger.error(f"Error editing magazine name: {e}")
        print("An error occurred. Please try again.")

def get_author_magazines_articles():
    try:
        author_name = input("Enter author's name: ")
        author = next((a for a in Author.all_authors if a.name == author_name), None)

        if author:
            print(f"\nMagazines and Articles by {author_name}:")
            for magazine in author.magazines:
                print(f"\nMagazine: {magazine.name}, Category: {magazine.category}")
                for article in author.articles:
                    if article.magazine == magazine:
                        print(f"- Article: {article.article_title}")

        else:
            print(f"Author '{author_name}' not found.")

    except Exception as e:
        logger.error(f"Error getting author's magazines and articles: {e}")
        print("An error occurred. Please try again.")

def get_authors_for_magazine():
    try:
        magazine_name = input("Enter magazine name: ")
        magazine = Magazine.find_by_name(magazine_name)

        if magazine:
            authors_count = {}
            for article in magazine.published_articles:
                author = article.author
                authors_count[author] = authors_count.get(author, 0) + 1

            relevant_authors = [author for author, count in authors_count.items() if count >= 2]

            if relevant_authors:
                print(f"\nAuthors with two or more articles for {magazine_name}:")
                for author in relevant_authors:
                    print(f"- {author.name}")
            else:
                print(f"No authors found with two or more articles for {magazine_name}.")
        else:
            print(f"Magazine '{magazine_name}' not found.")

    except Exception as e:
        logger.error(f"Error getting authors for magazine: {e}")
        print("An error occurred. Please try again.")

def main():
    
    # author1 = Author("John Doe")
    # author2 = Author("Jane Doe")

    # magazine1 = Magazine("Tech Weekly", "Technology")
    # magazine2 = Magazine("Science Monthly", "Science")

    # author1.add_article(magazine1, "The Future of AI")
    # author1.add_article(magazine1, "Advancements in Robotics")
    # author2.add_article(magazine1, "The Impact of Quantum Computing")

    # author2.add_article(magazine2, "Exploring Black Holes")
    # author2.add_article(magazine2, "The Search for Extraterrestrial Life")

    while True:
        print("\nOptions:")
        print("1. Add Article")
        print("2. Get Magazine Info")
        print("3. Update Magazine Info")
        print("4. Edit Magazine Name for Article")
        print("5. Get Author Magazines and Articles")
        print("6. Get Authors for Magazine")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            add_article()
        elif choice == "2":
            get_magazine_info()
        elif choice == "3":
            update_magazine_info()
        elif choice == "4":
            edit_magazine_name()
        elif choice == "5":
            get_author_magazines_articles()
        elif choice == "6":
            get_authors_for_magazine()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Unhandled exception: {e}")
        print("An unexpected error occurred. Please check the logs.")
