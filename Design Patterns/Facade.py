"""
The Facade design pattern is a structural pattern that provides a simplified interface to a complex subsystem or set of classes.
It hides the complexities of the subsystem and provides an easy-to-use interface, making the subsystem easier to interact with.
This pattern is particularly useful when dealing with complex systems, APIs, or libraries,
where the user might need only a small subset of functionalities or where the system's internal complexity needs to be hidden.

Key Components of the Facade Pattern:
    Facade: The class that provides a simplified interface to the subsystem.
    Subsystem Classes: The complex classes or components that perform the actual work but are hidden behind the facade.

Benefits:
    Simplifies usage: Provides a simple interface to a complex subsystem.
    Decouples the client: Reduces dependencies between the client and the subsystem.
    Promotes subsystem independence: Allows the subsystem to evolve independently from the client.

"""

class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def off(self):
        print("DVD Player is off")

    def play(self, movie):
        print(f"Playing movie: {movie}")

class SoundSystem:
    def on(self):
        print("Sound System is on")

    def off(self):
        print("Sound System is off")

    def set_volume(self, level):
        print(f"Setting volume to {level}")

class Projector:
    def on(self):
        print("Projector is on")

    def off(self):
        print("Projector is off")

    def set_input(self, input_source):
        print(f"Projector input set to {input_source}")

class HomeTheaterFacade:
    def __init__(self, dvd_player, sound_system, projector):
        self.dvd_player = dvd_player
        self.sound_system = sound_system
        self.projector = projector

    def watch_movie(self, movie):
        print("Getting ready to watch a movie...")
        self.dvd_player.on()
        self.dvd_player.play(movie)
        self.sound_system.on()
        self.sound_system.set_volume(10)
        self.projector.on()
        self.projector.set_input("DVD")
        print("Movie is playing. Enjoy!")

    def end_movie(self):
        print("Shutting down the home theater...")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        print("Home theater is off.")

# Usage
dvd_player = DVDPlayer()
sound_system = SoundSystem()
projector = Projector()

home_theater = HomeTheaterFacade(dvd_player, sound_system, projector)
home_theater.watch_movie("Inception")
home_theater.end_movie()
