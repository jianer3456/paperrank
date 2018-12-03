# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    acdemic_unit = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = True
        db_table = 'author'

    def insert(self, firstName, lastName, Unit):
        obj = Author(first_name=firstName, last_name=lastName, acdemic_unit=Unit)
        obj.save()

class Paper(models.Model):
    url = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateField()
    field = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cited_times = models.IntegerField()
    issn = models.CharField(db_column='ISSN', unique=True, max_length=100)  # Field name made lowercase.
    pages = models.CharField(max_length=100)
    sponsored = models.CharField(db_column='Sponsored', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'paper'

    def insert(self, url, title, date, field, publisher, cited_times,\
                issn, pages, sponsored):
        obj = Paper(url=url, title=title, date=date, field=field, publisher=publisher, \
                    cited_times=cited_times, issn=issn, pages=pages, sponsored=sponsored)
        obj.save()


class PaperAuthor(models.Model):
    paperid = models.ForeignKey(Paper, models.DO_NOTHING, db_column='paperid', primary_key=True)
    authorid = models.ForeignKey(Author, models.DO_NOTHING, db_column='authorid')
    author_type = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'paper_author'
        unique_together = (('paperid', 'authorid'),)

    def insert(self, paperid, authorid, authortype):
        paper = Paper.objects.get(id=paperid)
        author = Author.objects.get(id=authorid)
        paper.paperauthor_set.create(paperid=paper, authorid=author, author_type=authortype)



