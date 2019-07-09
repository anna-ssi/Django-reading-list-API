from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    rating = models.FloatField(null=True, blank=True)
    review_count = models.IntegerField(null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True)
    page = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'books'
        ordering = ('title',)

    def create(self, data):
        self.title = data['title']
        self.description = data['description']
        self.author = data['author']
        self.rating = data['rating']
        self.review_count = data['review_count']
        self.rating_count = data['rating_count']
        self.page = data['page']

        self.save()
        return self

    def __str__(self):
        return self.title
