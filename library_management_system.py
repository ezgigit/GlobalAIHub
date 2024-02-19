# L I B R A R Y   M A N A G E M E N T   S Y S T E M



class Library:

    def __init__ (self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        for line in book_lines:
            book_info = line.split(',')
            book_name, author, release_date, num_pages = book_info
            print(f"Book: {book_name}, Author: {author}, Release Date: {release_date}, Pages: {num_pages}")

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{book_title},{book_author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print(f"\nBook '{book_title}' added successfully.")

    def remove_book(self):
        book_title_to_remove = input("Enter the title of the book  you want to remove: ")

        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        index_to_remove = -1

        for i, line in enumerate(book_lines):
            if book_title_to_remove in line:
                index_to_remove = i
                break

        if index_to_remove != -1:
            del book_lines[index_to_remove]

            self.file.truncate(0)

            for line in book_lines:
                self.file.write(line + '\n')

            print(f"\nBook '{book_title_to_remove}' removed successfully.")

        else:
            print(f"\nBook '{book_title_to_remove}' not found.")

lib = Library()

def print_menu():
    print("\n*** MENU ***\n")
    print("1- List Books")
    print("2- Add a Book")
    print("3- Remove a Book")
    print("Press 'q' to quit.\n")

def main():
    while True:
        print_menu()
        choice = input("Please enter your choice: ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

