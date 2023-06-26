import os.path as osp
import tempfile
from uuid import uuid4

import qrcode


class QRGenerator:
    def __init__(self, vcard: str, qr_version: int = 2, qr_box_size: int = 10) -> None:
        self.vcard = vcard
        self.qr_version = qr_version
        self.qr_box_size = qr_box_size
        self.img: qrcode.image.pure.PyPNGImage | None = None
        self.result: bytes | None = None

    def _generate(self) -> None:
        qr = qrcode.QRCode(
            version=self.qr_version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.qr_box_size,
        )

        qr.add_data(self.vcard)
        qr.make(fit=True)

        self.img = qr.make_image()

    def run(self) -> bytes | None:
        self._generate()

        with tempfile.TemporaryDirectory() as td:
            filename = f"{uuid4()}.png"
            filepath = osp.join(td, filename)

            with open(filepath, "wb") as f:
                self.img.save(f)

            with open(filepath, "rb") as f:
                self.result = f.read()

        return self.result
