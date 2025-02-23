class TestBooksCollector:

    def test_add_book_in_favorites_add_new_favorites_book(self, collector):

        collector.add_new_book('Унесенные призраками')
        # Добавляем книгу в избранное
        collector.add_book_in_favorites('Унесенные призраками')
        # Проверяем что книга в Избранном
        assert len(collector.get_list_of_favorites_books()) == 1


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

        # Получаем список книг с жанром 'Мультфильмы'
        result = collector.get_books_with_specific_genre('Мультфильмы')

        # Проверяем, что список содержит правильные книги
        assert len(result) == 2


    def test_set_book_genre_from_list(self, collector):
        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        # Проверяем соответствие заданного жанра книги сохраненному
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'


    @pytest.mark.parametrize('book_name, genre', [
        ('Дорога домой', 'Неизвестный'),
    ])
    def test_get_book_genre_not_from_list(self, collector, book_name, genre):
        # Добавляем книгу
        collector.add_new_book(book_name)
        # Устанавливаем жанр не их списка жанров
        collector.set_book_genre(book_name, genre)
        # Проверяем отсутствие жанра по названию книги
        assert collector.get_book_genre(book_name) == '', 'Ошибка'



    def test_set_book_genre_not_in_list(self, collector):
        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение')
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение', 'Документалка')

        # Проверяем, что жанр не из списка не установлен
        assert collector.get_book_genre('Гордость и предубеждение') != 'Документалка'



    def test_add_new_book_double_book(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # Проверяем, что книга добавлена в books_genre
        assert len(collector.get_books_genre()) == 1, 'Ошибка!'

    def test_get_list_of_favorites_books(self, collector):
        # Добавляем книги
        collector.add_new_book('Анна Каренина')
        collector.add_new_book('Буря мечей')
        # Добавляем в избранное
        collector.add_book_in_favorites('Анна Каренина')
        collector.add_book_in_favorites('Буря мечей')
        # Проверяем наличие в списке
        assert collector.get_list_of_favorites_books() == ['Анна Каренина', 'Буря мечей']


    @pytest.mark.parametrize('book_name, genre', [
        ('Орден Феникса', 'Фантастика'),
        ('Принц-полукровка', 'Ужасы')
    ])
    def test_set_books_genre_in_dictionary(self, collector, book_name, genre):
        # Добавляем первую книги
        collector.add_new_book(book_name)
        # Устанавливаем жанр
        collector.set_book_genre(book_name, genre)
        # Проверяем наличие жанра у книг
        assert collector.get_book_genre(book_name) == genre
