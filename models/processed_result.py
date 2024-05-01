class ProcessResult:
    def __init__(self) -> None:
        self.given_seq: str = ""
        self.generated_seq: list[int] = []