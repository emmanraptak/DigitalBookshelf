from enum import Enum


class ReadingStatus(Enum):
    TBR = 'TBR'
    READING = 'READING'
    READ = 'READ'
    DNF = 'DNF'