from django.test import TestCase
from .models import Note, Category
from django.urls import reverse

class NoteTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Test Category")
        self.note = Note.objects.create(
            title="Test note",
            text="This is the test note",
            category=self.category
        )
    
    def test_create_note(self):
        response = self.client.post(reverse('create_note'), {
            'title': 'New note',
            'text': 'This is the new note',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 302)

        new_note = Note.objects.get(title='New note')
        self.assertEqual(new_note.text, 'This is the new note')

    def test_edit_note(self):
        response = self.client.post(reverse('edit_note', args=[self.note.id]), {
            'title': 'Updated note',
            'text': 'This note has been updated',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 302)

        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated note')
        self.assertEqual(updated_note.text, 'This note has been updated')

    def test_delete_note(self):
        response = self.client.get(reverse('delete_note', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)

        deleted_note_exists = Note.objects.filter(id=self.note.id).exists()
        self.assertFalse(deleted_note_exists)

    def test_view_note_detail(self):
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note')

