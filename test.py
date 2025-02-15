from main import BooksCollector


class TestBooksCollector:

    def add_book_in_favorites_add_new_favorites_book(self):
        collector = BooksCollector()

        collector.add_new_book('Унесенные призраками')
        # Добавляем книгу
        collector.add_book_in_favorites('Унесенные призраками')

        # Проверяем что книга в Избранном
        assert len(get_list_of_favorites_books()) == 1
