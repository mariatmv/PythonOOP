

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = list(filter(lambda x: x.id == category_id, self.categories))
        category[0].name = new_name

    def edit_topic(self, topic_id, new_name, new_folder):
        topic = list(filter(lambda x: x.id == topic_id, self.topics))
        topic[0].name = new_name
        topic[0].storage_folder = new_folder

    def edit_document(self, document_id, new_name):
        document = list(filter(lambda x: x.id == document_id, self.documents))
        document[0].file_name = new_name

    def delete_category(self, category_id):
        category = list(filter(lambda x: x.id == category_id, self.categories))
        self.categories.remove(category[0])

    def delete_topic(self, topic_id):
        topic = list(filter(lambda x: x.id == topic_id, self.topics))
        self.topics.remove(topic[0])

    def delete_document(self, document_id):
        document = list(filter(lambda x: x.id == document_id, self.documents))
        self.documents.remove(document[0])

    def get_document(self, document_id):
        document = list(filter(lambda x: x.id == document_id, self.documents))
        return document[0]

    def __repr__(self):
        output = ''
        for doc in self.documents:
            output += Document.__repr__(doc)
        return output


