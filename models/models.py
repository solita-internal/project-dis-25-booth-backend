from typing import List, Optional
from sqlalchemy import Boolean, DateTime, ForeignKeyConstraint, Identity, Integer, PrimaryKeyConstraint, Unicode, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

class Base(DeclarativeBase):
    pass


class Questions(Base):
    __tablename__ = 'questions'
    __table_args__ = (
        PrimaryKeyConstraint('Id', name='PK__question__3214EC0750BA1A9E'),
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_text: Mapped[Optional[str]] = mapped_column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    category: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    order: Mapped[Optional[int]] = mapped_column(Integer)
    active: Mapped[Optional[bool]] = mapped_column(Boolean)

    responses: Mapped[List['Responses']] = relationship('Responses', back_populates='question')


class SurveySession(Base):
    __tablename__ = 'survey_session'
    __table_args__ = (
        PrimaryKeyConstraint('Id', name='PK__Survey_S__3214EC07CDACCC77'),
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    contact_opt_in: Mapped[Optional[bool]] = mapped_column(Boolean)
    name: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    email: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    organization: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    location: Mapped[Optional[str]] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    responses: Mapped[List['Responses']] = relationship('Responses', back_populates='session')


class Responses(Base):
    __tablename__ = 'responses'
    __table_args__ = (
        ForeignKeyConstraint(['question_id'], ['questions.Id'], name='FK__responses__quest__628FA481'),
        ForeignKeyConstraint(['session_id'], ['survey_session.Id'], name='FK__responses__sessi__619B8048'),
        PrimaryKeyConstraint('id', name='PK__response__3213E83F3CA8CEBB')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    session_id: Mapped[int] = mapped_column(Integer)
    question_id: Mapped[int] = mapped_column(Integer)
    answer_text: Mapped[Optional[str]] = mapped_column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    timestamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('(getdate())'))

    question: Mapped['Questions'] = relationship('Questions', back_populates='responses')
    session: Mapped['SurveySession'] = relationship('SurveySession', back_populates='responses')
