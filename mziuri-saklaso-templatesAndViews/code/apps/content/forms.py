from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = [
            "title", "author", "written_date", "created_at", "like_count",
        ]