from dataclasses import dataclass


@dataclass
class BusinessCard:
    last_name: str
    first_name: str
    organization: str
    job_title: str
    email: str
    address: str | None = None
    work_phone: str | None = None
    cell: str | None = None
    fax: str | None = None
    website: str | None = None

    def convert(self) -> str:
        vcard = "BEGIN:VCARD\nVERSION:3.0\n"
        vcard += f"N:{self.last_name};{self.first_name};;\n"
        vcard += f"FN:{self.first_name} {self.last_name}\n"
        vcard += f"ORG:{self.organization}\n"
        vcard += f"TITLE:{self.job_title}\n"
        vcard += f"EMAIL:{self.email}\n"
        vcard += "" if self.address is None else f"ADR;TYPE=WORK:;;{self.address};;;;\n"
        vcard += "" if self.work_phone is None else f"TEL;WORK;VOICE:{self.work_phone}\n"
        vcard += "" if self.cell is None else f"TEL;CELL:{self.cell}\n"
        vcard += "" if self.fax is None else f"TEL;FAX:{self.fax}\n"
        vcard += "" if self.website is None else f"URL:{self.website}\n"
        vcard += "END:VCARD"
        return vcard
