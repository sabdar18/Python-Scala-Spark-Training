class SuperGreeter:
    def __init__(self, people_to_greet):
        self.people = people_to_greet

    def greet(self):
        for person in self.people:
            if person.islower():
                self._greet_street_style(person)
            elif len(person) > 7:
                self._greet_hawaii(person)
            else:
                self._greet_polite(person)
            
    def _greet_polite(self, name):
        greeting = "G'day {}! How are you doing?".format(name)
        print(greeting)

    def _greet_street_style(self, name):
        # import pdb; pdb.set_trace()  # UNCOMMENT
        name = name.upper()
        print('WASSUP {}!?'.format(name))

    def _greet_hawaii(self, name):
        print('Aloha {}!'.format(name))


def main():
    people = ['John Doe', 'Donald', 'Lisa', 'alex']
    # import pdb; pdb.set_trace()  # UNCOMMENT
    greeter = SuperGreeter(people)
    greeter.greet()


main()