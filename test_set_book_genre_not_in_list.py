from main import BooksCollector


class TestBooksCollector:

    def test_set_book_genre_not_in_list(self):
        collector = BooksCollector()
        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение')
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение', 'Документалка')

        # Проверяем, что жанр не установлен
        assert collector.get_book_genre('Гордость и предубеждение и зомби') != 'Документалка'
