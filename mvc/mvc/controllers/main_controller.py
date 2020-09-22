from mvc.models.repositories.note_repository import NoteRepository

class MainController:
    def __init__(self):
        # Create note repository here
        # Your code here
        self.noterepo = NoteRepository()
        # pass
    
    def get_all_notes(self):
        # Return all notes
        # Your code here
        return self.noterepo.get_all_notes()

    def add_note(self, note: str):
        # Add note
        # Your code here
        return self.noterepo.add_note(note)
        

    def clear_all(self):
        # Clear all note
        # Your code here
        return self.noterepo.clear_all_notes()
