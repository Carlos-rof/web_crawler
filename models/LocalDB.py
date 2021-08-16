import sqlite3
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path


class DB:
    app_path = Path.cwd()  # Mapea o caminho do Script
    connection = sqlite3.connect(f'{app_path}/ScrapedData.db')
    engine = create_engine(f'sqlite:///{app_path}/ScrapedData.db', echo=False)
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    class Tables(Base):
        __tablename__ = 'dados'

        id = Column(Integer, primary_key=True)
        score = Column(String, unique=False)
        storage = Column(String, unique=False)
        cpu = Column(String, unique=False)
        memory = Column(String, unique=False)
        bandwidth = Column(String, unique=False)
        price = Column(String, unique=False)
        hr_price = Column(String, unique=False)
        date = Column(String, unique=False)
        tipo = Column(String, unique=False)
        scraped_page = Column(String, unique=False)

        def __init__(self, score, storage, cpu, memory, bandwidth, price, hr_price, date, tipo, scraped_page):
            self.score = score
            self.storage = storage
            self.cpu = cpu
            self.memory = memory
            self.bandwidth = bandwidth
            self.price = price
            self.hr_price = hr_price
            self.date = date
            self.tipo = tipo
            self.scraped_page = scraped_page

        def __repr__(self):
            return "<Tables(score='%s', storage='%s', cpu,='%s' memory='%s', bandwidth='%s', price='%s', " \
                   "hr_price='%s', date='%s', tipo='%s', scraped page='%s')>" % (
                       self.score, self.storage, self.cpu, self.memory, self.bandwidth, self.price, self.hr_price,
                       self.date,
                       self.tipo, self.scraped_page
                   )

    Base.metadata.create_all(engine)

    @classmethod
    def fill_db(cls, **dados):
        objeto = DB.Tables(**dados)
        cls.session.add(objeto)
        cls.session.commit()
        return

    @classmethod
    def consult_db(cls):
        result = cls.session.query(DB.Tables)
        return result
