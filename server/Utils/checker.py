

class Checker:

    @staticmethod
    def is_service_type_ok(service):
        """
        Check if the service name is part of the implemented service
        :return: true/false
        """
        if service in ["youtube", "weather", "deezer", "timer", "mail", "github", "reddit", "yammer"]:
            return True
        return False
