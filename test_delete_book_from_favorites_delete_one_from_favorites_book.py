from main import BooksCollector


class TestBooksCollector:

    def test_delete_book_from_favorites_delete_one_from_favorites_book(self):
        collector = BooksCollector()

        # Добавляем книгу и отмечаем "Избранное"
        collector.add_new_book('Унесенные призраками')
        collector.add_book_in_favorites('Унесенные призраками')

        # Добавляем вторую книгу и отмечаем "Избранное"
        collector.add_new_book('Приключения Шерлока Хомса')
        collector.add_book_in_favorites('Приключения Шерлока Хомса')

        # Удаляем одну из книг
        collector.delete_book_from_favorites('Унесенные призраками')

        # Проверяем, что удалилось
        assert 'Унесенные призраками' not in collector.get_list_of_favorites_books()
        assert 'Приключения Шерлока Хомса' in collector.get_list_of_favorites_books()