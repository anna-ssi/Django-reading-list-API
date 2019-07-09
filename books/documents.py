from django_elasticsearch_dsl import DocType, Index

from books.models import Book

posts = Index('books')


@posts.doc_type
class BookDocument(DocType):
    class Meta:
        model = Book

        fields = [
            'title',
            'description',
            'author',
            'rating',
            'review_count',
            'rating_count',
            'page'
        ]
