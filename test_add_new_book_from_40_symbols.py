import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize('book', [
        'Мануал разных способов откосить от работ',
        'Гордость и предубеждение и зомби и страх',
        'Гаррик поттер и философский камень часть'
    ])
    def test_add_three_books(self, book):
        collector = BooksCollector()

        # Добавляем три книги
        collector.add_new_book('Мануал разных способов откосить от работ')
        collector.add_new_book('Гордость и предубеждение и зомби и страх')
        collector.add_new_book('Гаррик поттер и философский камень часть')

        # Проверяем, что книги добавлены
        assert len(collector.books_genre) == 3