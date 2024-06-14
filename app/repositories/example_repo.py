class ExampleRepo:
    def __init__(self, db):
        self.db = db

    def get_example(self, name):
        return self.db.get(name)

    def save_example(self, example):

        self.db.save(example)

        return example

    def delete_example(self, name):
        return self.db.delete(name)


"""_summary_
    
    For CRUD operations

"""
