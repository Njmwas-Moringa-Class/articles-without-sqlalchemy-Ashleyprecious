# main.py

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

        author = Author(author_name)
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
            print(f"Contributing Authors (more than 2 articles): {magazine.contributing_authors()}")
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

def main():
    # Adding sample data
    author1 = Author("John Doe")
    author2 = Author("Jane Doe")

    magazine1 = Magazine("Tech Weekly", "Technology")
    magazine2 = Magazine("Science Monthly", "Science")

    author1.add_article(magazine1, "The Future of AI")
    author1.add_article(magazine1, "Advancements in Robotics")
    author2.add_article(magazine1, "The Impact of Quantum Computing")

    author2.add_article(magazine2, "Exploring Black Holes")
    author2.add_article(magazine2, "The Search for Extraterrestrial Life")

    while True:
        print("\nOptions:")
        print("1. Add Article")
        print("2. Get Magazine Info")
        print("3. Update Magazine Info")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_article()
        elif choice == "2":
            get_magazine_info()
        elif choice == "3":
            update_magazine_info()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

        # Call get_magazine_info after each operation to see the updated information
        get_magazine_info()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Unhandled exception: {e}")
        print("An unexpected error occurred. Please check the logs.")

