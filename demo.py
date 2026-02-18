# Simple CRUD Operations

class CRUDApp:
    def __init__(self):
        self.data = {}
        self.id_counter = 1
    
    def create(self, name, email):
        """Create a new record"""
        self.data[self.id_counter] = {"name": name, "email": email}
        print(f"Record created with ID: {self.id_counter}")
        self.id_counter += 1
    
    def read(self, record_id):
        """Read a record by ID"""
        if record_id in self.data:
            return self.data[record_id]
        return "Record not found"
    
    def update(self, record_id, name=None, email=None):
        """Update a record"""
        if record_id in self.data:
            if name:
                self.data[record_id]["name"] = name
            if email:
                self.data[record_id]["email"] = email
            print("Record updated")
        else:
            print("Record not found")
    
    def delete(self, record_id):
        """Delete a record"""
        if record_id in self.data:
            del self.data[record_id]
            print("Record deleted")
        else:
            print("Record not found")
    
    def list_all(self):
        """List all records"""
        return self.data


# Example usage
if __name__ == "__main__":
    app = CRUDApp()
    
    app.create("Alice", "alice@example.com")
    app.create("Bob", "bob@example.com")
    
    print(app.read(1))
    
    app.update(1, email="alice.new@example.com")
    
    print(app.list_all())
    
    app.delete(1)
    
    print(app.list_all())