import io

import cv2
from telegram import Bot


class TelegramBotHelper:
    def __init__(self, token: str, chat_id: str):
        """
        Initializes the Telegram bot helper.
        :param token: Bot token from BotFather
        :param chat_id: Telegram chat ID where messages will be sent
        """
        self.bot = Bot(token=token)
        self.token = token
        self.chat_id = chat_id

    async def send_message(self, message: str):
        """
        Sends a plain text message to the chat.
        :param message: The text message to send
        """
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message)
            print(f"Message sent: {message}")
        except Exception as e:
            print(f"Failed to send message: {e}")

    async def send_ndarray_image(self, image, caption: str = ""):
        """
        Sends a NumPy ndarray image to the chat.
        :param image: Image in ndarray format (e.g., OpenCV image)
        :param caption: Optional caption for the image
        """
        try:
            is_success, buffer = cv2.imencode(".jpg", image)
            if not is_success:
                raise ValueError("Could not encode image to JPG format.")

            image_bytes = io.BytesIO(buffer.tobytes())
            image_bytes.name = "image.jpg"

            await self.bot.send_photo(chat_id=self.chat_id, photo=image_bytes, caption=caption)
            print("Image sent successfully.")
        except Exception as e:
            print(f"Failed to send ndarray image: {e}")