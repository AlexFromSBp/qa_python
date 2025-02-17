class TestBooksCollector:

    def test_add_book_in_favorites_add_new_favorites_book(self, collector):

        collector.add_new_book('Унесенные призраками')
    # Добавляем книгу в избранное
        collector.add_book_in_favorites('Унесенные призраками')
    # Проверяем что книга в Избранном
        assert len(collector.get_list_of_favorites_books()) == 1


class TestBooksCollector:

    def test_delete_book_from_favorites_delete_one_from_favorites_book(self, collector):
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


class TestBooksCollector:

    def test_get_books_for_children_without_age_rating(self, collector):
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


class TestBooksCollector:

    def test_get_books_with_specific_genre_only_multfilm(self, collector):
        # Добавляем книги и устанавливаем им жанры
        books_genre = {
            'Король Лев': 'Мультфильмы',
            'Шрек': 'Мультфильмы',
            'Гарри Поттер': 'Фантастика',
            'Дракула': 'Ужасы'
        }

        for book, genre in books_genre.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        # Получаем список книг с жанром "Мультфильмы"
        result = collector.get_books_with_specific_genre('Мультфильмы')

        # Проверяем, что список содержит правильные книги
        assert len(result) == 2


class TestBooksCollector:

    def test_set_book_genre_from_list(self, collector):
        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        # Проверяем соответствие заданного жанра книги сохраненному
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'


class TestBooksCollector:

    def test_get_book_genre_know_name(self, collector):
        # Добавляем первую книги
        collector.add_new_book('Кубок огня')
        collector.add_new_book('Тайная комната')
        # Устанавливаем жанр
        collector.set_book_genre('Кубок огня', 'Ужасы')
        collector.set_book_genre('Тайная комната', 'Фантастика')

        # Получаем жанр по названию книги
        print(collector.get_book_genre('Кубок огня'))
        print(collector.get_book_genre('Тайная комната'))

class TestBooksCollector:

    def test_set_book_genre_not_in_list(self, collector):
        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение')
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение', 'Документалка')

        # Проверяем, что жанр не из списка не установлен
        assert collector.get_book_genre('Гордость и предубеждение') != 'Документалка'


class TestBooksCollector:

    def test_add_new_book_double_book(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # Проверяем, что книга добавлена в books_genre
        assert len(collector.get_books_genre()) == 1, 'Ошибка!'


import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('books', [
        [
            'Мануал разных способов откосить от работ',
            'Гордость и предубеждение и зомби и страх',
            'Гаррик Поттер и философский камень часть'
        ]
    ])
    def test_get_list_of_favorites_books(self, collector, books):
        # Добавляем книги
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        # Получаем список избранных книг
        favorites = collector.get_list_of_favorites_books()

        # Выводим список в консоль
        print(len(favorites))  # Количество книг в избранном
        print(favorites)


class TestBooksCollector:

    def test_get_books_genre_in_dictionary(self, collector):
        # Добавляем первую книги
        collector.add_new_book('Орден Феникса')
        collector.add_new_book('принц-полукровка')
        # Устанавливаем жанр
        collector.set_book_genre('Орден Феникса', 'Ужасы')
        collector.set_book_genre('принц-полукровка', 'Фантастика')

        # Получаем словарь
        print(collector.get_books_genre())
