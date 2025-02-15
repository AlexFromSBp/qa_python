from main import BooksCollector


class TestBooksCollector:

    def test_get_books_for_children_without_age_rating(self):
        collector = BooksCollector()
        # Добавляем первую книгу
        collector.add_new_book('Как я встретил зомби')
        # Устанавливаем жанр
        collector.set_book_genre('Как я встретил зомби', 'Ужасы')

        # Добавляем вторую книгу
        collector.add_new_book('Сказки Андерсена')
        # Устанавливаем жанр
        collector.set_book_genre('Сказки Андерсена', 'Фантастика')

        # Проверяем сколько книг подходит для детей
        assert len(collector.get_books_for_children()) == 1
