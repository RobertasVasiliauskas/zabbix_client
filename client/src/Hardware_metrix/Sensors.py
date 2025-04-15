import psutil


class Sensors:
    def __init__(self):
        pass

    @staticmethod
    def get_sensors(fahrenheit: bool = False) -> list[dict]:
        """
        Retrieve a list of temperature sensors and their readings.

        :param fahrenheit: A boolean indicating whether to return temperatures in Fahrenheit. If `False`, temperatures are returned in Celsius. Defaults to `False`.
        :return: A list of dictionaries, where each dictionary represents a sensor
        """
        sensors = []

        for sensor, readings in psutil.sensors_temperatures(fahrenheit=fahrenheit).items():
            for reading in readings:
                sensor_info = {
                    'sensor': sensor,
                    'label': reading.label,
                    'current': reading.current,
                    'high': reading.high,
                    'critical': reading.critical
                }
                sensors.append(sensor_info)

        return sensors

    @staticmethod
    def get_fan_speeds() -> list[dict]:
        """
        Retrieve a list of fan speeds.

        :return: A list of dictionaries, where each dictionary represents a fan and its speed.
        """
        fans = []

        for fan, readings in psutil.sensors_fans().items():
            for reading in readings:
                fan_info = {
                    'fan': fan,
                    'current': reading.current
                }
                fans.append(fan_info)

        return fans

