#High-level modules (which contain complex logic)
#should not directly depend on low-level modules (which provide utility functionality).
#Instead, both should depend on abstractions.

#Abstractions (e.g., interfaces or abstract classes) should not depend on concrete implementations.
#Concrete implementations should depend on abstractions.

# class WeatherService:
#     def get_weather(self):
#         # Imagine this method fetches weather data from an external API
#         return "Sunny"

# class WeatherReporter:
#     def __init__(self):
#         self.weather_service = WeatherService()

#     def report(self):
#         weather = self.weather_service.get_weather()
#         print(f"The weather today is {weather}")

# reporter = WeatherReporter()
# reporter.report()

from abc import ABC, abstractmethod

class WeatherServiceInterface(ABC):
    @abstractmethod
    def get_weather(self):
        pass

class WeatherService(WeatherServiceInterface):
    def get_weather(self):
        # Imagine this method fetches weather data from an external API
        return "Sunny"

class WeatherReporter:
    def __init__(self, weather_service: WeatherServiceInterface):
        self.weather_service = weather_service

    def report(self):
        weather = self.weather_service.get_weather()
        print(f"The weather today is {weather}")

# Now, we can easily switch implementations of WeatherServiceInterface
weather_service = WeatherService()
reporter = WeatherReporter(weather_service)
reporter.report()
