# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BooksAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'books_author'


class BooksBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    publisher = models.ForeignKey('BooksPublisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book'


class BooksBookAuthors(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.ForeignKey(BooksBook, models.DO_NOTHING)
    author = models.ForeignKey(BooksAuthor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_authors'
        unique_together = (('book', 'author'),)


class BooksPublisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'books_publisher'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PollsChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Yes24BookDetail(models.Model):
    book_id = models.TextField(blank=True, null=True)
    page = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    book_intro = models.TextField(blank=True, null=True)
    pub_book_intro = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes24_book_detail'


class Yes24BookReviews(models.Model):
    book_id = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes24_book_reviews'


class Yes24OneLineReviews(models.Model):
    book_id = models.TextField(blank=True, null=True)
    one_line_review = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes24_one_line_reviews'


class Yes24Best200801202311(models.Model):
    book_id = models.TextField(blank=True, null=True)
    yy = models.BigIntegerField(blank=True, null=True)
    mon = models.BigIntegerField(blank=True, null=True)
    title_h = models.TextField(blank=True, null=True)
    title_f = models.TextField(blank=True, null=True)
    title_m = models.TextField(blank=True, null=True)
    title_e = models.TextField(blank=True, null=True)
    detail_link = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    pub_date = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    n_reviews = models.TextField(blank=True, null=True)
    review_link = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes24best200801_202311'


class Yes24BestReviews(models.Model):
    book_id = models.BigIntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes24best_reviews'


class Yes24Bestlist(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    book_id = models.TextField(blank=True, null=True)
    yy = models.BigIntegerField(blank=True, null=True)
    mon = models.BigIntegerField(blank=True, null=True)
    title_h = models.TextField(blank=True, null=True)
    title_m = models.TextField(blank=True, null=True)
    title_e = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    pub_date = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    page = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    pub_book_intro = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes24bestlist'
