import base64
import hashlib
import logging
import validators


class URLShortener:
    def __init__(self, length=5):
        """
        Initialize the URLShortener instance.

        Args:
            length (int): The length of the shortened URL (default: 5).
        """
        self.short_length = length
        self.init_logger()

    def shorten_url(self, url):
        """
        Shorten the given URL.

        Args:
            url (str): The URL to be shortened.

        Returns:
            str or None: The shortened URL if valid, otherwise None.

        Raises:
            None.
        """
        if validators.url(url):
            hash_value = hashlib.md5(url.encode('utf-8')).digest()
            altchars = '-_'.encode('utf-8')
            hashed_url = base64.b64encode(hash_value, altchars).decode('utf-8')

            logging.info('Original URL: %s ===> Shortened URL: %s', url, hashed_url[:self.short_length])
            return hashed_url[:self.short_length]
        else:
            logging.info('Validation Failure for URL: %s', url)
            return None

    def init_logger(self):
        """
        Initialize the logger.

        Args:
            None.

        Returns:
            None.

        Raises:
            None.
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)-20s %(levelname)-9s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.FileHandler('log.log', mode='a', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
