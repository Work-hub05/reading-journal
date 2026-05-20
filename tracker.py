def add_book(books):
    """Добавляет новую книгу."""
    print("\nДобавление книги")

    author = input("Автор: ").strip()
    title = input("Название: ").strip()

    if not author or not title:
        print("Ошибка: автор и название не могут быть пустыми.")
        return

    if is_duplicate(books, author, title):
        print("Такая книга уже есть в списке.")
        return

    rating = input_rating()
    read_date = input_date()

    book = {
        "author": author,
        "title": title,
        "rating": rating,
        "read_date": read_date
    }

    books.append(book)
    save_books(books)
    print("Книга добавлена.")