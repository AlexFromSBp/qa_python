from main import BooksCollector


class TestBooksCollector:

    def test_set_book_genre_from_list(self):
        collector = BooksCollector()
        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        # Проверяем жанр книги по её имени
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'
