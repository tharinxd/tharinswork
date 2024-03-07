class PersonManager:
    def __init__(self):
        self.id_to_name_mapping = {}

    def assign_id(self, person_id, person_name):
        """Assigns an ID to a person."""
        self.id_to_name_mapping[person_id] = person_name

    def get_name_by_id(self, person_id):
        """Gets the name associated with a given ID."""
        return self.id_to_name_mapping.get(person_id, "Name not found")

# Example usage
if __name__ == "__main__":
    person_manager = PersonManager()

    # Assigning IDs to people
    person_manager.assign_id(1, "Sourav")
    person_manager.assign_id(2, "Pratyush")
    person_manager.assign_id(3, "Tharin")

    # Retrieving names based on IDs
    user_id = 2
    user_name = person_manager.get_name_by_id(user_id)

    # Printing the result
    print(f"The name associated with ID {user_id} is: {user_name}")
