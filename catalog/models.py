from django.db import models


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="title")
    release_date = models.IntegerField(verbose_name="release_date")
    poster = models.ImageField(upload_to="posters/", verbose_name="poster", null=True)
    genre = models.CharField(max_length=100, verbose_name="genre", null=True)
    synopsis = models.TextField(verbose_name="synopsis", null=True)

    def __str__(self) -> str:
        return f""" Title: {self.title}\n
        Release Date: {self.release_date}\n
        Genre: {self.genre}\n
        Synopsis: {self.synopsis}."""

    def delete(self, using=None, keep_parents=False) -> None:
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
