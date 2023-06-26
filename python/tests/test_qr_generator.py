import unittest

import cv2
import numpy as np

from core.qr_generator import QRGenerator
from entity.business_card_entity import BusinessCard


class TestQRCode(unittest.TestCase):

    def setUp(self) -> None:
        business_card = BusinessCard(
            last_name="John",
            first_name="Doe",
            organization="World Corporation",
            job_title="Developer",
            email="john@exmaple.com",
            cell="123-456-7890",
        )

        self.vcard = business_card.convert()
    
    def test_qr_code(self):
        qr = QRGenerator(self.vcard)
        qr_img_binary = qr.run()

        encoded_img = np.frombuffer(qr_img_binary, np.uint8)
        img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

        qr_detect = cv2.QRCodeDetector()
        value, _, _ = qr_detect.detectAndDecode(img)

        self.assertEqual(self.vcard, value)
