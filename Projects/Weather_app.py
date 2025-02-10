import sys
import requests
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt6.QtCore import Qt


class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App")
        v_box = QVBoxLayout()
        v_box.addWidget(self.city_label)
        v_box.addWidget(self.city_input)
        v_box.addWidget(self.get_weather_button)
        v_box.addWidget(self.temperature_label)
        v_box.addWidget(self.emoji_label)
        v_box.addWidget(self.description_label)

        self.setLayout(v_box)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel,QPushButton{
                font-family: Times New Roman;               
            }
            QLabel#city_label{
                font-size: 40px ;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px
            }
            QPushButton#get_weather_button{
                font-size:30px;
                font-weight:bold
            }
            QLabel#temperature_label{
                   font-size:75px      
            }
            QLabel#emoji_label{
                font-size:100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size:70px
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        api_key= "ca4d6fbe79b6e170f01415d7a58474fd"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease Check Your Input")
                case 401:
                    self.display_error("Unautorized\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is Denied")
                case 404:
                    self.display_error("Not Found:\nCity Not Found")
                case 500:
                    self.display_error("Internal Service Error:\nPlease Try Again Later")
                case 501:
                    self.display_error("Bad Gateway:\nInvalid Response From the Server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is Down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo Response From the Server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck Your Internet Connection")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the URL")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe Request Timed Out")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")



    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size:30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size:60px")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]



        self.temperature_label.setText(f"{temperature_c:.1f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <=531:
            return "⛈"
        elif 600<= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌬"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather = Weather()
    weather.show()
    sys.exit(app.exec())