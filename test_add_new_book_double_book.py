from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_double_book(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # Проверяем, что книга добавлена в books_genre
        assert len(collector.get_books_genre()) == 1, 'Ошибка!'
