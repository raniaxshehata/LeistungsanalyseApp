from my_classes import Subject

def test_workflow():
    # Erstellen und Registrieren einer neuen Person
    subject = Subject("Mark", "john@example.com")
    subject.put()
    
    # Email-Adresse aktualisieren
    subject.update_email("new_mark@example.com")

    print("E-Mail aktualisiert:", subject.email)

if __name__ == "__main__":
    test_workflow()
