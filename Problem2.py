records = input("enter the book and the number of days like this format\n 'Python Basics - 5, Data Science Handbook - 3': ")
books = {} 
for record in records.split(", "):  
    title, days = record.split(" - ") 
    days = int(days) 
    if title in books:
        books[title] += days 
    else:
        books[title] = days  

most_borrowed = max(books, key=books.get)

least_borrowed = min(books, key=books.get)

total_days = sum(books.values())
size = len(books)
average_days = total_days / size

unique_titles = list(books.keys())

sorted_books = sorted(books.items(), key=lambda x: x[1], reverse=True)

print(f"\nMost Borrowed Book: {most_borrowed} ({books[most_borrowed]} days)")
print(f"Least Borrowed Book: {least_borrowed} ({books[least_borrowed]} days)")
print(f"Average Borrowing Days: {average_days:.2f}")
print(f"Unique Titles: {', '.join(unique_titles)}")
print("\nBooks sorted by borrowing days (descending):")
for book, days in sorted_books:
    print(f"{book}: {days} days")