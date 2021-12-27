from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# SQLAlchemyの「エンジン」を作成
"""
デフォルトでは、各スレッドが独立したリクエストを処理することを前提として、SQLiteは1つのスレッドのみがSQLiteと通信できるようにしている。
これは、異なるもの（異なる要求）に対して誤って同じ接続を共有することを防ぐため。
ただし、FastAPIでは、通常の関数（def）を使用すると、同じ要求に対して複数のスレッドがデータベースと対話する可能性があるため、
SQLiteに。でそれを許可する必要があることを通知する必要がありconnect_args={"check_same_thread": False}にする。
"""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# SessionLocalクラスの各インスタンスはデータベースセッションになる。クラス自体はまだデータベースセッションではない。
# SessionLocalクラスのインスタンスを作成すると、このインスタンスが実際のデータベースセッションになる。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# このクラスから継承して、各データベースモデルまたはクラス（ORMモデル）を作成する
Base = declarative_base()
