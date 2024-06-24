class Entity:
    # function to create an instance of "Entity"
    def __init__(self, name):
        # Add the name of the entity as its attribute
        self.name = name

    # function to add a relation that applies to all instances of this entity by default
    def add_default_relation(self, relation, entity):
        if relation not in self.default_relations:
            self.default_relations[relation] = []
        self.default_relations[relation].append(entity)


class Person(Entity):
    def __init__(self, name):
        # use function from parent class to create an instance of "Person"
        super().__init__(name)

        # implement as default that everyone likes puppies
        self.add_default_relation("likes", "Puppy")


class Animal(Entity):
    def __init__(self, name):
        super().__init__(name)
        # implement as default that all animals want food
        self.add_default_relation("wants", "food")


class Student(Person):
    def __init__(self, name, school):
        # use function from parent class to create an instance of "Student"
        super().__init__(name)


class Relationship:
    def __init__(self, entity1, relation, entity2):
        self.entity1 = entity1
        self.relation = relation
        self.entity2 = entity2

    def add_default_relation(self, relation, entity):
        if relation not in self.default_relations:
            self.default_relations[relation] = []
        self.default_relations[relation].append(entity)


class SemanticNetwork:
    def __init__(self):
        self.entities = {}
        self.relationships = []

    def add_entity(self, name):
        if name not in self.entities:
            self.entities[name] = Entity(name)

    def add_relationship(self, entity1, relation, entity2):
        if entity1 in self.entities and entity2 in self.entities:
            self.relationships.append(Relationship(entity1, relation, entity2))

    def query(self, entity1, relation, entity2):
        return any(rel.entity1 == entity1 and rel.relation == relation and rel.entity2 == entity2 for rel in
                   self.relationships)



# Create a semantic network

network = SemanticNetwork()

# Add three characters
network.add_entity(Person("Romeo"))
network.add_entity(Person("Julia"))
network.add_entity(Person("Benvolio"))

# Add a puppy
network.add_entity(Animal("Puppy"))

# Add relationships
network.add_relationship("Romeo", "knows", "Benvolio")
network.add_relationship("Romeo", "knows", "Juliet")
network.add_relationship("Romeo", "is cousin of", "Benvolio")
network.add_relationship("Romeo", "is in love with", "Juliet")



# Query examples
print(network.query("Romeo", "knows", "Benvolio"))    # Output: True
print(network.query("Romeo", "likes", "Puppy")) # Output: True
print(network.query("Juliet", "is cousin of", "Benvolio")) # Output: False



